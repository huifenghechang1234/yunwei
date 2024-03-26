
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess


#
#variable 'out' is subprocess output inf
cmd = "ping www.baidu.com -c 4"
cmd_list = cmd.split(' ')
p = subprocess.Popen(cmd_list,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
while p.poll() is None:
    line = p.stdout.readline().decode('utf8').strip()
    print(line)

#output info get from console has many unicode escape character ,such as \x1b(B\x1b[m\x1b[39;49m\x1b[K\n\x1b(B\x1b[m
#use decode('unicode-escape') to process
