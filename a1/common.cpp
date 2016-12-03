#include<iostream>
#include<string>
#include<set>
#include<vector>
using namespace std;

//function to capture the input string
string raw_input(string message) {
  string s;
  cout<< message << endl;
  getline(cin,s);
  return s;
}

//functoin to get the length of the string
int _string_length(string s) {
	return s.length();
}

//function to get the left shift movement strings
vector<string> get_left_shift_common_sub_strings_with_repetition(string first, string second) {
	vector<string> result;

	for (int i = 0; i < (int) first.length(); i++) {
		cout << (i + 1);
		cout << ". Left Shift" << endl; 
		int j = 0;
		int first_start = i;
		int prev_subtract = 0;
		string sub_string = "";
		while(j < (int) second.length() && j < ((int) first.length() - i)) {
			cout << first[first_start];
			cout << " - ";
			cout << second[j] << endl;
			int subtract = (int) first[first_start] - (int) second[j];
			if (prev_subtract == 0 && subtract == 0) {
				sub_string += second[j];
			} else if (prev_subtract != 0 && subtract == 0 && !sub_string.empty()) {
				result.push_back(sub_string);
				sub_string = "";
			} else if (prev_subtract != 0 && subtract == 0 && sub_string.empty()) {
				sub_string += second[j];
			} else if (prev_subtract != 0 && subtract != 0 && !sub_string.empty()) {
				result.push_back(sub_string);
				sub_string = "";
			} else if (prev_subtract == 0 && subtract != 0 && !sub_string.empty()) {
				result.push_back(sub_string);
				sub_string = "";
			}
			prev_subtract = subtract;
			j++; first_start++;
		}
		if (!sub_string.empty()) {
			result.push_back(sub_string);
			sub_string = "";
		}
	}

	return result;
}

vector<string> get_right_shift_common_sub_strings_with_repetition(string first,string second) {
	vector<string> result;
	
	for (int i = 1; i < (int) second.length(); i++) {
		cout << i;
		cout << ". Right Shift" << endl;
		int j = 0;
		int second_start = i;
		int prev_subtract = 0;
		string sub_string = "";
		while (second_start < (int) second.length()) {
			cout << first[j];
			cout << " - ";
			cout << second[second_start] << endl;
			int subtract = (int) first[j] - (int) second[second_start];
			if (prev_subtract == 0 && subtract == 0) {
				sub_string += second[second_start];
			} else if (prev_subtract != 0 && subtract == 0 && !sub_string.empty()) {
				result.push_back(sub_string);
				sub_string = "";
			} else if (prev_subtract != 0 && subtract == 0 && sub_string.empty()) {
				sub_string += second[second_start];
			} else if (prev_subtract != 0 && subtract != 0 && !sub_string.empty()) {
				result.push_back(sub_string);
				sub_string = "";
			} else if (prev_subtract == 0 && subtract != 0 && !sub_string.empty()) {
				result.push_back(sub_string);
				sub_string = "";
			}
			prev_subtract = subtract;
			j++; second_start++;
		}
		if (!sub_string.empty()) {
			result.push_back(sub_string);
			sub_string = "";
		}
	}

	return result;
}

set<string> _get_all_substrings(string s) {
	set<string> result;
	
	if (!s.empty()) {
		int sub_string_size = 1;
		while (sub_string_size < (int) s.length()) {
			for(int j = 0; j < (int) s.length() && ((int) s.length() - j) >= sub_string_size; j++) {
				string ss = s.substr(j, sub_string_size);
				result.insert(ss);
			}
			sub_string_size++;
		}
		result.insert(s);
	}
	
	return result;
}

int get_common_substrings(string first, string second) {	
	set<string> output;

	if (first.length() < second.length()) {
		string temp = second;
		second = first;
		first = temp;
	}

	//Left shift sub string captures
	vector<string> left_shift_string = get_left_shift_common_sub_strings_with_repetition(first,second);
	
	vector<string>::iterator left_shift_it;
	for (left_shift_it = left_shift_string.begin(); left_shift_it != left_shift_string.end(); left_shift_it++) {
		set<string> item_set = _get_all_substrings(*left_shift_it);
		output.insert(item_set.begin(), item_set.end()); 
	}
	
	cout << endl << endl;

	//Right shift sub string captures
	vector<string> right_shift_string = get_right_shift_common_sub_strings_with_repetition(first, second);

	vector<string>::iterator right_shift_it;
	for (right_shift_it = right_shift_string.begin(); right_shift_it != right_shift_string.end(); right_shift_it++) {
		set<string> item_set = _get_all_substrings(*right_shift_it);
		output.insert(item_set.begin(), item_set.end()); 
	}

	cout << endl << endl << "List of common substrings:" << endl << endl;
  	set<string>::iterator it;
  	for (it = output.begin(); it != output.end(); ++it) {
  		cout << *it << endl;
  	}

	return output.size();
}

int main() {
  string first_string = raw_input("Input the first string:");
  string second_string = raw_input("Input the second string:");

  //Write the logic of the program here
  int count = get_common_substrings(first_string, second_string);
  cout << endl << endl << "No. of common sub strings: ";
  cout << count << endl;

  return 0;
}
