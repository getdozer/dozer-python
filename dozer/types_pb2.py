# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0btypes.proto\x12\x0b\x64ozer.types\"\x9c\x01\n\tOperation\x12\'\n\x03typ\x18\x01 \x01(\x0e\x32\x1a.dozer.types.OperationType\x12%\n\x03old\x18\x02 \x01(\x0b\x32\x13.dozer.types.RecordH\x00\x88\x01\x01\x12 \n\x03new\x18\x03 \x01(\x0b\x32\x13.dozer.types.Record\x12\x15\n\rendpoint_name\x18\x04 \x01(\tB\x06\n\x04_old\"=\n\x06Record\x12\"\n\x06values\x18\x01 \x03(\x0b\x32\x12.dozer.types.Value\x12\x0f\n\x07version\x18\x02 \x01(\r\"?\n\x0cRecordWithId\x12\n\n\x02id\x18\x01 \x01(\x04\x12#\n\x06record\x18\x02 \x01(\x0b\x32\x13.dozer.types.Record\"u\n\x0bSchemaEvent\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x04\x12\x15\n\rprimary_index\x18\x03 \x03(\x05\x12,\n\x06\x66ields\x18\x04 \x03(\x0b\x32\x1c.dozer.types.FieldDefinition\"Q\n\x0f\x46ieldDefinition\x12\x1e\n\x03typ\x18\x01 \x01(\x0e\x32\x11.dozer.types.Type\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08nullable\x18\x03 \x01(\x08\"\xdf\x01\n\x05Value\x12\x14\n\nuint_value\x18\x02 \x01(\x04H\x00\x12\x13\n\tint_value\x18\x03 \x01(\x03H\x00\x12\x15\n\x0b\x66loat_value\x18\x04 \x01(\x02H\x00\x12\x14\n\nbool_value\x18\x05 \x01(\x08H\x00\x12\x16\n\x0cstring_value\x18\x06 \x01(\tH\x00\x12\x15\n\x0b\x62ytes_value\x18\x07 \x01(\x0cH\x00\x12.\n\x0b\x61rray_value\x18\x08 \x01(\x0b\x32\x17.dozer.types.ArrayValueH\x00\x12\x16\n\x0c\x64ouble_value\x18\t \x01(\x01H\x00\x42\x07\n\x05value\"5\n\nArrayValue\x12\'\n\x0b\x61rray_value\x18\x02 \x03(\x0b\x32\x12.dozer.types.Value*G\n\tEventType\x12\x07\n\x03\x41LL\x10\x00\x12\x0f\n\x0bINSERT_ONLY\x10\x01\x12\x0f\n\x0bUPDATE_ONLY\x10\x02\x12\x0f\n\x0b\x44\x45LETE_ONLY\x10\x03*3\n\rOperationType\x12\n\n\x06INSERT\x10\x00\x12\n\n\x06\x44\x45LETE\x10\x01\x12\n\n\x06UPDATE\x10\x02*\x83\x01\n\x04Type\x12\x08\n\x04UInt\x10\x00\x12\x07\n\x03Int\x10\x01\x12\t\n\x05\x46loat\x10\x02\x12\x0b\n\x07\x42oolean\x10\x03\x12\n\n\x06String\x10\x04\x12\x08\n\x04Text\x10\x05\x12\n\n\x06\x42inary\x10\x06\x12\x0b\n\x07\x44\x65\x63imal\x10\x07\x12\r\n\tTimestamp\x10\x08\x12\x08\n\x04\x44\x61te\x10\t\x12\x08\n\x04\x42son\x10\nb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EVENTTYPE._serialized_start=798
  _EVENTTYPE._serialized_end=869
  _OPERATIONTYPE._serialized_start=871
  _OPERATIONTYPE._serialized_end=922
  _TYPE._serialized_start=925
  _TYPE._serialized_end=1056
  _OPERATION._serialized_start=29
  _OPERATION._serialized_end=185
  _RECORD._serialized_start=187
  _RECORD._serialized_end=248
  _RECORDWITHID._serialized_start=250
  _RECORDWITHID._serialized_end=313
  _SCHEMAEVENT._serialized_start=315
  _SCHEMAEVENT._serialized_end=432
  _FIELDDEFINITION._serialized_start=434
  _FIELDDEFINITION._serialized_end=515
  _VALUE._serialized_start=518
  _VALUE._serialized_end=741
  _ARRAYVALUE._serialized_start=743
  _ARRAYVALUE._serialized_end=796
# @@protoc_insertion_point(module_scope)
