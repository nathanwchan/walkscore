#!/usr/bin/python

import sys

filename = sys.argv[1]

try:
   with open(filename): pass
except IOError:
   print 'Invalid file!'
   sys.exit(0)

f = open(filename, 'r')

edgeStartNodes = []
edgeEndNodes = []
for line in f:
	nodes = line.split('\t')
	if len(nodes) != 2:
		print 'Invalid line in file: ' + line
   		sys.exit(0)
   	edgeStartNodes.append(nodes[0])
   	edgeEndNodes.append(nodes[1].rstrip('\n'))

print 'edgeStartNodes: ' + str(edgeStartNodes)
print 'edgeEndNodes: ' + str(edgeEndNodes)
