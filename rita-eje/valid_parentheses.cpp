#include <iostream>
#include <string>
using namespace std;

bool isValid(string s)
{
    if (s.length() == 0)
    {
        return false;
    }
    const int MAX_LENGTH = 1000;
    char stack[MAX_LENGTH];
    int top = -1;

    for (char i : s)
    {
        if (i == '(' || i == '{' || i == '[')
        {
            stack[++top] = i;
        }
        else
        {
            if (top == -1 ||
                (i == ')' && stack[top] != '(') ||
                (i == '}' && stack[top] != '{') ||
                (i == ']' && stack[top] != '['))
            {
                return false;
            }

            top--;
        }
    }

    return top == -1;
}

int main()
{
    string x1 = "()[]{}";
    string x2 = "([])";
    string x3 = "(]";
    string x4 = "";

    cout << isValid(x1) << endl; // true
    cout << isValid(x2) << endl; // true
    cout << isValid(x3) << endl; // false
    cout << isValid(x4) << endl; // true

    return 0;
}
