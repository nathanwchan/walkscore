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

couldHaveDuplicateEdges = True
while couldHaveDuplicateEdges:
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
		except ValueError: # this can happen in loop case where a node is already popped out of edge Start/End Nodes list
	   		continue

		print 'isStartNodeIndex: ' + str(isStartNodeIndex) + ' ' + edgeStartNodes[isStartNodeIndex] + ' ' + edgeEndNodes[isStartNodeIndex]
		print 'isEndNodeIndex: ' + str(isEndNodeIndex) + ' ' + edgeStartNodes[isEndNodeIndex] + ' ' + edgeEndNodes[isEndNodeIndex]

		if edgeStartNodes[isEndNodeIndex] != edgeEndNodes[isStartNodeIndex]: # non-loop case
			edgeEndNodes[isEndNodeIndex] = edgeEndNodes[isStartNodeIndex]
			edgeStartNodes.pop(isStartNodeIndex)
			edgeEndNodes.pop(isStartNodeIndex)
		else: # loop case
			if isStartNodeIndex > isEndNodeIndex: # need to pop larger index first, otherwise could get index out of range
				edgeStartNodes.pop(isStartNodeIndex)
				edgeEndNodes.pop(isStartNodeIndex)
				edgeStartNodes.pop(isEndNodeIndex)
				edgeEndNodes.pop(isEndNodeIndex)
			else:
				edgeStartNodes.pop(isEndNodeIndex)
				edgeEndNodes.pop(isEndNodeIndex)
				edgeStartNodes.pop(isStartNodeIndex)
				edgeEndNodes.pop(isStartNodeIndex)

	print 'edgeStartNodes: ' + str(edgeStartNodes)
	print 'edgeEndNodes: ' + str(edgeEndNodes)

	# find duplicate edges
	allEdges = zip(edgeStartNodes, edgeEndNodes)
	allEdgesAfterRemovingDuplicates = list(set(allEdges))
	print 'allEdges: ' + str(allEdges)
	print 'allEdgesAfterRemovingDuplicates: ' + str(allEdgesAfterRemovingDuplicates)
	if len(allEdges) == len(allEdgesAfterRemovingDuplicates): # there are no duplicates
		couldHaveDuplicateEdges = False
	else:
		unzippedEdges = zip(*allEdgesAfterRemovingDuplicates)
		edgeStartNodes = list(unzippedEdges[0])
		edgeEndNodes = list(unzippedEdges[1])

print 'FINAL edgeStartNodes: ' + str(edgeStartNodes)
print 'FINAL edgeEndNodes: ' + str(edgeEndNodes)

