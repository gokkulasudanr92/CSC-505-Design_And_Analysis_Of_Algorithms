#Implementation of a binary search tree
class BinarySearchTree(object):
	""" Representation of a node in a binary search tree """
	def __init__(self, parent, key, character):
		""" Create a new leaf with key and character """
		self.key = key
		self.parent = parent
		self.left = None
		self.right = None
		self.character = character
		
	def insert(self, key, character):
		""" Insert a key into the subtree """
		if key <= self.key:
			if self.left is None:
				self.left = BinarySearchTree(self, key, character)
				self.left.parent = self
			else:
				self.left.insert(key, character)
		else:
			if self.right is None:
				self.right = BinarySearchTree(self, key, character)
				self.right.parent = self
			else:
				self.right.insert(key, character)
				
	def printTree(self):
		print self.key
		if not self.left is None:
			self.left.printTree()
		if not self.right is None:
			self.right.printTree()

""" Initialize character list dictionary """
character_list = []

for i in xrange(256):
	character_list.append(chr(i))

character_list_dict = {}

for i in character_list:
	character_list_dict[i] = 1
character_list_dict['EOF'] = 1;

""" Read file and update the dictionary """
import sys

input_string = "";
for line in sys.stdin:
	input_string = input_string + line

text = input_string.strip()

for x in character_list_dict:
	character_list_dict[x] = character_list_dict[x] + text.count(x)

""" Implementing Ternary Heap for Min Priority Queue """
def parent(x):
	return (x - 1) / 3

def child_first(x):
	return 3 * x + 1
	
def child_second(x):
	return 3 * x + 2
	
def child_third(x):
	return 3 * x + 3
	
def min_heapify(list, node):
	first = child_first(node)
	second = child_second(node)
	third = child_third(node)
	
	smallest = node
	if first < len(list) and list[first] < list[smallest]:
		smallest = first
	
	if second < len(list) and list[second] < list[smallest]:
		smallest = second
		
	if third < len(list) and list[third] < list[smallest]:
		smallest = third
		
	if smallest != node:
		temp = list[node];
		list[node] = list[smallest]
		list[smallest] = temp
		min_heapify(list, smallest)
		
"""def build_min_heap(list):
	if len(list) > 1:
		heap_size = len(list)
		
		n = (heap_size - 2) / 3;
		for i in range(n, 0, -1):
			min_heapify(list, i)"""

def insert(list, val):
	list.append(val)
	node = len(list) - 1
	
	while node > 0 and list[parent(node)].key > list[node].key:
		temp = list[parent(node)]
		list[parent(node)] = list[node]
		list[node] = temp
		node = parent(node)
		
def removeMin(list):
	if len(list) < 1:
		print "Heap Underflow condition"
		exit(-1)
		
	result = list[0]
	list.pop(0)
	min_heapify(list, 0)
	return result

ternary_priority_queue = []

for key in character_list_dict:
	insert(ternary_priority_queue, BinarySearchTree(None, character_list_dict[key], key))
	
while len(ternary_priority_queue) != 1:
	first_min_tree = removeMin(ternary_priority_queue)
	second_min_tree = removeMin(ternary_priority_queue)
	new_root = BinarySearchTree(None, int(first_min_tree.key) + int(second_min_tree.key), None)
	new_root.left = first_min_tree
	new_root.right = second_min_tree
	insert(ternary_priority_queue, new_root)

huffman_root = removeMin(ternary_priority_queue)

""" Implementing all leaf traversals """
codes = {}

def codesFunc(s, node, codes):
	if node.character:
		if not s:
			codes[node.character] = "0"
		else:
			codes[node.character] = s
	else:
		codesFunc(s+"0", node.left, codes)
		codesFunc(s+"1", node.right, codes)

codesFunc("", huffman_root, codes)

""" Printing the codes """
data = sorted(codes)
data.remove('EOF')

for key in data:
	key_with_out_quotes = repr(key).replace("\\x", "")[1:-1]
	if len(key_with_out_quotes) == 1:
		print " ", key_with_out_quotes, " ", codes[key]
	elif len(key_with_out_quotes) == 2:
		if key_with_out_quotes.find("\\") == -1:
			print "", key_with_out_quotes.upper(), " ", codes[key]
		else:
			print "", key_with_out_quotes, " ", codes[key]
print 'EOF', " ", codes["EOF"]