//Write a program that prints a right-angled triangle using stars (*) with a nested loop. 

#include <iostream>
using namespace std;

int main() {
    int rows;

    cout << "Enter number of rows: ";
    cin >> rows;

    for (int i = 1; i <= rows; i++) {      // Outer loop
        for (int j = 1; j <= i; j++) {     // Inner loop
            cout << "* ";
        }
        cout << endl;
    }

    return 0;
}
