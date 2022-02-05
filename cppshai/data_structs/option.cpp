/* Compile with:
 * gcc <name> -std=c++17 -o <out>
 */

#include <iostream>
#include <optional>

std::optional<int> divide(int a, int b)
{
    if (b == 0)
    {
        return std::nullopt;
    }
    return a / b;
}

void div_and_print(int a, int b)
{
    std::optional<int> opt_answer = divide(a, b);
    if (opt_answer.has_value())
    {
        int answer = *opt_answer; // Not dereferencing; overloaded syntax
        std::cout << "Success: ";
        std::cout << answer << std::endl;
    } else {
        std::cout << "Error" << std::endl;;
    }
}

int main() {
    div_and_print(12, 4);
    div_and_print(3, 4);
    div_and_print(3, 0);
}
