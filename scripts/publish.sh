#!/usr/bin/env bash

zipfile=lambda_function.zip
bucket=sharpertool.lambda.deploy
stage=test

# Parse options
# -p <profile>
# -f <function name>: required
# -c -- set to true to compile first.
compile="false"
profile=sharpertool
export AWS_DEFAULT_REGION=us-west-2
while getopts p:f:s:c option
do
	case "${option}" in
		p) profile=${OPTARG};;
		f) function=${OPTARG};;
		s) stage=${OPTARG} ;;
		c) compile="true"
	esac
done

echo "Deployment stage is ${stage}"

# This gets the first param, uses as profile name
# and the 2nd param as function name
#profile=$1
#function=$2

if [ "true" == ${compile} ]
then
	`dirname $0`/compile.sh
fi

if [ -z ${function} ]
then
	echo "Must specify a function prefix with: -f <function>"
	exit 2
fi
bucket_key=${function}

echo "Transfer to S3  >>>"
ls -lh $zipfile
time aws s3 --profile $profile --region us-east-1 \
        cp ${zipfile} s3://${bucket}/${bucket_key}/${stage}/
echo "Transfer done."

echo "Updating Lambda functions"
time aws lambda --profile ${profile} update-function-code \
    --function-name ${function} \
    --s3-bucket ${bucket} \
    --s3-key ${bucket_key}/${stage}/${zipfile} \
    --publish


