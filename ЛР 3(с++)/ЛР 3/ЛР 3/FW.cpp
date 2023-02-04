#include <iostream>
#include <Windows.h>
#include <set>
#include <algorithm>
#include <iterator>
#include "Header.h"

using namespace std;

void WaveFront() 
{
	SetConsoleOutputCP(1251);
	int length, i , j;
	cout << "¬вед≥ть к≥льк≥сть вершин: ";
	cin >> length;
	int** matrix = new int* [length];
	for (i = 0; i < length; i++)
		matrix[i] = new int[length];
	Set2DArray(matrix, length);
	Print2DArray;
	set <int> FW = { 0 };
	set <int> D = { 0 };
	
}

