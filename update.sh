#!/usr/bin/expect -f
# Expect script to supply root/admin password for remote ssh server 
# and execute command.
# This script needs three argument to(s) connect to remote server:
# user = Username of remote unix server
# password = Password of remote UNIX server, for determined user above
# ipaddr = IP Address of remote UNIX server, no hostname
# For example:
#  ./sshlogin.exp user password 192.168.1.11
# ------------------------------------------------------------------------
# Copyright (c) 2004 nixCraft project <http://cyberciti.biz/fb/>
# This script is licensed under GNU GPL version 2.0 or above
# -------------------------------------------------------------------------
# This script is part of nixCraft shell script collection (NSSC)
# Visit http://bash.cyberciti.biz/ for more information.
# ----------------------------------------------------------------------
# set Variables
set user [lrange $argv 0 0] 
set password [lrange $argv 1 1]   
set ipaddr [lrange $argv 2 2] 
set arg1 [lrange $argv 3 3] 
set timeout -1   
# now connect to remote UNIX box (ipaddr) with given script to execute
#spawn ssh root@$ipaddr $scriptname $arg1
#spawn ssh root@$ipaddr $scriptname 
spawn ssh $user@$ipaddr
match_max 100000
# Look for passwod prompt
expect "yes/no" { 
    send "yes\r"
    expect "*?assword" { send "[lindex $password]\r" }
    } "*?assword" { send "[lindex $password]\r" }
# Send password aka $password 
#send -- "$password\r"
expect "#"
#expect ": " { send "touch ya.txt\r" }
send -- "bash ./update.sh\r"
#send "bash ./update.sh\r"
# send blank line (\r) to make sure we get back to gui
send -- "exit\r"
expect eof
