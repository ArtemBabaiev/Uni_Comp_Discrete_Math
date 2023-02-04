#include <iostream>
#include <Windows.h>
#include "Header.h"


using namespace std;

int main()
{

    bool repit = true;
	while (repit)
	{
		SetConsoleCP(1251);
		SetConsoleOutputCP(1251);
		
		int num;
		cout << "Введіть номер завдання: ";
		cin >> num;
		switch (num)
		{
		case 1:
			cout << "Фронт Хвиль\n";
			WaveFront();
			break;
		case 2:
			cout << "Алгоритм Дейкстри\n";
			///WaveFront();
			break;
		case 3:
			cout << "Алгоритм Флойда-Уоршелла\n";
			AFW();
			break;
		default:
			repit = false;
			break;
		}
	}
}

