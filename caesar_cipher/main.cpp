    
#include <iostream>
#include <string>
using namespace std;

class CircularQueue {
private:
    char arr[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    int front;
    int rear;
    int size;
    int count;
    int alphabet_size = 26;
    int text_length;
    int text_front;
    int text_rear;
    
    char text[1000];
public:
    CircularQueue(string text) {
        this->size = 26;
        front = 0;
        rear = 25;
        count = 26;

        // for text
        text_length = text.length();
        for (int i = 0; i < text_length; i++) {
            this->text[i] = text[i];
        }

        text_rear = text_length - 1;
    }


    void enqueue(char value) {
        if (isFull()) {
            cout << "Queue is full, cannot enqueue " << value << endl;
            return;
        }

        if (isEmpty()) {
            front = 0;
        }

        text_length += 1;
        text_rear = (text_rear + 1) % text_length;
        text[text_rear] = value;
    }

    char dequeue() {
        if (isEmpty()) {
            cout << "Queue is empty, cannot dequeue" << endl;
            return '\0';
        }

        char value = text[text_front];
        text_front = (text_front + 1) % text_length;
        text_length -= 1;

        return value;
    }

    char peek() {
        if (isEmpty()) {
            cout << "Queue is empty, nothing to peek" << endl;
            return '\0';
        }
        return arr[front];
    }
    bool isFull() {
        return false;
    }

    bool isEmpty() {
        return false;
    }

    void display() {
        if (isEmpty()) {
            cout << "Queue is empty" << endl;
            return;
        }

        cout << "Queue elements: ";
        int i = front;
        for (int j = 0; j < count; j++) {
            cout << arr[i] << " ";
            i = (i + 1) % size;
        }
        cout << endl;
    }
    
    void encryption(int shiftvalue) {
        if (isEmpty()) {
            cout << "Queue is empty" << endl;
            return;
        }

        int i = front;
        
        
        front = (front + shiftvalue) % size; 
        rear = (rear + shiftvalue) % size;
        
        for (int i = 0; i < text_length; i++) {
            char ch = text[i]; // h
            
            for (int j = 0; j < count; j++) {
                if (ch == arr[j]) {
                    text[i] = (arr[(j + shiftvalue) % size]);
                }
            }
            
        }
        
        for (int i = 0; i < text_length; i++) {
            cout << text[i] << ' ';
        }
        cout << endl;
    }
    
    void dencryption(int key) {
        if (isEmpty()) {
            cout << "Queue is empty" << endl;
            return;
        }

        int i = front;

        
        
        front = (front + size - key) % size; 
        rear = (rear + size - key) % size;
        
        for (int i = 0; i < text_length; i++) {
            char ch = text[i]; // i
            
            for (int j = 0; j < count; j++) {
                if (ch == arr[j]) {
                    text[i] = (arr[(j + (1000000 * size) - key) % size]); // size = 26, j = 6, key = 77 
                }
            }
            
        }
        
        for (int i = 0; i < text_length; i++) {
            cout << text[i] << ' ';
        }
        cout << endl;
    }
};

int main() {

    string text;
    int key;
    
    cout << "enter text for encryption: ";
    cin >> text;

    cout << "enter key (integer) for encryption: ";
    cin >> key;

    CircularQueue q(text);
    q.display();
    
    q.encryption(key);
    q.display();
    
    q.dencryption(key);
    q.display();

    return 0;
}