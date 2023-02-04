#include <iostream>

void Task1();
void Task2();

int main()
{
    using namespace std;
    bool repit = true;
    int num;
    while (repit) {
        cout << "Enter number of Task ";
        cin >> num;
        switch (num)
        {
        case 1:
            Task1();
            break;
        case 2:
            Task2();
            break;
        default:
            repit = false;
            break;
        }
    }
}

