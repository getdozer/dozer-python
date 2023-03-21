#!/bin/bash

BASEDIR=$(dirname "$0")
cd ${BASEDIR}/../

PROTO_DEST=./pydozer

mkdir -p ${PROTO_DEST}


python -m grpc_tools.protoc --experimental_allow_proto3_optional -I protos/ --python_out=${PROTO_DEST} \
         --grpc_python_out=${PROTO_DEST} protos/*.proto