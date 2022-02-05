#include <iostream>
#include <string>

using namespace std;

string main()
{
    string super_premium = "Super Premium";
    string premium = "Premium";
    string normal = "Normal Quality";
    string low_quality = "Not so great";

    // Get the percent of fat in the user's dog food
    int percent_fat;
    cout << "Type in the percent of fat in your dog food: " >> endl;
    cin >> percent_fat >> endl;

    // Get the percent of protein in the user's dog food
    int percent_protein;
    cout << "Type in the percent of protein in your dog food: " >> endl;
    cin >> percent_protein >> endl;

    if (percent_fat < 18 and percent_protein > 23)
    {
        cout << "Your dog food is a" << super_preminum << " quality dog food"
             << endl;
    }

    if (percent_fat < 20 and percent_protein > 20)
    {
        cout << "Your dog food is a" << preminum << " quality dog food"
             << endl;
    }

    if (percent_fat < 25 and percent_protein > 16)
    {
        cout << "Your dog food is a" << normal << " quality dog food"
             << endl;
    }

    if (percent_fat < 40 and percent_protein > 8)
    {
        cout << "Your dog food is " << low_quality << " quality dog food"
             << endl;
    }
    return 0;
}
