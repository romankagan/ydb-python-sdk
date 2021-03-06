# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kikimr/public/api/grpc/ydb_scheme_v1.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kikimr.public.api.protos import ydb_scheme_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kikimr/public/api/grpc/ydb_scheme_v1.proto',
  package='Ydb.Scheme.V1',
  syntax='proto3',
  serialized_pb=_b('\n*kikimr/public/api/grpc/ydb_scheme_v1.proto\x12\rYdb.Scheme.V1\x1a)kikimr/public/api/protos/ydb_scheme.proto2\xcc\x03\n\rSchemeService\x12T\n\rMakeDirectory\x12 .Ydb.Scheme.MakeDirectoryRequest\x1a!.Ydb.Scheme.MakeDirectoryResponse\x12Z\n\x0fRemoveDirectory\x12\".Ydb.Scheme.RemoveDirectoryRequest\x1a#.Ydb.Scheme.RemoveDirectoryResponse\x12T\n\rListDirectory\x12 .Ydb.Scheme.ListDirectoryRequest\x1a!.Ydb.Scheme.ListDirectoryResponse\x12Q\n\x0c\x44\x65scribePath\x12\x1f.Ydb.Scheme.DescribePathRequest\x1a .Ydb.Scheme.DescribePathResponse\x12`\n\x11ModifyPermissions\x12$.Ydb.Scheme.ModifyPermissionsRequest\x1a%.Ydb.Scheme.ModifyPermissionsResponseB\x1a\n\x18\x63om.yandex.ydb.scheme.v1b\x06proto3')
  ,
  dependencies=[kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030com.yandex.ydb.scheme.v1'))

_SCHEMESERVICE = _descriptor.ServiceDescriptor(
  name='SchemeService',
  full_name='Ydb.Scheme.V1.SchemeService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=105,
  serialized_end=565,
  methods=[
  _descriptor.MethodDescriptor(
    name='MakeDirectory',
    full_name='Ydb.Scheme.V1.SchemeService.MakeDirectory',
    index=0,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2._MAKEDIRECTORYREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2._MAKEDIRECTORYRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveDirectory',
    full_name='Ydb.Scheme.V1.SchemeService.RemoveDirectory',
    index=1,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2._REMOVEDIRECTORYREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2._REMOVEDIRECTORYRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListDirectory',
    full_name='Ydb.Scheme.V1.SchemeService.ListDirectory',
    index=2,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2._LISTDIRECTORYREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2._LISTDIRECTORYRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DescribePath',
    full_name='Ydb.Scheme.V1.SchemeService.DescribePath',
    index=3,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2._DESCRIBEPATHREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2._DESCRIBEPATHRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ModifyPermissions',
    full_name='Ydb.Scheme.V1.SchemeService.ModifyPermissions',
    index=4,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2._MODIFYPERMISSIONSREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2._MODIFYPERMISSIONSRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SCHEMESERVICE)

DESCRIPTOR.services_by_name['SchemeService'] = _SCHEMESERVICE

# @@protoc_insertion_point(module_scope)
