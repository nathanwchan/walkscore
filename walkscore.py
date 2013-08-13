#!/usr/bin/python

import sys
from collections import Counter

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

uniqueEdgeStartNodes = [k for k,v in Counter(edgeStartNodes).items() if v==1]
uniqueEdgeEndNodes = [k for k,v in Counter(edgeEndNodes).items() if v==1]

print 'uniqueEdgeStartNodes: ' + str(uniqueEdgeStartNodes)
print 'uniqueEdgeEndNodes: ' + str(uniqueEdgeEndNodes)

nodesToEliminate = set(uniqueEdgeStartNodes).intersection(uniqueEdgeEndNodes)

print 'nodesToEliminate: ' + str(nodesToEliminate)

for node in nodesToEliminate:
	try:
		isStartNodeIndex = edgeStartNodes.index(node)
		isEndNodeIndex = edgeEndNodes.index(node)
	except ValueError as e:
   		print 'Error: ' + str(e)
   		sys.exit(0)

	print 'isStartNodeIndex: ' + str(isStartNodeIndex) + ' ' + edgeStartNodes[isStartNodeIndex] + ' ' + edgeEndNodes[isStartNodeIndex]
	print 'isEndNodeIndex: ' + str(isEndNodeIndex) + ' ' + edgeStartNodes[isEndNodeIndex] + ' ' + edgeEndNodes[isEndNodeIndex]
	
	if edgeStartNodes[isEndNodeIndex] != edgeEndNodes[isStartNodeIndex]:
		edgeEndNodes[isEndNodeIndex] = edgeEndNodes[isStartNodeIndex]
		edgeStartNodes.pop(isStartNodeIndex)
		edgeEndNodes.pop(isStartNodeIndex)

	print 'edgeStartNodes: ' + str(edgeStartNodes)
	print 'edgeEndNodes: ' + str(edgeEndNodes)

