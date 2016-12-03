#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <stdlib.h>
using namespace std;

string get_instruction(string s) {
	string result;
	int space_delimiter = s.find(" ");
	if (space_delimiter != -1)
		result = s.substr(0, space_delimiter);
	else {
		result = s;
	}
	return result;
}

int get_value(string s) {
	int result;
	int space_delimiter = s.find(" ");
	string value = s.substr(space_delimiter + 1);
	result = atoi(value.c_str());
	return result;
}

// function to obtain the parent of the child
int parent_of_node(int x, int no_of_childs) {
	return (x - 1) / no_of_childs;
}

// which_child is used to point out 1st, 2nd, 3rd, ..... , nth
// function to obtain which child_of_node
int child_of_node (int x, int no_of_childs, int which_child) {
	return (no_of_childs * x + which_child);
}

void min_heapify(vector<int> &v, int no_of_childs, int node) {
	int a[no_of_childs];
	for (int i = 0; i < no_of_childs; i ++) {
		a[i] = child_of_node(node, no_of_childs, i + 1);
	}
	
	int smallest = node;
	for (int i = 0; i < no_of_childs; i ++) {
		if (a[i] < v.size() && v.at(a[i]) < v.at(smallest)) {
			smallest = a[i];
		}
	}
	
	if (smallest != node) {
		swap(v[node], v[smallest]);
		min_heapify(v, no_of_childs, smallest);
	}
}

void build_min_heap(vector<int> &v, int no_of_childs) {
	if (v.size() > 1) {
		int heap_size = v.size();
	
		//Build heap for all non-leaves
		int n = (heap_size - 2) / no_of_childs;
	
		for (int i = n; i >= 0; i --) {
			min_heapify(v, no_of_childs, i);
		}
	}
}

void insert(vector<int> &v, int value, int no_of_childs) {
	v.push_back(value);
	int node = v.size() - 1;
	
	while (node > 0 && v[parent_of_node(node, no_of_childs)] > v[node]) {
		swap(v[parent_of_node(node, no_of_childs)], v[node]);
		node = parent_of_node(node, no_of_childs);
	}
}

int removeMin(vector<int> &v, int no_of_childs) {
	if (v.size() < 1) {
		cout << "Heap Underflow Condition" << endl;
		exit(-1);
	}
	
	int result;
	result = v[0];
	swap(v[0], v[v.size() - 1]);
	v.pop_back();
	
	// Now build the min heap for the new list
	min_heapify(v, no_of_childs, 0);
	
	return result;
}

/**
Here we are implementing a min heap datastructure in 
order to perform add and remove instructions.

add v ---- insert value v to the heap 
				-> v is a 32-bit signed value
remove --- removes the minimum value from the heap and 
		   prints it on a line to standard output 
		   (In min heap, we are talking about the first 
		   element (or) root element)
**/
int main() {
	vector<int> result;
	
	string input;
	while(getline(cin, input)) {
		string instruction = get_instruction(input);
		
		if (instruction.compare("add") == 0) { /* Add instruction call */
			int value = get_value(input);
			insert(result, value, 3); /* Trinary Heap Insert */
		} else if (instruction.compare("remove") == 0) { /* Remove instruction call */
			int min = removeMin(result, 3); /* Trinary Heap Remove */
			cout << min << endl;
		}
	}
	
	return 0;
}
