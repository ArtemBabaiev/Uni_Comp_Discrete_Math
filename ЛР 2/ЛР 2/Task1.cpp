#include <iostream>
#include <cstdlib>
#include <ctime>

void Task1() {
	srand(time(NULL));
	using namespace std;
	int length, i, j;
	cout << "Enter lenght of arrays ";
	cin >> length;

	int* A = new int[length];
	int* B = new int[length];

	int** matrix = new int* [length];
	for (i = 0; i < length; ++i)
		matrix[i] = new int[length];

	for (i = 0; i < length; i++) {
		A[i] = rand() % 13 - 6;
		B[i] = rand() % 13 - 6;
	}
	cout << "Array A\n\t";
	for (i = 0; i < length; i++) {
		cout << A[i] << " | ";
	}
	cout << '\n';
	cout << "Array B\n\t";
	for (i = 0; i < length; i++) {
		cout << B[i] << " | ";
	}

	int k = 0, t;
	for (i = 0; i < length; i++)
	{
		t = 0;
		for (j = 0; j < length; j++)
		{
			if (A[j] != 0) 
			{
				if (B[i] % A[j] == 0)
				{
					matrix[k][t] = 1;
					t++;
				}
				else
				{
					matrix[k][t] = 0;
					t++;
				}
			}
			else 
			{
				matrix[k][t] = 0;
				t++;
			}
			
		}
		k++;
	}
	delete[] A;
	delete[] B;

	cout << "\nBinary matrix\n";
	for (i = 0; i < length; i++) {
		for (j = 0; j < length; j++) {
			cout << matrix[i][j] << " | ";
		}
		cout << '\n';
	}

	for (i = 0; i < length; i++) {
		delete[] matrix[i];
	}
	delete[] matrix;
}