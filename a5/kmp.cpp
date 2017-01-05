#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <ctime>
using namespace std;

int naive(string text, int n, string pattern, int m) {
	for (int i = 0;i < n; i++) {
		bool check = true;
		int j = 0;
		while ((i + j) < n && j < m) {
			int diff = (int) text[i + j] - (int) pattern[j];
			if (diff != 0) {
				check = false;
				break;
			} else {
				j++;
			}
		}
		
		if (check) {
			return i;
		}
	}
	return -1;
}

void compute_prefix_table(int *pi_table, string pattern, int m) {
	pi_table[0] = 0;
	int j = 0;
	for (int i = 1; i < m; i++) {
		int diff = (int) pattern[j] - (int) pattern[i];
		while (j > 0 && diff != 0) {
			j = pi_table[j - 1];
		}
		
		if (diff == 0) {
			j++;
		}
		
		pi_table[i] = j;
	}
}

int kmp(string text, int n, string pattern, int m) {
	int pi_table[m];
	for (int i = 0; i < m; i++) {
		pi_table[i] = -1;
	}
	compute_prefix_table(pi_table, pattern, m);
	
	int j = 0;
	for (int i = 0; i < n; i++) {
		while (j > 0 && text[i] != pattern[j]) {
			j = pi_table[j - 1];
		}
		
		if (j == 0 && text[i] != pattern[j]) {
			continue;
		}
		
		if (text[i] == pattern[j]) {
			j++;
		}
		
		if (j == m) {
			return i - m + 1;
		}
	}
	return -1;
}

int main (int argc, char *argv[]) {
	string text, pattern;
	clock_t start, end;
	
	if (argc == 1) {
		int size = 1000000;
		text = "";
		pattern = "aaaaaaaaaaaaaaaaaaaabcccccccccc";
		for (int i = 0; i < size; i++) {
			if (i < 999990) {
				text += "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
			} else {
				text += pattern;
			}
		}
	} else {
		ifstream file;
		file.open(argv[1]);
		
		if (file.is_open()) {
			string data;
			int c = 0;
			while(!file.eof()) {
				if (c == 2) {
					break;
				} else if (c == 0) {
					file >> data;
					text = data;
				} else {
					file >> data;
					pattern = data;
				}
				c++;
			}
		}
	}
	
	int n = text.length(), m = pattern.length();
	
	//cout << "The text is as follows: " << text << endl;
	//cout << "The pattern is as follows: " << pattern << endl;
	
	//Naive String Search Operation
	start = clock();
	int naive_res = naive(text, n, pattern, m);
	end = clock();
	cout << "found at: " << naive_res << endl;
	cout << "naive search time: " << (double(end - start) / CLOCKS_PER_SEC) * 1000 << endl;
	
	//Standard String Search Operation
	start = clock();
	int std_res = text.find(pattern);
	end = clock();
	cout << "found at: " << std_res << endl;
	cout << "standard search time: " << (double(end - start) / CLOCKS_PER_SEC) * 1000 << endl;
	
	//KMP String Search Operation
	start = clock();
	int kmp_res = kmp(text, n, pattern, m);
	end = clock();
	cout << "found at: " << kmp_res << endl;
	cout << "kmp search time: " << (double(end - start) / CLOCKS_PER_SEC) * 1000 << endl;
	
	return 0;
}
