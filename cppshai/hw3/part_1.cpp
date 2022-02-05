#include <iostream>

using namespace std;

int main()
{
    int first_num;
    cout << "Type in the first number: ";
    cin >> first_num;

    int second_num;
    cout << "Type in the second number: ";
    cin >> second_num;

    cout << endl << "Each operation is always done using the first number before the second"
         << endl;

    if (second_num != 0)
    {
        int quotient = first_num / second_num;
        cout << endl << "Quotient of the two numbers: " << quotient << endl;
    }
    else
    {
        cout << endl << "You cannot divide any number by 0." << endl;
    }

    int difference = first_num - second_num;
    cout << endl << "Difference of the two numbers: " << difference << endl;

    int sum = first_num + second_num;
    cout << endl << "Sum of the two numbers: " << sum << endl;

    int product = first_num * second_num;
    cout  << endl << "Product of the two numbers: " << product << endl;

    return 0;
}
