//Write a C++ program that accepts an array of integers, calculates the sum and 
//average, and displays the results. 

#include <iostream>
using namespace std;

int main()
{
    int n;

    cout << "Enter number of elements: ";
    cin >> n;

    int arr[n];     // array
    int sum = 0;

    cout << "Enter " << n << " numbers:\n";
    for(int i = 0; i < n; i++)
    {
        cin >> arr[i];
        sum = sum + arr[i];
    }

    float average = (float)sum / n;

    cout << "Sum = " << sum << endl;
    cout << "Average = " << average;

    return 0;
}
