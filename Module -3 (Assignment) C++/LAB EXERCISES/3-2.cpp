//Write a C++ program that asks the user to guess a number between 1 and 100. The 
//program should provide hints if the guess is too high or too low. Use loops to allow 
//the user multiple attempts. 

#include <iostream>
using namespace std;

int main() {
    int number, guess;

    cout << "Enter a number between 1 and 100: ";
    cin >> number;

    cout << "Now guess the number!" << endl;

    while (guess != number) {
        cout << "Enter your guess: ";
        cin >> guess;

        if (guess > number) {
            cout << "Too High!" << endl;
        }
        else if (guess < number) {
            cout << "Too Low!" << endl;
        }
        else {
            cout << "Correct Guess!" << endl;
        }
    }

    return 0;
}
