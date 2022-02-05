/* Ishai Masada
 * Computing Retroactive Pay */

#include <iostream>
using namespace std;

const double salary_increase = 1.076;

int main()
{
    // The new salary after adding the increase
    double new_salary;

    // How many months the user has not been paid their new salary
    int time = 6;

    while (true)
    {
        // Get the previous salary from the user
        double prev_salary;
        cout << endl
             << "Type in your previous annual salary or 0 to end the program: ";
        cin >> prev_salary;

        // End the program if the user enters a zero
        if (prev_salary == 0)
        {
            break;
        }

        // Convert the salary into a monthly salary
        double prev_monthly_salary = prev_salary / 12;

        // Calculate the salary that the user is supposed to be paid
        // Derive the monthly salary from the new salary
        new_salary = prev_salary * salary_increase;
        double new_monthly_salary = new_salary / 12;

        // Display the new yearly salary
        cout << "New yearly salary: " << int(new_salary) << endl
             << "New monthly salary: " << int(new_monthly_salary) << endl;

        // Calculate and display the retroactive pay
        double owed_pay = new_monthly_salary * 6;
        double actual_pay = prev_monthly_salary * 6;
        int retroactive_pay = owed_pay - actual_pay;
        cout << "Retroactive pay: " <<  retroactive_pay << endl;
    }

    return 0;
}

