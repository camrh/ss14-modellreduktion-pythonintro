#!/usr/bin/python

import time

def report_letter(c):
  print(chr(ord('z') - c))

count = 10
#! results in a en endless loop. why?
while count > 0:
    count-=1
    report_letter(count)

print("hallo")