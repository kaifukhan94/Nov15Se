//Write a C++ program that accepts user input for their name and age and then 
//displays a personalized greeting. 

#include <iostream>
using namespace std;

int main() {
    char name[50];
    int age;

    cout << "Enter your name: ";
    cin >> name;   // Takes single word name

    cout << "Enter your age: ";
    cin >> age;

    cout << "Hello " << name << "! ";
    cout << "You are " << age << " years old.";

    return 0;
}
