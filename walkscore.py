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

couldHaveDuplicateEdges = True
while couldHaveDuplicateEdges:
	uniqueEdgeStartNodes = [k for k,v in Counter(edgeStartNodes).items() if v==1]
	uniqueEdgeEndNodes = [k for k,v in Counter(edgeEndNodes).items() if v==1]

	nodesToEliminate = set(uniqueEdgeStartNodes).intersection(uniqueEdgeEndNodes)

	for node in nodesToEliminate:
		try:
			isStartNodeIndex = edgeStartNodes.index(node)
			isEndNodeIndex = edgeEndNodes.index(node)
		except ValueError: # this can happen in loop case where a node is already popped out of edge Start/End Nodes list
	   		continue

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

	# find duplicate edges
	allEdges = zip(edgeStartNodes, edgeEndNodes)
	allEdgesAfterRemovingDuplicates = list(set(allEdges))
	if len(allEdges) == len(allEdgesAfterRemovingDuplicates): # there are no duplicates
		couldHaveDuplicateEdges = False
	else:
		unzippedEdges = zip(*allEdgesAfterRemovingDuplicates)
		edgeStartNodes = list(unzippedEdges[0])
		edgeEndNodes = list(unzippedEdges[1])

# write to file
writefilename = 'output.txt'
wf = open(writefilename, 'w')
for i in range(len(edgeStartNodes)):
	line = edgeStartNodes[i] + '\t' + edgeEndNodes[i]
	print line
	wf.write(line + '\n')
print 'Output written to ' + writefilename


