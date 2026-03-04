//Write a C++ program to check if a given string is a palindrome (reads the same 
//forwards and backwards). 

#include <iostream>
using namespace std;

int main()
{
    char str[100];
    int i, length = 0;
    bool isPalindrome = true;

    cout << "Enter a string: ";
    cin >> str;

    // Find length
    for(i = 0; str[i] != '\0'; i++)
    {
        length++;
    }

    // Check palindrome
    for(i = 0; i < length / 2; i++)
    {
        if(str[i] != str[length - i - 1])
        {
            isPalindrome = false;
            break;
        }
    }

    if(isPalindrome)
        cout << "It is a Palindrome.";
    else
        cout << "It is not a Palindrome.";

    return 0;
}
