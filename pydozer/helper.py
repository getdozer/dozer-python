import io
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import ProtoReflectionDescriptorDatabase
from google.protobuf.descriptor_pool import DescriptorPool
import polars as pl
from pydozer.ingest_pb2 import IngestRequest, IngestArrowRequest
from pydozer.types_pb2 import Record, Value
from decimal import Decimal
import pyarrow as pa
import json


def describe_services(channel) -> dict:
    # https://github.com/grpc/grpc/blob/master/doc/python/server_reflection.md

    reflection_db = ProtoReflectionDescriptorDatabase(channel)
    desc_pool = DescriptorPool(reflection_db)
    services = reflection_db.get_services()

    service_dict = {}
    for s in services:
        methods = []
        print(s)
        print("  Methods: ")
        service_desc = desc_pool.FindServiceByName(
            s)
        for m in service_desc.methods:
            methods.append(m.name)
        service_dict[s] = methods
    return service_dict


def get_desc_pool(channel) -> DescriptorPool:
    reflection_db = ProtoReflectionDescriptorDatabase(channel)
    return DescriptorPool(reflection_db)


def get_arrow_schema(df, schema_name) -> dict:
    fields = []
    for (name, typ) in zip(df.columns, df.dtypes):
        dict = {
            "dict_id": 0,
            "dict_is_ordered": False,
            "metadata": {}
        }
        if typ == pl.Datetime:
            dict["data_type"] = "Timestamp"
        else:
            dict["data_type"] = str(typ)

        dict["name"] = name
        dict["nullable"] = True
        fields.append(dict)
    return {
        "name": schema_name,
        "schema": {
            "fields": fields,
            "metadata": {}
        }
    }


def get_schema(df, schema_name) -> dict:
    fields = []
    for (name, typ) in zip(df.columns, df.dtypes):
        dict = {}
        if typ == pl.UInt64 or typ == pl.UInt32 or typ == pl.UInt64:
            dict["typ"] = 'UInt'
        if typ == pl.Int64 or typ == pl.Int32 or typ == pl.Int64:
            dict["typ"] = 'Int'
        elif typ == pl.Float64 or typ == pl.Float32:
            dict["typ"] = 'Float'
        elif typ == pl.Boolean:
            dict["typ"] = 'Boolean'
        elif typ == pl.Utf8:
            dict["typ"] = 'String'
        elif typ == pl.Date:
            dict["typ"] = 'Date'
        elif typ == pl.Datetime:
            dict["typ"] = 'String'
        elif typ == pl.Time:
            dict["typ"] = 'String'
        elif type == pl.Binary:
            dict["typ"] = 'Binary'
        else:
            dict["typ"] = 'Text'
        dict["name"] = name
        dict["nullable"] = True

        fields.append(dict)

    return {
        "name": schema_name,
        "schema": {
            "fields": fields
        }
    }


def map_value(col, typ) -> Value:

    if col == None or str(col).strip() == "":
        return Value()

    if typ == pl.UInt64 or typ == pl.UInt32 or typ == pl.UInt64:
        return Value(uint_value=col)
    if typ == pl.Int64 or typ == pl.Int32 or typ == pl.Int64:
        return Value(int_value=col)
    elif typ == pl.Float64 or typ == pl.Float32:
        return Value(float_value=col)
    elif typ == pl.Boolean:
        return Value(bool_value=col)
    elif typ == pl.Utf8:
        return Value(string_value=col)
    elif typ == pl.Date:
        return Value(date_value=col)
    elif typ == pl.Datetime:
        # return Value(timestamp_value=col)
        return Value(string_value=str(col))
    elif typ == pl.Time:
        return Value(string_value=str(col))
    elif typ == pl.Binary:
        return Value(bytes_value=col)
    else:
        return Value()


def map_record(schema_name: str, row: list, types, idx) -> IngestRequest:
    values = []
    assert len(row) == len(types), "Row and types must be the same length"
    for i in range(len(row)):
        val = map_value(row[i], types[i])
        values.append(val)

    return IngestRequest(
        schema_name=schema_name,
        typ=0,
        old=None,
        new=values,
        seq_no=idx
    )


def map_arrow_df(schema_name: str, df: pl.DataFrame, idx: int) -> IngestArrowRequest:
    values = get_bytes(df)

    return IngestArrowRequest(
        schema_name=schema_name,
        records=values,
        seq_no=idx
    )


def get_bytes(df: pl.DataFrame):

    batches = df.to_arrow().to_batches()
    sink = pa.BufferOutputStream()
    for batch in batches:
        writer = pa.ipc.new_stream(sink, batch.schema)
        writer.write_batch(batch)
        writer.close()
    buf = sink.getvalue()
    return buf.to_pybytes()
