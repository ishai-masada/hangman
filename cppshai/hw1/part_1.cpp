/* Ishai Masada
 * Fahrenheit and Celsius Conversions */

#include <iostream>
using namespace std;

const float F_TO_C_FACTOR = 5.0 / 9.0;

// Converts temperature from Celsius to Fahrenheit
int f2c(int temp)
{
    return (temp - 32) * (F_TO_C_FACTOR);
}

// Converts temperature from Fahrenheit to Celsius
int c2f(int temp)
{
    return (temp * 1.8) + 32;
}

int main()
{
    // Initial Temperature
    int temperature = 55;
    cout << "Temperature in Celsius: ";
    cout << temperature << endl;

    // Celsius to Fahrenheit
    cout << "Celsius to Fahrenheit: ";
    // The new temperature after it's been converted to Faherenheit
    int f_temp = c2f(temperature);
    cout << f_temp << endl;

    // Fahrenheit to Celsius
    cout << "Fahrenheit to Celsius: ";
    // The new temperature after it's been converted to Celsius
    int c_temp = f2c(f_temp);
    cout << c_temp << endl;
}
