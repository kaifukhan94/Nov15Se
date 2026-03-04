//Write a C++ program that defines functions for basic arithmetic operations (add, 
//subtract, multiply, divide). The main function should call these based on user input. 

#include <iostream>
using namespace std;

// Function declarations
int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int multiply(int a, int b) {
    return a * b;
}

float divide(int a, int b) {
    return (float)a / b;
}

int main() {
    int num1, num2, choice;

    cout << "Enter first number: ";
    cin >> num1;

    cout << "Enter second number: ";
    cin >> num2;

    cout << "\nSelect Operation:" << endl;
    cout << "1. Add" << endl;
    cout << "2. Subtract" << endl;
    cout << "3. Multiply" << endl;
    cout << "4. Divide" << endl;
    cout << "Enter your choice: ";
    cin >> choice;

    if (choice == 1) {
        cout << "Result = " << add(num1, num2);
    }
    else if (choice == 2) {
        cout << "Result = " << subtract(num1, num2);
    }
    else if (choice == 3) {
        cout << "Result = " << multiply(num1, num2);
    }
    else if (choice == 4) {
        if (num2 != 0)
            cout << "Result = " << divide(num1, num2);
        else
            cout << "Cannot divide by zero!";
    }
    else {
        cout << "Invalid choice!";
    }

    return 0;
}
