#!/bin/bash
kill -9 `ps axu | grep qemu |grep system-aarch64 |awk '{print $2}'`
