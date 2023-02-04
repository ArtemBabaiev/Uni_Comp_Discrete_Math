#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

void Set2DArray(int** arr, int size) {
	srand(time(NULL));
	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			cin >> arr[i][j];
			//arr[i][j] = rand() % edge;
		}
	}
}
void Print2DArray(int** arr, int size)
{
	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			cout << arr[i][j] << "\t";
		}
		cout << '\n';
	}
}












/*#include <vector>
std::vector <int> A = { 1,9,5,4,11,15,16,17,22 };
std::copy(A.begin(), A.end(), std::ostream_iterator <int>(std::cout, " | "));*/