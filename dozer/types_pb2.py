# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: types.proto
"""Generated protocol buffer code."""
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0btypes.proto\x12\x0b\x64ozer.types\x1a\x1fgoogle/protobuf/timestamp.proto\"\xbc\x01\n\tOperation\x12\'\n\x03typ\x18\x01 \x01(\x0e\x32\x1a.dozer.types.OperationType\x12%\n\x03old\x18\x02 \x01(\x0b\x32\x13.dozer.types.RecordH\x00\x88\x01\x01\x12 \n\x03new\x18\x03 \x01(\x0b\x32\x13.dozer.types.Record\x12\x13\n\x06new_id\x18\x04 \x01(\x04H\x01\x88\x01\x01\x12\x15\n\rendpoint_name\x18\x05 \x01(\tB\x06\n\x04_oldB\t\n\x07_new_id\"=\n\x06Record\x12\"\n\x06values\x18\x01 \x03(\x0b\x32\x12.dozer.types.Value\x12\x0f\n\x07version\x18\x02 \x01(\r\"?\n\x0cRecordWithId\x12\n\n\x02id\x18\x01 \x01(\x04\x12#\n\x06record\x18\x02 \x01(\x0b\x32\x13.dozer.types.Record\"u\n\x0bSchemaEvent\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x04\x12\x15\n\rprimary_index\x18\x03 \x03(\x05\x12,\n\x06\x66ields\x18\x04 \x03(\x0b\x32\x1c.dozer.types.FieldDefinition\"Q\n\x0f\x46ieldDefinition\x12\x1e\n\x03typ\x18\x01 \x01(\x0e\x32\x11.dozer.types.Type\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08nullable\x18\x03 \x01(\x08\"!\n\tPointType\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\"A\n\x0bRustDecimal\x12\r\n\x05\x66lags\x18\x01 \x01(\r\x12\n\n\x02lo\x18\x02 \x01(\r\x12\x0b\n\x03mid\x18\x03 \x01(\r\x12\n\n\x02hi\x18\x04 \x01(\r\"\xc6\x02\n\x05Value\x12\x14\n\nuint_value\x18\x01 \x01(\x04H\x00\x12\x13\n\tint_value\x18\x02 \x01(\x03H\x00\x12\x15\n\x0b\x66loat_value\x18\x03 \x01(\x01H\x00\x12\x14\n\nbool_value\x18\x04 \x01(\x08H\x00\x12\x16\n\x0cstring_value\x18\x05 \x01(\tH\x00\x12\x15\n\x0b\x62ytes_value\x18\x07 \x01(\x0cH\x00\x12\x31\n\rdecimal_value\x18\x08 \x01(\x0b\x32\x18.dozer.types.RustDecimalH\x00\x12\x35\n\x0ftimestamp_value\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x12\x14\n\ndate_value\x18\n \x01(\tH\x00\x12-\n\x0bpoint_value\x18\x0c \x01(\x0b\x32\x16.dozer.types.PointTypeH\x00\x42\x07\n\x05value*G\n\tEventType\x12\x07\n\x03\x41LL\x10\x00\x12\x0f\n\x0bINSERT_ONLY\x10\x01\x12\x0f\n\x0bUPDATE_ONLY\x10\x02\x12\x0f\n\x0b\x44\x45LETE_ONLY\x10\x03*3\n\rOperationType\x12\n\n\x06INSERT\x10\x00\x12\n\n\x06\x44\x45LETE\x10\x01\x12\n\n\x06UPDATE\x10\x02*\x8e\x01\n\x04Type\x12\x08\n\x04UInt\x10\x00\x12\x07\n\x03Int\x10\x01\x12\t\n\x05\x46loat\x10\x02\x12\x0b\n\x07\x42oolean\x10\x03\x12\n\n\x06String\x10\x04\x12\x08\n\x04Text\x10\x05\x12\n\n\x06\x42inary\x10\x06\x12\x0b\n\x07\x44\x65\x63imal\x10\x07\x12\r\n\tTimestamp\x10\x08\x12\x08\n\x04\x44\x61te\x10\t\x12\x08\n\x04\x42son\x10\n\x12\t\n\x05Point\x10\x0b\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _EVENTTYPE._serialized_start = 1013
    _EVENTTYPE._serialized_end = 1084
    _OPERATIONTYPE._serialized_start = 1086
    _OPERATIONTYPE._serialized_end = 1137
    _TYPE._serialized_start = 1140
    _TYPE._serialized_end = 1282
    _OPERATION._serialized_start = 62
    _OPERATION._serialized_end = 250
    _RECORD._serialized_start = 252
    _RECORD._serialized_end = 313
    _RECORDWITHID._serialized_start = 315
    _RECORDWITHID._serialized_end = 378
    _SCHEMAEVENT._serialized_start = 380
    _SCHEMAEVENT._serialized_end = 497
    _FIELDDEFINITION._serialized_start = 499
    _FIELDDEFINITION._serialized_end = 580
    _POINTTYPE._serialized_start = 582
    _POINTTYPE._serialized_end = 615
    _RUSTDECIMAL._serialized_start = 617
    _RUSTDECIMAL._serialized_end = 682
    _VALUE._serialized_start = 685
    _VALUE._serialized_end = 1011
# @@protoc_insertion_point(module_scope)
