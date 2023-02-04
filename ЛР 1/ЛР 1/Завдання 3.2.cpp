#include <iostream>
#include <set>
#include <algorithm>
#include <iterator>
#include <Windows.h>


void Task_3_2() 
{
	SetConsoleOutputCP(1251);
	std::set <int> A;
	std::set <int> B;
	std::set <int> C;
	std::set <int> FirstStep;
	std::set <int> SecondStep;
	std::set <int> ThirdStep;
	std::set <int> F;

	int i, k;
	std::cout << "Введіть елементи множини А:\n";
	for ( i = 0; i < 10;) 
	{
		std::cin >> k;
		if (k >= 1 && k <= 100) {
			A.insert(k);
			i++;
		}
	}

	std::cout << "\nМножина А:\n";
	std::copy(A.begin(), A.end(), std::ostream_iterator<int>(std::cout, " "));
	for (i = 0; i < 10; i++) {
		B.insert((rand() % 51 + 10) * 3);
	}
	std::cout << "\nМножина B:\n";
	std::copy(B.begin(), B.end(), std::ostream_iterator<int>(std::cout, " | "));
	for (i = 0; i < 10; i++) {
		C.insert(rand()%101 + 20);
	}
	std::cout << "\nМножина С:\n";
	std::copy(C.begin(), C.end(), std::ostream_iterator<int>(std::cout, " "));

	// BUC
	set_union(B.begin(), B.end(), C.begin(), C.end(), std::inserter(FirstStep, FirstStep.begin()));

	// SimilarDifference
	set_symmetric_difference(A.begin(), A.end(), FirstStep.begin(), FirstStep.end(), std::inserter(SecondStep, SecondStep.begin()));

	// C\B
	set_difference(C.begin(), C.end(), B.begin(), B.end(), std::inserter(ThirdStep, ThirdStep.begin()));

	// SD U C\B
	set_union(SecondStep.begin(), SecondStep.end(), ThirdStep.begin(), ThirdStep.end(), std::inserter(F, F.begin()));

	std::cout << "\nМножина F:\n";
	std::copy(F.begin(), F.end(), std::ostream_iterator<int>(std::cout, " | "));
}
