//Procedural Programming (POP) Program
//In POP, we use functions and normal variables.

#include <iostream>
using namespace std;

float area(float length, float width) {
    return length * width;
}

int main() {
    float l, w;

    cout << "Enter length: ";
    cin >> l;

    cout << "Enter width: ";
    cin >> w;

    cout << "Area of Rectangle = " << area(l, w);

    return 0;
}
