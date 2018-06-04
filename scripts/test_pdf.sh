#!/usr/bin/env bash

mypath=$(dirname $0)

url="https://bwo31pmgwb.execute-api.us-east-1.amazonaws.com/test/export/pdf?show_input"
headers="Content-Type: text/json; charset=utf-8"

cmd="curl -X POST ${url} -H ${headers} -d @${mypath}/post_body.json"

if [ -x "$(command -v jq)" ];then
    echo "You have jq installed, pipe output through it"
    ${cmd} | jq
else
    echo "Install jq for better output: https://stedolan.github.io/jq/"
    ${cmd}
fi



