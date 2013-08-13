walkscore
=========

walk score challenge: https://github.com/walkscore/Walk-Score-Coding-Challenge


Assumptions:
- The goal is to continue to eliminate the directed graph down until there are no nodes with exactly one input and one output edge
- Remove duplicate directed edges (eg. multiple edges going from A->B)
- Loop-connected nodes (eg. A->B, B->A), with no other edges connected to the nodes, returns null
	- edge case #1: for loop-connected nodes where one of the nodes has another edge (ie. A->B, B->A, B->C), eliminate the loop (ie. return B->C)
	- edge case #2: for loop-connected nodes where both nodes have another edge (ie. A->B, B->A, B->C, D->A), keep the loop intact (ie. return A->B, B->A, B->C, D->A)


Approach:
- Read file, save nodes to two lists - edgeStartNodes and edgeEndNodes
- Traverse through each edgeStartNodes and edgeEndNodes, add to uniqueEdgeStartNodes and uniqueEdgeEndNodes if only one instance of the node
- Create list nodesToEliminate which are nodes in both uniqueEdgeStartNodes and uniqueEdgeEndNodes
- For each node in nodesToEliminate, find its edges in edgeStartNodes and edgeEndNodes:
	- if neighboring nodes are different, connect them
	- if neighboring nodes are the same, delete both edges
- Remove duplicate directed edges
