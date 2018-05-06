#!/usr/bin/env python

import sys

def print_usage():
  print "Usage:"
  print "  topN.py <file> <num_results>"

# Implementation of insertion sort in python.
# By FAR the slowest way tried.
def insertionSort(results):
  for index in range(1,len(results)):
    currentvalue = results[index]
    position     = index

    while position > 0 and results[position - 1] > currentvalue:
         results[position] = results[position - 1]
         position = position - 1

    results[position] = currentvalue

# Sort the results table on every iteration 
# This ensures that the results table always has 
# The smallest value first
def sortList(results):
  results.sort()

results     = []

try:
  src_file    = sys.argv[1]
  num_results = int(sys.argv[2])

except:
  print_usage()
  sys.exit(1)

with open(src_file) as f:
  for line in f:
    if len(results) < num_results:
      results.insert(1, int(line))
      sortList(results)
 
    elif line > results[0]:
      results.insert(1, int(line))
      sortList(results)
      results.pop(0)

    else:
      continue

for num in results:
  print num 
