# 4.1 Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes. 

import Queue

class Graph():

    def __init__(self):
        self.max_vertices = 6
        self.vertices = [0] * self.max_vertices
        self.count = 0
    
    def addNode(self, x):
        if self.count < self.max_vertices:
            self.vertices[self.count] = x
            self.count += 1
        else:
            print "Graph full"
    
    def getNodes(self):
        return self.vertices

class Node():

    def __init__(self, vertex, adjacentLength):
        self.adjacent = [0] * adjacentLength
        self.vertex = vertex
        self.adjacentCount = 0
        self.visited = False

    def addAdjacent(self, x):
        if self.adjacentCount < len(self.adjacent):
            self.adjacent[self.adjacentCount] = x
            self.adjacentCount += 1
        else:
            print "No more adjacent nodes can be added"
    
    def getAdjacent(self):
        return self.adjacent

    def getVertex(self):
        return self.vertext

def breadthFirstSearch(graph, start, end):
    if start == end:
        return True

    q = Queue.Queue(len(g.getNodes()))
    start.visited = True
    q.put(start)

    while not q.empty():
        r = q.get()
        if r != None:
            adjacent = r.getAdjacent()
            for i in range(len(adjacent)):
                if adjacent[i].visited == False:
                    if adjacent[i] == end:
                        return True
                    else:
                        q.put(adjacent[i])
                    adjacent[i].visited = True

    return False
