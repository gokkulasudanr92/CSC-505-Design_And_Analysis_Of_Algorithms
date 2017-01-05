import sys

input = []
for line in sys.stdin:
	input.append(line.strip())
	
first_line = input[0]
input.pop(0)

n = int(first_line.split(' ')[0])
m = int(first_line.split(' ')[1])

""" Always vertex 0 is the source and vertex 1 is the sink """

""" Initializing Capacity Matrix, FLow Passed Matrix & Adjacency list """
capacity_matrix = []
flow_passed = []
adjacency_list_with_residue = {}

for i in range(n):
	list_1, list_2 = [], []
	for j in range(n):
		list_1.append(-1)
		list_2.append(-1)
	capacity_matrix.append(list_1)
	flow_passed.append(list_2)
	adjacency_list_with_residue[i] = []

m_edges_list = []
m_edges_list = input

for line in input:
	edge_note = line.split(' ')
	i = int(edge_note[0])
	j = int(edge_note[1])
	weight = int(edge_note[2])
	capacity_matrix[i][j] = flow_passed[i][j] = weight
	flow_passed[j][i] = 0
	adjacency_list_with_residue[i].append(j)
	adjacency_list_with_residue[j].append(i)

source = 0
sink = 1
	
parent_list = {}
current_capcity = {}

def bfs(startNode, endNode):
	global parent_list
	for i in range(n):
		parent_list[i] = -1
		
	global current_capcity
	for i in range(n):
		current_capcity[i] = 0
		
	queue = []
	queue.append(startNode)
	
	parent_list[startNode] = -2
	current_capcity[startNode] = sys.maxint
	
	while len(queue) > 0:
		currentNode = queue[0]
		queue.pop(0)
		
		for to_vertex in adjacency_list_with_residue[currentNode]:
			if parent_list[to_vertex] == -1:
				flow_effective = capacity_matrix[currentNode][to_vertex] - flow_passed[to_vertex][currentNode]
				if flow_effective > 0:
					parent_list[to_vertex] = currentNode
					current_capcity[to_vertex] = current_capcity[currentNode] if current_capcity[currentNode] < flow_effective else flow_effective
					if to_vertex == endNode:
						return current_capcity[endNode]
					queue.append(to_vertex)
					
	
	return 0
	
def edmonds_karp(startNode, endNode):
	global flow_passed
	
	maxFlow = 0
	while True:
		flow = bfs(startNode, endNode)
		if flow == 0:
			break
		maxFlow += flow
		currentNode = endNode
		while currentNode != startNode:
			previousNode = parent_list[currentNode]
			flow_passed[currentNode][previousNode] += flow
			flow_passed[previousNode][currentNode] -= flow
			currentNode = previousNode
	
	return maxFlow
	
print edmonds_karp(source, sink)

for line in input:
	edge_list = line.split(' ')
	i = int(edge_list[0])
	j = int(edge_list[1])
	print i, j, flow_passed[j][i]