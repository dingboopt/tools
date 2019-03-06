#!/usr/bin/expect
set timeout 200
set user [lindex $argv 0];
set passwd [lindex $argv 1];
spawn git submodule update --init --recursive
expect "*Username*"
send "$user\r"
expect "Password*"
send "$passwd\r"
expect "*Username*"
send "$user\r"
expect "Password*"
send "$passwd\r"
expect "*Username*"
send "$user\r"
expect "Password*"
send "$passwd\r"
expect "*Username*"
send "$user\r"
expect "Password*"
send "$passwd\r"
expect "*Username*"
send "$user\r"
expect "Password*"
send "$passwd\r"
interact
