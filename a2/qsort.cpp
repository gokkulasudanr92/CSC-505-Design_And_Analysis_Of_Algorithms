#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <utility>
#include <sys/time.h>
using namespace std;

int partition_input(vector<int> &v, int start, int end) {
	int pivot = v[end];
	
	int i = start - 1;
	int j = start;
	while (j < end) {
		if (v[j] <= pivot) {
			i ++;
			swap (v[i], v[j]);
		}
		j++;
	}
	swap(v[i + 1], v[end]);
	return i + 1;
}

void bubble_sort(vector<int> &v, int start, int end) {
	if (start < end) {
		for (int i = start; i <= end; i ++) {
			for (int j = start; j <= (end - 1); j++) {
				if (v[j] > v[j + 1]) {
					swap(v[j],v[j + 1]);
				}
			}
		}
	}
}

void insertion_sort(vector<int> &v, int start, int end) {
	if (start < end) {
		for (int i = start + 1; i <= end; i++) {
			int key = i;
			while (key > start && v[key] < v[key - 1]) {
				swap(v[key - 1], v[key]);
				key --;
			}
		}
	}
}

void quicksort(vector<int> &v, int start, int end, int strategy_size) {
	if (start < end) {
		int smaller_size = (end - start) + 1;
		if (smaller_size <= strategy_size) {
			insertion_sort(v, start, end);
		} else {
			int partition = partition_input(v, start, end);
			quicksort(v, start, partition - 1, strategy_size);
			quicksort(v, partition + 1, end, strategy_size);
		}
	}
}

long getMilliseconds() {
	timeval tv;
	gettimeofday( &tv, NULL );
	long int ms = tv.tv_sec;
	ms = ms * 1000 + tv.tv_usec / 1000;
	return ms;
}

/**
The program is used to implement a quicksort algorithm whose 
sorting strategy changes when the size of the list is less 
than 'k' where k is an input argument;
**/
int main (int argc, char **args) {
	int strategy_size = 0;
	vector<int> input;
	
	if (argc <= 2) {
		if (argc == 2)
			strategy_size = atoi(args[1]);
	} else {
		cout << "Usage of "; cout << args[0]; cout << "is: ";
		cout << args[0]; cout << " n"; cout << endl;
	}
	
	//Read the input array
	string x;
	while(getline(cin, x)) {
		input.push_back(atoi(x.c_str()));
	}
	
	long t0 = getMilliseconds();
	quicksort(input, 0, input.size() - 1, strategy_size);
	long t1 = getMilliseconds();
	fprintf( stderr, "%ld\n", t1 - t0 );
	
	vector<int>::iterator it;
	for (it = input.begin(); it != input.end(); it++) {
		cout << *it; cout << endl;
	}
	
	return 0;
}