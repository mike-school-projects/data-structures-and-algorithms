# Code Challenge 37 Graph Business Trip

Write a function called business trip
- Arguments: graph, array of city names
- Return: the cost of the trip (if it’s possible) or None (if not)
- Determine whether the trip is possible with direct flights, and how much it would cost.

## Whiteboard Process
![Whiteboard image](whiteboard37.png)

[Whiteboard link](https://www.figma.com/file/BRZdIM6bloibjbQ0WmwVwa/Code-Challenge-37?type=whiteboard&node-id=0%3A1&t=qR3c06Zudah3XRJv-1)

## Approach & Efficiency

- Create temp variables for total_cost
- Loop through itinerary_list, starting at 0, ending at 2nd from end:
- Set start location name and end location name
- Find the vertex corresponding to those names
- Find the edges from the start location
- Loop through edges:
- If end location found, add to total_cost
- If not found, return None
- Return total_cost

Time: O(n*n) because we have to loop through each location, and for each location we have to loop through all the edges

Space: O(1) because we’re only using a few static variables, no data structures


## Solution

[Link to code](https://github.com/mikeshen7/data-structures-and-algorithms/blob/main/python/code_challenges/graph_business_trip.py)

To run file, from python directory:

python -m code_challenges.graph_business_trip

To test, from python directory:

pytest


