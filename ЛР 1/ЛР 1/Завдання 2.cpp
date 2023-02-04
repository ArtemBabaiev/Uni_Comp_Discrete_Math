#include <iostream>
#include <set>
#include <algorithm>
#include <iterator>
#include <Windows.h>

void Task_2()
{
    SetConsoleOutputCP(1251);
    std::set <int> A = { 1,9,10,11,15,16,17,22 };
    std::set <int> B = { 1,4,5,6,7,8,13,14,18,19,23 };
    std::set <int> C = { 1,2,3,4,5,16,18,19,24,25 };


    std::cout << "\nSet C:\n";
    std::copy(C.begin(), C.end(), std::ostream_iterator<int>(std::cout, " "));
    C.erase(24);
    std::cout << "\n";
    std::copy(C.begin(), C.end(), std::ostream_iterator<int>(std::cout, " "));
    
    
    std::cout << "����� ������ � " << size(A);
    std::cout << "\n�� ������ � " << B.empty();
    
    C.clear();
    std::cout << "\nSet C:\n";
    std::copy(C.begin(), C.end(), std::ostream_iterator<int>(std::cout, " "));
    std::cout << "\n�� ������ � " << C.empty();

    
    if (B.count(5))
    {
        std::cout << "\n\n�������� 5 �� B\n";
    }
    else std::cout << "\n\n�� �������� 5 �� B\n";
    if (B.count(0))
    {
        std::cout << "�������� 0 �� B\n";
    }
    else std::cout << "�� ��������0 �� B\n";
    
    B.swap(A);
    std::cout << "\nSet A:\n";
    std::copy(A.begin(), A.end(), std::ostream_iterator<int>(std::cout, " "));
    std::cout << "\nSet C:\n";
    std::copy(B.begin(), B.end(), std::ostream_iterator<int>(std::cout, " "));
}