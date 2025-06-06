# 🔍Algorithm Design - Shortest Path Algorithm

## Description

I implemented a shortest path algorithm in this project using core Python concepts such as functions, loops, conditionals, and dictionary comprehensions.

The goal was to find the shortest distance between a starting node and all other nodes in a graph. This algorithm is foundational in computer science and has real-world applications in GPS systems, network routing, and game AI.

## 🧠 What I Learned

- How to represent a graph using dictionaries and lists in Python.
- The use of dictionary comprehensions to initialize tracking structures like distances and paths.
- How to apply a greedy approach to iteratively find the shortest paths by updating distances.
- The importance of tracking visited and unvisited nodes to ensure optimal path selection.

## 🗺️ How It Works

- The graph is represented as a dictionary where each node maps to a list of tuples containing neighboring nodes and edge weights.
- The `shortest_path()` function calculates the shortest path from a given starting node to all others (or a specified target).
- The algorithm updates the shortest known distance and path for each node until all nodes have been visited.

## 🧪 Example Output

Calling the function with the following:

```python
shortest_path(my_graph, 'A')
```
Produces:
```
A-B distance: 4
Path: A -> C -> B

A-C distance: 3
Path: A -> C

A-D distance: 4
Path: A -> C -> D

A-E distance: 8
Path: A -> C -> E

A-F distance: 6
Path: A -> C -> B -> F
```
This output shows the shortest distance from node 'A' to every other node in the graph, along with the path taken.

## 🎓 Credits
This project is part of the "Learn Algorithm Design by Building a Shortest Path Algorithm" course by 
**[freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/)**.  
