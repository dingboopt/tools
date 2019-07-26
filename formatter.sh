#!/bin/bash
set -x
find . -type f -exec sed -i 's/\t/    /g' {} +

//replace a reg expression pattern 
find . -type f -exec sed -i  's/TRACE_DEBUG(\([^;]*\));/ Log::debug("appId2")<<\1;/g' {} +
sleep 1
find . -type f -print0 | xargs -0 perl -pi -e 's/ +$//'
