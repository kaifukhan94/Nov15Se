//Write a C++ program that demonstrates arithmetic, relational, logical, and bitwise 
//operators. Perform operations using each type of operator and display the results. 

#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 5;

    // Arithmetic Operators
    cout << "Arithmetic Operators:" << endl;
    cout << "a + b = " << a + b << endl;
    cout << "a - b = " << a - b << endl;
    cout << "a * b = " << a * b << endl;
    cout << "a / b = " << a / b << endl;
    cout << "a % b = " << a % b << endl;

    // Relational Operators
    cout << "\nRelational Operators:" << endl;
    cout << "a > b = " << (a > b) << endl;
    cout << "a < b = " << (a < b) << endl;
    cout << "a == b = " << (a == b) << endl;
    cout << "a != b = " << (a != b) << endl;

    // Logical Operators
    cout << "\nLogical Operators:" << endl;
    cout << "(a > 5 && b < 10) = " << (a > 5 && b < 10) << endl;
    cout << "(a < 5 || b < 10) = " << (a < 5 || b < 10) << endl;
    cout << "!(a > b) = " << !(a > b) << endl;

    // Bitwise Operators
    cout << "\nBitwise Operators:" << endl;
    cout << "a & b = " << (a & b) << endl;
    cout << "a | b = " << (a | b) << endl;
    cout << "a ^ b = " << (a ^ b) << endl;
    cout << "a << 1 = " << (a << 1) << endl;
    cout << "a >> 1 = " << (a >> 1) << endl;

    return 0;
}
