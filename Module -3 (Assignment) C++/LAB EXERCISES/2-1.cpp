//Write a C++ program that demonstrates the use of variables and constants. Create 
//variables of different data types and perform operations on them. 

#include <iostream>
using namespace std;

int main() {
    // Variables of different data types
    int a = 10, b = 5;
    float price = 99.5;
    char grade = 'A';
    bool status = true;

    // Constant
    const float PI = 3.14;

    // Performing operations
    int sum = a + b;
    int product = a * b;
    float circleArea = PI * a * a;   // Using constant

    // Displaying values
    cout << "Integer values: " << a << " and " << b << endl;
    cout << "Sum = " << sum << endl;
    cout << "Product = " << product << endl;

    cout << "Float value (price) = " << price << endl;
    cout << "Character value (grade) = " << grade << endl;
    cout << "Boolean value (status) = " << status << endl;

    cout << "Constant PI = " << PI << endl;
    cout << "Area of Circle using constant = " << circleArea << endl;

    return 0;
}
