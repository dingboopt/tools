#!/usr/bin/expect
#set timeout 20 #
set user [lindex $argv 0];
set passwd [lindex $argv 0];
spawn git submodule update --init --recursive
expect "*Username*"
send "$user\r"
expect "Passwd*"
send "$passwd\r"
expect "*Username*"
send "$user\r"
expect "Passwd*"
send "$passwd\r"
expect "*Username*"
send "$user\r"
expect "Passwd*"
send "$passwd\r"
expect "*Username*"
send "$user\r"
expect "Passwd*"
send "$passwd\r"
expect "*Username*"
send "$user\r"
expect "Passwd*"
send "$passwd\r"
interact
