#include <iostream>
#include <set>
#include <algorithm>
#include <iterator>
#include <Windows.h>

void Task_2();
void Task_3_1();
void Task_3_2();
void Task_3_3();

int main()
{
    SetConsoleOutputCP(1251);
    int n, k;
    bool repit = true;
    while(repit)
    {
        std::cout << "\nВедіть номер завдання: ";
        std::cin >> n;
        switch (n)
        {
        case 2:
            Task_2();
            break;
        case 31:
            Task_3_1();
            break;
        case 32:
            Task_3_2();
            break;
        case 33:
            Task_3_3();
            break;
            
        default:
            repit = false;
        }
    
    }
}
