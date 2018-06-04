#!/usr/bin/env bash

name=$1

aws lambda update-function-code \
  --region ${AWS_REGION:-us-east-1} \
  --function-name ${name}-pdf \
  --s3-bucket ${BUCKET_NAME} \
  --s3-key ${BUCKET_PATH}/lambda_function.zip \
  --publish

aws lambda update-function-code \
  --region ${AWS_REGION:-us-east-1} \
  --function-name ${name}-png \
  --s3-bucket ${BUCKET_NAME} \
  --s3-key ${BUCKET_PATH}/lambda_function.zip \
  --publish
