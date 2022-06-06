#!/bin/bash
set -x
find . -type f -exec sed -i 's/\t/    /g' {} +

//replace a reg expression pattern 
find . -name "*.cpp" -type f -exec sed -i  's/TRACE_DEBUG(\([^;]*\));/ Log::debug("appId2")<<\1;/g' {} +
sleep 1
find . -name "*.cpp" -type f -print0 | xargs -0 perl -pi -e 's/ +$//'

//find underscore followed lowercase alphabet  _a
grep -Enr "_[a-z]" dir/ | grep -v  "memset_s\|uint[1-9]*_t\|memcpy_s\|size_t\|include\|g_\|.h" | grep -E "_[a-z]"


//一把改名字
find .  -type f -exec rename 's/\u8fed\u4ee3\u4e00/\u8fed\u4ee3\u4e8c/'  {} +
