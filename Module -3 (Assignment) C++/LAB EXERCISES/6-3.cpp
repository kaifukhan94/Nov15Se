//Write a program that implements inheritance using a base class Person and derived 
//classes Student and Teacher. Demonstrate reusability through inheritance. 

#include <iostream>
using namespace std;

// Base class
class Person
{
public:
    string name;
    int age;

    void setData(string n, int a)
    {
        name = n;
        age = a;
    }

    void showData()
    {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
    }
};

// Derived class 1
class Student : public Person
{
public:
    int rollNo;

    void setStudent(string n, int a, int r)
    {
        setData(n, a);
        rollNo = r;
    }

    void showStudent()
    {
        showData();
        cout << "Roll No: " << rollNo << endl;
    }
};

// Derived class 2
class Teacher : public Person
{
public:
    string subject;

    void setTeacher(string n, int a, string s)
    {
        setData(n, a);
        subject = s;
    }

    void showTeacher()
    {
        showData();
        cout << "Subject: " << subject << endl;
    }
};

int main()
{
    Student s;
    Teacher t;

    string name, subject;
    int age, rollNo;

    // Input for Student
    cout << "Enter Student Name: ";
    cin >> name;
    cout << "Enter Student Age: ";
    cin >> age;
    cout << "Enter Roll No: ";
    cin >> rollNo;

    s.setStudent(name, age, rollNo);

    cout << endl;

    // Input for Teacher
    cout << "Enter Teacher Name: ";
    cin >> name;
    cout << "Enter Teacher Age: ";
    cin >> age;
    cout << "Enter Subject: ";
    cin >> subject;

    t.setTeacher(name, age, subject);

    cout << "\nStudent Details:\n";
    s.showStudent();

    cout << "\nTeacher Details:\n";
    t.showTeacher();

    return 0;
}
