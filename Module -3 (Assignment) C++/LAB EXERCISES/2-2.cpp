//Write a C++ program that performs both implicit and explicit type conversions and 
//prints the results.

#include <iostream>
using namespace std;

int main() {
    // Implicit Type Conversion
    int num1 = 10;
    float num2 = 5.5;

    float result1 = num1 + num2;   // int automatically converted to float

    cout << "Implicit Conversion:" << endl;
    cout << "num1 (int) + num2 (float) = " << result1 << endl;

    // Explicit Type Conversion (Type Casting)
    float value = 9.7;
    int result2 = (int)value;   // manually converting float to int

    cout << "\nExplicit Conversion:" << endl;
    cout << "Float value = " << value << endl;
    cout << "After casting to int = " << result2 << endl;

    return 0;
}
