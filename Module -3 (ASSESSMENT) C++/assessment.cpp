#include <iostream>
#include <ctime>
using namespace std;

class ATM
{
private:
    int pin;
    long balance;

public:
    // Constructor to initialize values
    ATM();

    void welcomeScreen();
    void helpScreen();
    bool checkPin();
    void menu();
    void deposit();
    void withdraw();
    void checkBalance();
};

// Constructor definition using scope resolution
ATM::ATM()
{
    pin = 12345;          // Fixed ATM PIN
    balance = 20000;     // Present account balance
}

// Function to display welcome screen
void ATM::welcomeScreen()
{
    time_t now = time(0);

    cout << "====================================\n";
    cout << "        WELCOME TO ATM SYSTEM        \n";
    cout << "====================================\n";
    cout << "\n1. Enter ATM PIN";
    cout << "\n2. Help";
    cout << "\n====================================\n";
}

// Function to display help screen
void ATM::helpScreen()
{
    cout << "\n--- HELP SCREEN ---\n";
    cout << "1. Enter correct ATM PIN (Only three attempt allowed)\n";
    cout << "2. Select appropriate menu option\n";
    cout << "3. Contact bank for any issue\n\n";
}

// Function to check ATM PIN
bool ATM::checkPin()
{
    int userPin;
    cout << "\nEnter ATM PIN: ";
    cin >> userPin;

    if (userPin == pin)
        return true;
    else
        return false;
}

// Function to show menu after successful login
void ATM::menu()
{
    int choice;
    do
    {
        cout << "\n===== ATM MENU =====";
        cout << "\n1. Deposit";
        cout << "\n2. Withdraw";
        cout << "\n3. Check Balance";
        cout << "\n4. Exit";
        cout << "\nEnter choice: ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            deposit();
            break;

        case 2:
            withdraw();
            break;

        case 3:
            checkBalance();
            break;

        case 4:
            cout << "\nThank you for using ATM.\n";
            break;

        default:
            cout << "\nInvalid choice!\n";
        }

    } while (choice != 4);
}

// Function to deposit amount
void ATM::deposit()
{
    long amount;
    cout << "\nEnter amount to deposit: Rs. ";
    cin >> amount;

    if (amount > 0)
    {
        balance += amount;
        cout << "Amount deposited successfully.\n";
    }
    else
    {
        cout << "Invalid amount.\n";
    }
}

// Function to withdraw amount
void ATM::withdraw()
{
    long amount;
    cout << "\nEnter amount to withdraw: Rs. ";
    cin >> amount;

    if (amount > balance)
    {
        cout << "\nTransaction Failed: Insufficient Balance.\n";
    }
    else
    {
        balance -= amount;
        cout << "\nPlease collect your cash.\n";
    }
}

// Function to check balance
void ATM::checkBalance()
{
    cout << "\nAvailable Balance: Rs. " << balance << endl;
}

// Main function
int main()
{
    ATM user;
    int choice;

    user.welcomeScreen();
    cout << "Enter your choice: ";
    cin >> choice;

    if (choice == 1)
    {
        if (user.checkPin())
        {
            cout << "\nPIN Verified Successfully.\n";
            user.menu();
        }
        else
        {
            cout << "\nIncorrect PIN. Access Denied.\n";
        }
    }
    else if (choice == 2)
    {
        user.helpScreen();
    }
    else
    {
        cout << "\nInvalid choice.\n";
    }

    return 0;
}
