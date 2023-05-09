# Graph

Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

### add node
•	Arguments: value
•	Returns: The added node
•	Add a node to the graph
### add edge
•	Arguments: 2 nodes to be connected by the edge, weight (optional)
•	Returns: nothing
•	Adds a new edge between two nodes in the graph
•	If specified, assign a weight to the edge
•	Both nodes should already be in the Graph
### get nodes
•	Arguments: none
•	Returns all of the nodes in the graph as a collection (set, list, or similar)
•	Empty collection returned if there are no nodes
### get neighbors
•	Arguments: node
•	Returns a collection of edges connected to the given node
•	Include the weight of the connection in the returned collection
•	Empty collection returned if there are no nodes
### size
•	Arguments: none
•	Returns the total number of nodes in the graph
•	0 if there are none
### breadth_first
•	Arguments: node
•	Returns the list of
•	0 if there are none


## Whiteboard Process

![Breadth First Whiteboard image](whiteboard36.png)

[Whiteboard link](https://www.figma.com/file/TYHQxAoEjAQwJQYiZTyL1u/Code-Challenge-36?type=whiteboard&node-id=0%3A1&t=bgCOlAKUYlIItFMs-1)

## Approach & Efficiency

Use a dict to store the adjacency list, with node as key and value as a list of edges.  Dicts are fash look-up.

Breadth-first:
- Create output_list variable to hold vertexes visited
- Create queue to do breadth-first traversal
- Add root node to the queue
- While queue is not empty:
- dequeue and save to current
- If not in output_list
- add current to output_list
- Add current’s edges to queue
- Convert from vertex to names
- Return names

Time: O(n) because we go through all the connected nodes

Space: O(n) because we have a list and a queue with all the connected nodes

## Solution

[Link to code](https://github.com/mikeshen7/data-structures-and-algorithms/blob/main/python/data_structures/graph.py)

To run file, from python directory:

python -m data_structures.graph

To test, from python directory:

pytest
