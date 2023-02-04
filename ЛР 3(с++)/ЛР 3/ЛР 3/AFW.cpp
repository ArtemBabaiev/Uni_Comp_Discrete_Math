#include <iostream>
#include <Windows.h>
#include <set>
#include <algorithm>
#include "Header.h"

using namespace std;
const int maxi = 9999;

void SetS(int** S, int size);
void ReductInf(int** S, int size);
set<int> FindAllPathes(int start, int end, int** S, set<int> Path);

void AFW() 
{
	SetConsoleOutputCP(1251);
	int length, i, j, k;
	cout << "¬вед≥ть к≥льк≥сть вершин: ";
	cin >> length;
	int** matrix = new int* [length];
	for (i = 0; i < length; i++)
		matrix[i] = new int[length];
	int** S = new int* [length];
	for (i = 0; i < length; i++)
		S[i] = new int[length];
	cout << "ћатриц€ ваг\n";
	Set2DArray(matrix, length);
	ReductInf(matrix, length);
	Print2DArray(matrix, length);
	cout << "ћатриц€ чогось\n";
	SetS(S, length);
	Print2DArray(S, length);

	for (k = 0; k < length; k++)
	{
		for (i = 0; i < length; i++)
		{
			if (i == k) 
			{
				continue;
			}
			for (j = 0; j < length; j++)
			{
				if (j == k)
				{
					continue;
				}
				int sum = matrix[i][k] + matrix[k][j];
				if (sum < matrix[i][j])
				{
					matrix[i][j] = sum;
					S[i][j] = k + 1;
				}
			}
		}
	}
	cout << "–езультат\n";
	Print2DArray(matrix, length);
	cout << "«м≥ни\n";
	Print2DArray(S, length);
	for (i = 1; i <= length; i++)
	{
		for (j = 1; j <= length; j++)
		{
			set<int> Path = {};
			Path = FindAllPathes(i, j, S, Path);
			std::copy(Path.begin(), Path.end(), std::ostream_iterator <int>(std::cout, " | "));
			Path.empty();
			cout << "\n";
		}
	}
}

set<int> FindAllPathes(int start, int end, int**S, set<int> Path)
{
	Path.insert(start);
	int a = 0;
	int ind = start - 1;
	a = S[ind][end - 1];
	if (a == start)
	{
		Path.insert(a);
		Path.insert(end);
		return Path;
	}
	if (a == 0)
	{
		return {};
	}
	return FindAllPathes(a, end, S, Path);
}












void SetS(int** S, int size) 
{
	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			if (i == j) 
			{
				S[i][j] = 0;
			}
			else
			{
				S[i][j] = i + 1;
			}
		}
	}
}
void ReductInf(int** arr, int size)
{
	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			if (arr[i][j] == -1) 
			{
				arr[i][j] = maxi;
			}
		}
	}
}