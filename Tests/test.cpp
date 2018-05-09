#include "stdafx.h"
#include <utility>
#include <iomanip>
#include <random>
#include <iostream>
#include <vector>
#include <string>
#include <ctime> 
#include <map>
using namespace std;

vector<int> prefixFunction(const string& text, int& count)
{
	if (text.empty())
		return {};

	vector<int> prefixVector(text.size(), 0);

	for (int i = 1; i < text.size(); i++)
	{
		int k = prefixVector[i - 1];

		while (k > 0 and text[i] != text[k])
		{
			count++;
			k = prefixVector[k - 1];
		}
			
		count++;
		if (text[i] == text[k])
			k++;

		prefixVector[i] = k;
	}

	return prefixVector;
}

vector<int> algoKnuthMorrisPratt(const string& pattern, const string& text, int& count)
{
	vector<int> resultVector;
	vector<int> prefixVector = prefixFunction(pattern, count);
	if (pattern.empty() || text.empty())
		return { -1 };

	int pos = 0;

	for (int i = 0; i < text.size(); i++) 
	{

		//cout << pos << ":" << pattern.size() << ":" << pattern[pos] << ":" << text[i] << endl;
		while (pos > 0 and (pos >= pattern.size() || pattern[pos] != text[i]))
		{
			count++;
			pos = prefixVector[pos - 1];
			
		}
			
		count++;
		if (pattern[pos] == text[i])
			pos++;

		if (pos == pattern.size())
			resultVector.push_back(i - pos + 1);
	}

	if (resultVector.empty())
		resultVector.resize(1, -1);

	return resultVector;
}

std::vector<size_t> naive_matcher(const std::string& pattern, const std::string& text, int& count)
{
	if (!pattern.size() || !text.size()) {
		return {};
	}

	std::vector<size_t> result;
	result.reserve(text.size() / pattern.size());

	for (size_t i = 0; i < text.size() - pattern.size() + 1; i++) {
		for (size_t j = 0; j < pattern.size(); j++) {
			count++;

			if (pattern[j] == text[j + i]) {
				if (j == pattern.size() - 1)
					result.push_back(i);
			}
			else {
				break;
			}
		}
	}

	return result;
}


string generateString(int size)
{
	string result;
	for (int i = 0; i < size; i++)
	{

		result += rand() % 26 + 'A';
	}

	return result;
}

int main()
{

	srand(time(0));

	map<int, map<int, pair<int, int>>> a;

	cout << "Test\nComparison of naive search and KMP algorithm\n";
	for (int i = 1000; i <= 1000000; i*=10)
	{
		for (int j = 2; j <= 64; j*=2)
		{
			cout << "Pattern size: " << j << "  Text size: " << i << endl;
			int naive_count = 0;
			int kmp_count = 0;

			cout << "Number of tests: 10 - Processing ";
			for (int k = 1; k <= 10; k++)
			{				
				string pattern = generateString(j);
				string text = generateString(i);
								
				naive_matcher(pattern, text, naive_count);
				algoKnuthMorrisPratt(pattern, text, kmp_count);

				cout << ".";
				
			}
			naive_count /= 10.0;
			kmp_count /= 10.0;

			cout << "     OK\nAverange comparasion: " << naive_count << ":" << kmp_count <<  "\n-----------------------------\n";
			a[j][i] = make_pair(naive_count, kmp_count);
			

		}
	}

		

	

	cout << "|    | ";
	for (auto& x : a[2])
		cout  << setw(18) << setfill(' ') << x.first << "  |";
	

	for (auto& t : a)
	{
		cout << "\n|----|---------------------|--------------------|--------------------|--------------------|\n";
		cout << "|" << right << setw(3) << setfill(' ') << t.first << " |  ";
		for (auto& x : t.second)
		{
			cout << setw(8) << setfill(' ') << x.second.first;
			cout << ";";
			cout << setw(8) << setfill(' ') << x.second.second << "  | ";
	    }
	}

	//for (auto& t : a)
	//{
	//	cout << setw(3) << right << setfill(' ') << t.first << " :  ";
	//	for (auto& x : t.second)
	//	{
	//		if (x.second.first <  x.second.second)
	//			cout << left << setfill(' ') << "Nat (" << abs(x.second.first - x.second.second) << ")  ";
	//		else
	//			cout << left << setfill(' ') << "KMP (" << abs(x.second.first - x.second.second) << ")  ";
	//	}
	//	cout << "\n";
	//}


	system("pause");
	return 0;
			
}