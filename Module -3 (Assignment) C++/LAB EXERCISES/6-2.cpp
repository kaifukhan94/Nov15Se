//Create a class BankAccount with data members like balance and member functions 
//like deposit and withdraw. Implement encapsulation by keeping the data members 
//private. 

#include <iostream>
using namespace std;

class BankAccount
{
private:
    double balance;   // private data member

public:
    // Constructor to initialize balance
    BankAccount(double b)
    {
        balance = b;
    }

    void deposit(double amount)
    {
        balance = balance + amount;
        cout << "Deposited: " << amount << endl;
    }

    void withdraw(double amount)
    {
        if(amount <= balance)
        {
            balance = balance - amount;
            cout << "Withdrawn: " << amount << endl;
        }
        else
        {
            cout << "Insufficient Balance!" << endl;
        }
    }

    void showBalance()
    {
        cout << "Current Balance: " << balance << endl;
    }
};

int main()
{
    BankAccount acc(1000);   // object with initial balance

    acc.showBalance();
    acc.deposit(500);
    acc.withdraw(300);
    acc.showBalance();

    return 0;
}
