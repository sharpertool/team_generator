#!/bin/bash

builddir=$1
rsync -av --delete --exclude=docs --exclude=samples --exclude=tests --exclude=rpm --exclude=src /var/lang/lib/node_modules/casperjs /${builddir}/node_modules
#rsync -av --delete \
#    --exclude=test --exclude lib/phantom/examples \
#    /var/lang/lib/node_modules/phantomjs-prebuilt /${builddir}/node_modules


