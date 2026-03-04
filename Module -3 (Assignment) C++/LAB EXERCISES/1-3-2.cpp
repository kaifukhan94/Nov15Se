//Object-Oriented Programming (OOP) Program
//In OOP, we use class and object.

#include <iostream>
using namespace std;

class Rectangle {
    float length, width;

public:
    void getData() {
        cout << "Enter length: ";
        cin >> length;

        cout << "Enter width: ";
        cin >> width;
    }

    float calculateArea() {
        return length * width;
    }
};

int main() {
    Rectangle r;   // Object creation

    r.getData();
    cout << "Area of Rectangle = " << r.calculateArea();

    return 0;
}
