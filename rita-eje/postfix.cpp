#include <iostream>
#include <stack>
#include <string>

using namespace std;

// Simple arithmetic operations
double operate(char op, double a, double b)
{
    if (op == '+')
        return a + b;
    if (op == '-')
        return a - b;
    if (op == '*')
        return a * b;
    if (op == '/')
        return a / b;
    return 0; // Bad case
}

// For prefix calculation
double calculatePrefix(const string &expr)
{
    stack<double> s;

    // From end to beginning
    for (int i = expr.size() - 1; i >= 0; i--)
    {
        char ch = expr[i];

        if (isdigit(ch))
        {
            s.push(ch - '0'); // Conversion char to int
        }
        else if (ch == '+' || ch == '-' || ch == '*' || ch == '/')
        {
            double a = s.top();
            s.pop();
            double b = s.top();
            s.pop();
            s.push(operate(ch, a, b)); // Executing math operation
        }
    }

    return s.top(); // Возвращаем результат
}

int main()
{
    string expr1 = "+ / 3 4 2";     // (3 / 4) + 2 = 14
    string expr2 = "+ 5 * 2 3";     // (2 * 3) + (-5) = 1
    string expr3 = "/ * 12 2 3";    // (12 * 2) / 3 = 8
    string expr4 = "- + 5 6 * 2 3"; // (2 * 3) - (5 + 6) = 5

    cout << "Result: " << calculatePrefix(expr1) << endl;
    cout << "Result: " << calculatePrefix(expr2) << endl;
    cout << "Result: " << calculatePrefix(expr3) << endl;
    cout << "Result: " << calculatePrefix(expr4) << endl;

    return 0;
}
