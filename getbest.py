#!/usr/bin/env python3

import sys

def getCols(f):
    ''' Identify the columns that contain the marks and student numbers '''
    headings = f.readline().strip().split(",")
    i=0 #bug 1: this started from 1 while computers run starting at index 0#
    for head in headings:
        if head == "Student Number": num_col=i
        elif head == "Mark" : mark_col = i
        i+= 1 #counter was never incremented#
    return (num_col, mark_col)

def findTop(f,num_col, mark_col):
    ''' finds the top student in the class '''
    best = best_idx =  0
    for line in f:
        data = line.strip().split(",")
        mark = int(data[mark_col])
        if mark > best:
            best=mark
            best_idx+= 1 #bug 2counter was never incremented#
    return best_idx, best

if __name__ == "__main__":#added to run unit tests#
  f = open(sys.argv[1])
  num_col, mark_col = getCols(f)
  best_idx, best = findTop(f,num_col,mark_col)
  print("The top student was student %s with %d"%(best_idx,best))