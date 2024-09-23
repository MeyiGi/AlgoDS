#include <iostream>

class Node
{
public:
    int value;
    Node *next;

    Node(int value) : value(value), next(nullptr) {}
};

class Stack
{
private:
    Node *head;

public:
    Stack() : head(nullptr) {}

    void push(int value)
    {
        Node *newNode = new Node(value);
        newNode->next = head;
        head = newNode;
    }

    int pop()
    {
        if (isEmpty())
        {
            std::cerr << "The stack is empty, nothing to pop.\n";
            return -1;
        }
        int x = head->value;
        Node *temp = head;
        head = head->next;
        delete temp;
        return x;
    }

    bool isEmpty() const
    {
        return head == nullptr;
    }

    void print() const
    {
        Node *current = head;
        while (current != nullptr)
        {
            std::cout << current->value << " ";
            current = current->next;
        }
        std::cout << std::endl;
    }
};

int main()
{
    Stack muha;
    muha.push(10);
    muha.push(20);
    muha.push(30);

    std::cout << "Original stack: ";
    muha.print(); // Outputs: 30 20 10

    Stack muha_lox;
    muha_lox.push(muha.pop());
    muha_lox.push(muha.pop());
    muha_lox.push(muha.pop());

    std::cout << "Reversed stack: ";
    muha_lox.print(); // Outputs: 10 20 30

    return 0;
}
