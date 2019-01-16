#!/bin/bash
set -x
find . -type f -exec sed -i 's/\t/    /g' {} +
sleep 1
find . -type f -print0 | xargs -0 perl -pi -e 's/ +$//'
