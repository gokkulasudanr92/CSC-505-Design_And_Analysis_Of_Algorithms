import sys
import collections

result = []

input = []
""" 0 -> white, 1-> gray, 2->black """
color_dict = {}
color_dict = collections.OrderedDict()
vertices_dict = []

""" Function to sort a list based on the index """
def order(givenlist):
    return lambda a,b: cmp(givenlist.index(a), givenlist.index(b))

""" Read input from a file """
for line in sys.stdin:
    line = line.split('\n')
    input.append(line[0])
no_of_vertices = int(input[0])
input.pop(0)

adj_list, graph_rev_adj_list = {}, {}
adj_list = collections.OrderedDict()
graph_rev_adj_list = collections.OrderedDict()

for i in range(no_of_vertices):
	adj_list[input[i]] = []
	graph_rev_adj_list[input[i]] = []
	vertices_dict.append(input[i])
	
""" Initialize finsh time for all the vertices """
finish_time_dict = {}
for key in vertices_dict:
	finish_time_dict[key] = 0

dependencies = int(input[no_of_vertices])

dependency_input = []
for i in range(dependencies):
	current_line = input[no_of_vertices + i + 1]
	dependency_input.append(current_line.split(' '))

for i in range(dependencies):
	if dependency_input[i][1] in adj_list:
		adj_list[dependency_input[i][1]].append(dependency_input[i][0])

def dfs_with_dict(adj_list, vertices_dict, color_dict):
	""" Global timer to record node visit """
	global time_dict
	
	""" Mark all the vertices white """
	for v in vertices_dict:
		color_dict[v] = 0;
	
	time_dict = 0
	for key in color_dict:
		if color_dict[key] == 0:
			dfs_visit_with_dict(adj_list, key, color_dict)
		
def dfs_visit_with_dict(adj_list, vertex, color_dict):
	""" Global timer to record node visit """
	global time_dict
	time_dict = time_dict + 1
	
	""" The vertex is visited """
	color_dict[vertex] = 1
	for next_vertex in adj_list[vertex]:
		if color_dict[next_vertex] == 0:
			dfs_visit_with_dict(adj_list, next_vertex, color_dict)
	""" Update the vertex color to black """
	color_dict[vertex] = 2
	time_dict = time_dict + 1
	finish_time_dict[vertex] = time_dict
		
def reverse_dict(graph_rev_adj_list, dependency_input, dependencies):
	for i in range(dependencies):
		if dependency_input[i][0] in graph_rev_adj_list:
			graph_rev_adj_list[dependency_input[i][0]].append(dependency_input[i][1])

def dfs_reverse_dict(result, graph_rev_adj_list, no_of_vertices, vertices, color_dict, finish_time_dict):
	""" Coloring all vertices white again """
	for vertex in vertices:
		color_dict[vertex] = 0
	
	i = 0
	count = 0
	while i < no_of_vertices and count < no_of_vertices:
		check_vertex = None
		scc = []
		
		finish_order = sorted(finish_time_dict.values(), reverse = True)
		max = finish_order[0]
		
		for vertex in finish_time_dict:
			if finish_time_dict[vertex] == max:
				check_vertex = vertex
		
		if not check_vertex is None:
			if color_dict[check_vertex] == 0:
				dfs_visit_reverse_with_dict(graph_rev_adj_list, check_vertex, scc, color_dict)
				finish_time_dict[check_vertex] = 0
			
				if (len(scc) > 1):
					scc.sort(order(vertices))
					result.append(scc)
			else:
				finish_time_dict[check_vertex] = 0
			i += 1
		count += 1
				
def dfs_visit_reverse_with_dict(graph_rev_adj_list, check_vertex, scc, color_dict):
	""" Color the vertex grap """
	color_dict[check_vertex] = 1
	
	for elem in graph_rev_adj_list[check_vertex]:
		if color_dict[elem] == 0:
			dfs_visit_reverse_with_dict(graph_rev_adj_list, elem, scc, color_dict)
	
	""" Update the color of the list to black """
	color_dict[check_vertex] = 2
	scc.append(check_vertex)
			
def print_scc_dict(result, vertices_dict, no_of_vertices):
	i = 0
	curr = zip(*result)
	while i < no_of_vertices:
		for scc_v in curr[0]:
			if vertices_dict[i] == scc_v:
				print " ".join(result[curr[0].index(scc_v)])
		i += 1
                
""" Perform Topological Sort """
dfs_with_dict(adj_list, vertices_dict, color_dict)

""" Reverse Order """
reverse_dict(graph_rev_adj_list, dependency_input, dependencies)

""" Perform DFS based on last finish time """
dfs_reverse_dict(result, graph_rev_adj_list, no_of_vertices, vertices_dict, color_dict, finish_time_dict)

""" Ouputting the strongly connecte dcomponents """
print_scc_dict(result, vertices_dict, no_of_vertices)