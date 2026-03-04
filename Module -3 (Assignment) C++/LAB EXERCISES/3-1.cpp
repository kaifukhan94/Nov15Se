//Write a C++ program that takes a student’s marks as input and calculates the grade 
//based on if-else conditions. 

#include <iostream>
using namespace std;

int main() {
    int marks;

    cout << "Enter student marks (0-100): ";
    cin >> marks;

    if (marks >= 90 && marks <= 100) {
        cout << "Grade: A";
    }
    else if (marks >= 75) {
        cout << "Grade: B";
    }
    else if (marks >= 60) {
        cout << "Grade: C";
    }
    else if (marks >= 50) {
        cout << "Grade: D";
    }
    else if (marks >= 0) {
        cout << "Result: Fail";
    }
    else {
        cout << "Invalid marks entered!";
    }

    return 0;
}
