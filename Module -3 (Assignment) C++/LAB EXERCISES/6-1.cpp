//Write a C++ program that defines a class Calculator with functions for addition, 
//subtraction, multiplication, and division. Create objects to use these functions.

#include <iostream>
using namespace std;

class Calculator
{
public:
    int add(int a, int b)
    {
        return a + b;
    }

    int subtract(int a, int b)
    {
        return a - b;
    }

    int multiply(int a, int b)
    {
        return a * b;
    }

    float divide(int a, int b)
    {
        return (float)a / b;
    }
};

int main()
{
    Calculator calc;   // object creation
    int num1, num2, choice;

    cout << "Enter first number: ";
    cin >> num1;

    cout << "Enter second number: ";
    cin >> num2;

    cout << "\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n";
    cout << "Enter your choice: ";
    cin >> choice;

    if(choice == 1)
        cout << "Result = " << calc.add(num1, num2);
    else if(choice == 2)
        cout << "Result = " << calc.subtract(num1, num2);
    else if(choice == 3)
        cout << "Result = " << calc.multiply(num1, num2);
    else if(choice == 4)
        cout << "Result = " << calc.divide(num1, num2);
    else
        cout << "Invalid choice";

    return 0;
}
