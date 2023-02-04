#include <iostream>
#include <cstdlib>
#include <ctime>
#include <Windows.h>

void Task2() {
	SetConsoleOutputCP(1251);
	srand(time(NULL));
	using namespace std;

	bool sym = false, asym = false, antisym = false;
	bool refl = false, antirefl = false;
	bool trans = false, antitrans = false;
	bool isbreak = false;
	int length, i, j;
	cout << "Enter lenght of arrays ";
	cin >> length;

	int** matrix = new int* [length];
	for (i = 0; i < length; i++)
		matrix[i] = new int[length];
	for (i = 0; i < length; i++)
	{
		for (j = 0; j < length; j++)
		{
			cin >> matrix[i][j];
			//matrix[i][j] = rand() % 2;
		}
	}

	for (i = 0; i < length; i++) {
		for (j = 0; j < length; j++) {
			cout << matrix[i][j] << " | ";
		}
		cout << '\n';
	}

	//Рефлексивність 𝐸⊆𝐴
	for (i = 0; i < length; i++) 
	{
		if (matrix[i][i] == 1) {
			refl = true;
		}
		else 
		{
			refl = false;
			break;
		}
	}

	//Антирефлектисвність 𝐴∩𝐸=∅
	for (i = 0; i < length; i++)
	{
		if (matrix[i][i] == 0)
		{
			antirefl = true;
		}
		else
		{
			antirefl = false;
			break;
		}
	}
	
	if (refl)
		cout << "\nРефлексивна\n";
	if (antirefl)
		cout << "\nАнтирефлексивна\n";


	//Симетричність 𝐴=𝐴^(−1)
	for (i = 0; i < length; i++)
	{
		for (j = 0; j < length; j++) 
		{
			if (matrix[i][j] == matrix[j][i])			//якщо рівні симетричні елементи ставимо тру, якщо хоч одні не співпадає, то ставимо фолс
			{
				sym = true;
			}
			else
			{
				sym = false;
				isbreak = true;
				break;
			}
		}
		if (isbreak) {
			break;
		}
	}
	isbreak = false;

	//Асиметричнысть 𝐴∩𝐴^(−1)=∅
	for (i = 0; i < length; i++)
	{
		for (j = 0; j < length; j++)
		{
			if (matrix[i][j] != matrix[j][i])			//якщо вони різні, то тру
			{
				asym = true;
			}
			else if (matrix[i][j] == matrix[j][i] && matrix[i][j] == 0)		//якщо рівні, але нулі допускаються
			{
				asym = true;
			}
			else if (matrix[i][j] == matrix[j][i] && matrix[i][j] == 1)		//якщо рівні, то тілки коли одиниці переводимо у фолс
			{
				asym = false;
				isbreak = true;
				break;
			}
		}
		if (isbreak) {
			break;
		}
	}
	isbreak = false;

	//Антисиметричність 𝐴∩𝐴^(−1)⊆𝐸
	for (i = 0; i < length; i++)
	{
		for (j = 0; j < length; j++)
		{
			if (matrix[i][j] == matrix[j][i] && i == j)			// якщо однакові на головній діагоналі
			{
				antisym = true;
			}
			else if (matrix[i][j] == matrix[j][i] && i != j && matrix[i][j]==1)			// якщо однакові на симетричних місцях і лише на одиницях
			{
				antisym = false;
				isbreak = true;
				break;
			}
		}
		if (isbreak) {
			break;
		}
	}
	isbreak = false;

	if (sym)
		cout << "\nСиметрична\n";
	if (antisym)
		cout << "\nАнтисиметрична\n";
	if (asym)
		cout << "\nАсиметрична\n";




	int** arr = new int* [length];
	for (i = 0; i < length; i++)
		arr[i] = new int[length];
	int k;

	//Транзитивність 𝐴∘𝐴⊆𝐴
	for (i = 0; i < length; i++)
	{
		for (j = 0; j < length; j++)
		{
			if (matrix[i][j] == 1) {
				for (k = 0; k < length; k++) {
					if (matrix[j][k] == 1) {
						//cout <<i<<" "<< j << " " << k<<'\n';
						arr[i][k] = 1;
					}
				}
			}
		}
	}

	for (i = 0; i < length; i++)
	{
		for (j = 0; j < length; j++)
		{
			if (arr[i][j] != 1)
				arr[i][j] = 0;
		}
	}

	cout <<"\nКомпозиція:\n";

	for (i = 0; i < length; i++)
	{
		for (j = 0; j < length; j++)
		{
			cout << arr[i][j] << " | ";
		}
		cout << '\n';
	}

	for (i = 0; i < length; i++)
	{
		for (j = 0; j < length; j++)
		{
			if (arr[i][j] == matrix[i][j])			// якщо рівні, тру
			{
				trans = true;
			}
			else if (arr[i][j] == 0 && matrix[i][j] == 1)		// якщо різні, але допускається 
			{
				trans = true;
			}
			else if (arr[i][j] == 1 && matrix[i][j] == 0)		 // не збіг
			{
				trans = false;
				isbreak = true;
				break;
			}
		}
		if (isbreak) 
		{
			break;
		}
	}
	if (trans) 
	{
		cout << "\nТранзитивна\n";
	}
	isbreak = false;

	//Антитранзитивність (А∘А)∩А=∅
	for (i = 0; i < length; i++)
	{
		for (j = 0; j < length; j++)
		{
			if (arr[i][j] != matrix[i][j])					//якщо різні то ок
			{
				antitrans = true;
			}
			else if (arr[i][j] == matrix[i][j] && arr[i][j] == 0)   //коли однакові, але нулі - допускається
			{
				antitrans = true;
			}
			else if (arr[i][j] == matrix[i][j] && arr[i][j] == 1)   //коли однакові та одиниці - фолс
			{
				antitrans = false;
				isbreak = true;
				break;
			}
			
		}
		if (isbreak)
		{
			break;
		}
	}
	if (antitrans)
	{
		cout << "\nАнтитранзитивна\n";
	}










	for (i = 0; i < length; i++) {
		delete[] arr[i];
	}
	delete[] arr;

	for (i = 0; i < length; i++) {
		delete[] matrix[i];
	}
	delete[] matrix;
}


