#include <iostream>
#include <iterator>
#include <set>
#include <vector>
#include <algorithm>
#include <iterator>
#include <Windows.h>


void Task_3_3()
{
	SetConsoleOutputCP(1251);
	std::vector <int> A = { 1,9,10,11,15,16,17,22 };
	std::vector <int> B = { 1,4,5,6,7,8,13,14,18,19,23 };
	std::vector <int> C = { 1,2,3,4,5,16,18,19,24,25 };
	std::vector <int> FirstStep;
	std::vector <int> SecondStep;
	std::vector <int> ThirdStep;
	std::vector <int> F;

	// A\C
	set_difference(A.begin(), A.end(), C.begin(), C.end(), std::inserter(FirstStep, FirstStep.begin()));

	// B SD C
	set_symmetric_difference(B.begin(), B.end(), C.begin(), C.end(), std::inserter(SecondStep, SecondStep.begin()));

	// sec ∩ B
	set_intersection(SecondStep.begin(), SecondStep.end(), B.begin(), B.end(), std::inserter(ThirdStep, ThirdStep.begin()));

	// first U third
	set_union(FirstStep.begin(), FirstStep.end(), ThirdStep.begin(), ThirdStep.end(), std::inserter(F, F.begin()));
	std::copy(F.begin(), F.end(), std::ostream_iterator <int>(std::cout, " | "));
}