#include <iostream>
#include <climits>
using namespace std;

typedef struct OptimalData {
	long product;
	int partition;
} DP;


void construct_matrix_chain(DP **m, int matrices[], int no_of_matrices) {
	for (int i = 1; i < no_of_matrices; i++) {
		m[i][i].product = 0;
		m[i][i].partition = i;
		for (int j = 1; j < no_of_matrices; j++) {
			if (i != j) {
				m[i][j].product = LONG_MAX;
				m[i][j].partition = 0;
			}
		}
	}
	
	for (int i = (no_of_matrices - 1); i > 0; i--) {
		for (int j = i + 1; j < no_of_matrices; j++) {
			for (int k = i; k < j; k++) {
				long new_product = matrices[i - 1] * matrices[k] * matrices[j];
				new_product = new_product + m[i][k].product + m[k + 1][j].product;
				if (m[i][j].product > new_product) {
					m[i][j].product = new_product;
					m[i][j].partition = k;
				}
			}
		}
	}
}

void print_solution(DP **m, int p, int q) {
	if (p == q) {
		cout << "M";
		cout << p;
	} else {
		int k = m[p][q].partition;
		
		if (p != k) {
			cout << "( ";
			print_solution(m, p, k);
			cout << " )";
		} else {
			print_solution(m, p, k);
		}
		
		cout << " * ";
		
		if ((k + 1) != q) {
			cout << "( ";
			print_solution(m, k + 1, q);
			cout << " )";
		} else {
			print_solution(m, k + 1, q);
		}
	}	
}

int main () {
	int no_of_matrices;
	cin >> no_of_matrices;
	no_of_matrices = no_of_matrices + 1;

	int *matrices;
	matrices = new int[no_of_matrices];

	int input_counter = no_of_matrices;
	while(input_counter != 0) {
		cin >> matrices[no_of_matrices - input_counter];
		input_counter --;
	}	
  
	//Initializig the dynamic storage matrix
	DP **m;
	m = new DP *[no_of_matrices];
	for (int i = 0; i < no_of_matrices; i ++) {
		m[i] = new DP[no_of_matrices];
	}
	
	construct_matrix_chain(m, matrices, no_of_matrices);
	
	//Next step recovering the solution from the matrix
	print_solution(m, 1, no_of_matrices - 1);
	
	cout << endl;

	return 0;
}