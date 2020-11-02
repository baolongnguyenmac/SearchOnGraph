import pygame
import graphUI
import math
from node_color import white, yellow, black, red, blue, purple, orange, green

"""
Feel free print graph, edges to console to get more understand input.
Do not change input parameters
Create new function/file if necessary
"""
def heapifyDown(heap, pos):
    while pos < len(heap):
        min = pos
        left = 2*pos + 1
        right = 2*pos + 2

        if right >= len(heap):
            if left >= len(heap):
                return
            else:
                min = left
        else:
            if heap[left][1] < heap[right][1]:
                min = left
            else:
                min = right

        if heap[min][1] < heap[pos][1]:
            heap[pos], heap[min] = heap[min], heap[pos]
            pos = min
        else:
            break


def pop(heap):
    # print(heap)
    rs = None
    if len(heap) > 0:
        rs = heap[0]
        if len(heap) > 1:
            heap[0] = heap.pop()
            heapifyDown(heap, 0)
        else:
            heap.pop()
    return rs


def push(heap, item):
    heap.append(item)
    heapifyUp(heap, len(heap) - 1)


def heapifyUp(heap, pos):
    while pos > 0:
        parent = (pos - 1) // 2
        if heap[pos][1] < heap[parent][1]:
            heap[pos], heap[parent] = heap[parent], heap[pos]
            pos = parent
        else:
            break


def getH(node1, node2):
    return math.sqrt((node1[0][0] - node2[0][0])**2 + (node1[0][1] - node2[0][1])**2)


def printPath(graph, edges, edge_id, parent, goal):
    """
    tô màu cam cho start
    tô màu tím cho goal 
    tô màu xanh cho đường đi
    """
    graph[goal][3] = purple
    graphUI.updateUI()
    sumCost = 0
    while True:
        if parent[goal] == -1:
            graph[goal][3] = orange
            graphUI.updateUI()
            print(goal, end=' ')
            break
        else:
            edges[edge_id(goal, parent[goal])][1] = green
            graphUI.updateUI()
            print(goal, end=' ')
            goal = parent[goal]
            sumCost += getH(graph[goal], graph[parent[goal]])
    print('sum cost: ', sumCost)


def setNodeColor(node, color):
    node[3] = color
    graphUI.updateUI()
    pygame.time.delay(400)


def setEdgeColor(edges, edge_id, node1, node2, color):
    edges[edge_id(node1, node2)][1] = color
    graphUI.updateUI()
    pygame.time.delay(400)


def BFS(graph, edges, edge_id, start, goal):
    """
    BFS search
    """
    # TODO: your code
    print("Implement BFS algorithm.")
    pass


def DFS(graph, edges, edge_id, start, goal):
    """
    DFS search
    """
    print("Implement DFS algorithm.")
    pass

def UCS(graph, edges, edge_id, start, goal):
    """
    Uniform Cost Search search
    """
    # TODO: your code
    print("Implement Uniform Cost Search algorithm.")

    parent = [-1] * len(graph)
    cost = [1000] * len(graph)
    cost[start] = 0
    heap = [(start, 0)]
    setNodeColor(graph[start], red)

    while True:
        if len(heap) == 0:
            print('k tim thay duong di')
            return

        current = pop(heap)
        setNodeColor(graph[current[0]], yellow)
        if current[0] == goal:
            printPath(graph, edges, edge_id, parent, goal)
            return

        currentNode = graph[current[0]]
        for adjNum in currentNode[1]:
            c = cost[current[0]] + getH(graph[current[0]], graph[adjNum])
            if graph[adjNum][3] == black or (graph[adjNum][3] == red and cost[adjNum] > c):
                setEdgeColor(edges, edge_id, adjNum, current[0], white)
                setNodeColor(graph[adjNum], red)

                cost[adjNum] = c
                parent[adjNum] = current[0]
                push(heap, (adjNum, c))
        setNodeColor(graph[current[0]], blue)

def AStar(graph, edges, edge_id, start, goal):
    """
    A star search
    """
    # TODO: your code
    print("Implement A* algorithm.")

    parent = [-1] * len(graph)
    cost = [1000] * len(graph)
    cost[start] = 0
    heap = [(start, getH(graph[start], graph[goal]))]
    setNodeColor(graph[start], red)

    while True:
        if len(heap) == 0:
            print('k tim thay duong di')
            return

        current = pop(heap)
        # print('curr = ', current)
        # print('heap = ', heap)
        print()
        setNodeColor(graph[current[0]], yellow)
        if current[0] == goal:
            printPath(graph, edges, edge_id, parent, goal)
            return

        currentNode = graph[current[0]]
        for adjNum in currentNode[1]:
            c = cost[current[0]] + getH(graph[current[0]], graph[adjNum])
            if graph[adjNum][3] == black or (graph[adjNum][3] == red and cost[adjNum] > c):
                setEdgeColor(edges, edge_id, adjNum, current[0], white)
                setNodeColor(graph[adjNum], red)

                cost[adjNum] = c
                parent[adjNum] = current[0]
                push(heap, (adjNum, c + getH(graph[adjNum], graph[goal])))
        setNodeColor(graph[current[0]], blue)


def example_func(graph, edges, edge_id, start, goal):
    """
    This function is just show some basic feature that you can use your project.
    @param graph: list - contain information of graph (same value as global_graph)
                    list of object:
                        [0] : (x,y) coordinate in UI
                        [1] : adjacent node indexes
                        [2] : node edge color
                        [3] : node fill color
                Ex: graph = [
                                [
                                    (139, 140),             # position of node when draw on UI
                                    [1, 2],                 # list of adjacent node
                                    (100, 100, 100),        # grey - node edged color
                                    (0, 0, 0)               # black - node fill color
                                ],
                                [(312, 224), [0, 4, 2, 3], (100, 100, 100), (0, 0, 0)],
                                ...
                            ]
                It means this graph has Node 0 links to Node 1 and Node 2.
                Node 1 links to Node 0,2,3 and 4.
    @param edges: dict - dictionary of edge_id: [(n1,n2), color]. Ex: edges[edge_id(0,1)] = [(0,1), (0,0,0)] : set color
                    of edge from Node 0 to Node 1 is black.
    @param edge_id: id of each edge between two nodes. Ex: edge_id(0, 1) : id edge of two Node 0 and Node 1
    @param start: int - start vertices/node
    @param goal: int - vertices/node to search
    @return:
    """

    # Ex1: Set all edge from Node 1 to Adjacency node of Node 1 is green edges.
    node_1 = graph[1]
    for adjacency_node in node_1[1]:
        edges[edge_id(1, adjacency_node)][1] = green
    graphUI.updateUI()

    # Ex2: Set color of Node 2 is Red
    graph[2][3] = red
    graphUI.updateUI()

    # Ex3: Set all edge between node in a array.
    path = [4, 7, 9]  # -> set edge from 4-7, 7-9 is blue
    for i in range(len(path) - 1):
        edges[edge_id(path[i], path[i + 1])][1] = blue
    graphUI.updateUI()
