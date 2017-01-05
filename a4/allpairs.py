import sys

def print_path(path_list, result, vertices, source, destination):
	k = result[source][destination].getPartition()
	
	if k == -1:
		return
		
	print_path(path_list, result, vertices, source, k)
	path_list.append(vertices[k])
	print_path(path_list, result, vertices, k, destination)
		
def match_strings(s1, s2):
	pos = -1
	
	for i, (c1, c2) in enumerate(zip(s1, s2)):
		if c1 != c2:
			if pos != -1:
				return -1
			else:
				pos = i
				
	return pos

class partition(object):
	def __init__(self, distance, k):
		self.distance = distance
		self.k = k
		
	def setDistance(self, distance):
		self.distance = distance
		
	def getDistance(self):
		return self.distance
		
	def setPartition(self, k):
		self.k = k
		
	def getPartition(self):
		return self.k

input = []
for line in sys.stdin:
	input.append(line.strip())
	
n = int(input[0])
input.pop(0)

vertices = []
for i in range(n):
	vertices.append(input[0])
	input.pop(0)
	
m = int(input[0])
input.pop(0)

list_of_queries = []

for i in range(m):
	list_of_queries.append(input[0])
	input.pop(0)
	
# Let us construct the adjacency matrix
adj_matrix = []

""" Initialization of the representation """
for i in range(n):
	new_list = []
	for j in range(n):
		value = partition(sys.maxint, -1)
		new_list.append(value)
	adj_matrix.append(new_list)

""" Updating the values of the index based on the conditions """
for i in range(n):
	s1 = vertices[i]
	for j in range(n):
		if i != j:
			s2 = vertices[j]
			if len(s1) != len(s2):
				pass
			else:
				position = match_strings(s1, s2)
				if position != -1:
					weight = ord(s1[position]) - ord(s2[position])
					weight = weight if weight > 0 else -1 * weight
					adj_matrix[i][j].setDistance(weight)
					adj_matrix[i][j].setPartition(-1)
		else:
			adj_matrix[i][j].setDistance(0)
			adj_matrix[i][j].setPartition(-1)
				
res = adj_matrix

""" Applying Floyd Warshall Algorithm """
for k in range(n):
	for i in range(n):
		for j in range(n):
			sum = sys.maxint
			
			if res[i][k].getDistance() != sys.maxint and res[k][j].getDistance() != sys.maxint:
				sum = res[i][k].getDistance() + res[k][j].getDistance()
				if  sum < res[i][j].getDistance():
					res[i][j].setDistance(res[i][k].getDistance() + res[k][j].getDistance())
					res[i][j].setPartition(k)
				else:
					pass
									
""" for i in range(n):
	print i, ":", 
	for j in range(n):
		print "(", res[i][j].getDistance(), ",", res[i][j].getPartition(), ")",
	print """
	
""" Computing average value """
sum_count = 0
for i in range(n):
	for j in range(n):
		if res[i][j].getDistance() < sys.maxint:
			sum_count += 1
			
avg_total = float(sum_count) / n
""" Rounded the value of to 2 decimal values """
avg_total = round(avg_total, 2)
print avg_total

""" Printing shortest path for the following """
for query in list_of_queries:
	src_dest = query.split(' ')
	source = vertices.index(src_dest[0])
	destination = vertices.index(src_dest[1])
	
	if res[source][destination].getPartition() == -1:
		print vertices[source], vertices[destination], "not reachable"
	else:
		path_list = []
		print_path(path_list, res, vertices, source, destination)
		path_list.insert(0, vertices[source])
		path_list.append(vertices[destination])
		print res[source][destination].getDistance(), ' '.join(path_list)