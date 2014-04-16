#!/usr/bin/python

from pprint import pprint
import traceback
import collections as cl
import pickle

data = {'A': [1, 'kl'], 'B': [1]}
try:
  data['C'].append(2)
except KeyError, e:
  print("blubb")
  #traceback.print_exc()

try:
  d_data = cl.defaultdict(set)
  d_data.update(data)
  #d_data.
except KeyError, e:
  pprint("error")
pprint(d_data)
#! a datastructure from the collections module allows the append operation
#d_data = ???
#d_data.update(data)
#d_data['C'].append(2)
#pprint(d_data)

