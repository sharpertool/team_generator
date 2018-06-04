#!/usr/bin/env bash
# Script to build the project in a separate directory so we can insure that ONLY production files are built.
# We also assemble all that is needed for the deploy package
# Use zip to create a zipfile for the deploy package.

builddir=build

rm -rf ${builddir}
mkdir -p ${builddir}

rsync -av src/ ${builddir}

# We need to run from the top level dir
cd `dirname $0`/..

echo "Working dir: $PWD"

zipfile=lambda_function.zip

# CI will use a different step for the zip build, just to be clearer on the CI steps.
if [ "${CI}" != "true" ];then
    # Must be in the build directory to properly build the zip file
    echo "Build the zip file"
    pushd ${builddir}
    zip -r -u ../${zipfile} ./
    popd
fi





