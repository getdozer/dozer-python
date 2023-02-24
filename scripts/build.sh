#!/bin/bash

BASEDIR=$(dirname "$0")
cd ${BASEDIR}/../

PROTO_DEST=./dozer/generated

mkdir -p ${PROTO_DEST}
mkdir -p ${PROTO_DEST}/api
mkdir -p ${PROTO_DEST}/ingest


python -m grpc_tools.protoc --experimental_allow_proto3_optional -I protos/ --python_out=${PROTO_DEST} \
         --grpc_python_out=${PROTO_DEST} protos/*.proto

python -m grpc_tools.protoc --experimental_allow_proto3_optional -I protos/ingest --python_out=${PROTO_DEST}/ingest \
         --grpc_python_out=${PROTO_DEST}/ingest protos/ingest/*.proto         

python -m grpc_tools.protoc --experimental_allow_proto3_optional -I protos/api --python_out=${PROTO_DEST}/api \
         --grpc_python_out=${PROTO_DEST}/api protos/api/*.proto         