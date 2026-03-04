//Write a program that demonstrates the difference between local and global 
//variables in C++. Use functions to show scope. 

#include <iostream>
using namespace std;

// Global variable
int x = 10;

void show()
{
    int x = 20;   // Local variable (same name)

    cout << "Inside function, local x = " << x << endl;
    cout << "Inside function, global x = " << ::x << endl;
}

int main()
{
    cout << "Inside main, global x = " << x << endl;

    show();

    return 0;
}
