#include <iostream>
#include <string>
using namespace std;

class PriorityQueue {
private:
    int *priority;
    string *subjects;
    int size;
    int count;

public:
    PriorityQueue(int size) {
        this->size = size;
        this->count = 0;
        priority = new int[size];
        subjects = new string[size];
    }

    ~PriorityQueue() {
        delete[] priority;
        delete[] subjects;
    }

    bool isEmpty() {
        return count == 0;
    }

    bool isFull() {
        return count == size;
    }

    void enqueue(int val, string subject) {
        if (isFull()) {
            cout << "Queue is full" << endl;
            return;
        }

        int i;
        for (i = count - 1; i >= 0 && priority[i] < val; i--) {
            priority[i + 1] = priority[i];
            subjects[i + 1] = subjects[i];
        }

        priority[i + 1] = val;
        subjects[i + 1] = subject;
        count++;
    }

    string dequeue() {
        if (isEmpty()) {
            cout << "Queue is empty" << endl;
            return "is empty";
        }

        count--;
        return subjects[count];
    }

    void display() {
        if (isEmpty()) {
            cout << "Queue is empty" << endl;
            return;
        }

        for (int i = size - 1; i >= 0; i--) {
            cout << i << "[" << priority[i] << "] " << subjects[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    PriorityQueue q(6);

    q.enqueue(3, "physics");
    q.enqueue(7, "math");
    q.enqueue(1, "algorithms");
    q.enqueue(2, "differentials");
    q.enqueue(5, "programming");

    q.display();

    cout << "Dequeued: " << q.dequeue() << endl;
    q.enqueue(9, "philosophy");
    

    q.display();

    return 0;
}
