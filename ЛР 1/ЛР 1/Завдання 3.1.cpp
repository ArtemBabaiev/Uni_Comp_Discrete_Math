#include <iostream>
#include <set>
#include <algorithm>
#include <iterator>

void Task_3_1 ()
{
    std::set <char> A = { 'q', 's', 'c', 'l', 'r', 's' , 'f', 'N', 'E', 's' };
    std::set <char> B = { 'S', 'z', 'x', 'Y', 'k', 'g', 'V', 'r', 't', 'b' };
    std::set <char> C = {'U', 'A', 'l', 'd', 'p', 'O', 's', 'F', 'B', 'C', 'W' };
    std::set <char> F;
    std::set <char> FirstStep;
    std::set <char> SecondStep;
    std::set <char> ThirdStep;
    std::set <char> FandS;

    //A∩B
    set_intersection(A.begin(), A.end(), B.begin(), B.end(), std::inserter(FirstStep, FirstStep.begin()));
    //BUC
    set_union(B.begin(), B.end(), C.begin(), C.end(), std::inserter(SecondStep, SecondStep.begin()));
    //AUC
    set_union(A.begin(), A.end(), C.begin(), C.end(), std::inserter(ThirdStep, ThirdStep.begin()));
    // 1U2
    set_union(FirstStep.begin(), FirstStep.end(), SecondStep.begin(), SecondStep.end(), std::inserter(FandS, FandS.begin()));
    // Finale
    set_intersection(FandS.begin(), FandS.end(), ThirdStep.begin(), ThirdStep.end(), std::inserter(F, F.begin()));
    std::copy(F.begin(), F.end(), std::ostream_iterator<char>(std::cout, " "));
    std::cout << '\n';

}