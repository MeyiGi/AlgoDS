#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

class Array {
public:
    int rear;
    int front;
    int size;
    int *arr;
    int count;
    

    Array(int size) {
        this->count = 0;
        this->rear = -1;
        this->front = -1;
        this->size = size;

        arr = new int[size];
    }

    bool isEmpty() {
        return count == 0;
    }

    bool isFull() {
        return count == size;
    }
};

void insertQatEnd(Array &arr, int val) {
    if (arr.isFull()) {
        cout << "\nQueue is full" << endl;
        return;
    }

    if (arr.isEmpty()) {
        arr.rear = arr.front = 0;
    } 
    else {
        arr.rear = (arr.rear + 1) % arr.size;
    }

    arr.arr[arr.rear] = val;
    arr.count += 1;
}

void insertQatBeg(Array &arr, int val) {
    if (arr.isFull()) {
        cout << "\nQueue is full" << endl;
        return;
    }

    if (arr.isEmpty()) {
        arr.rear = arr.front = 0;
    }
    else {
        arr.front = (arr.front - 1 + arr.size) % arr.size;
    }

    arr.arr[arr.front] = val;
    arr.count += 1;
}

int delQBeg(Array &arr) {
    int return_value = arr.arr[arr.front];
    arr.front = (arr.front + 1) % arr.size;
    arr.count -= 1;

    if (arr.isEmpty()) {
        arr.rear = arr.front = -1;
    }

    return return_value;
}

int delQEnd(Array &arr) {
    int return_value = arr.arr[arr.rear];
    arr.rear = (arr.rear - 1 + arr.size) % arr.size;
    arr.count -= 1;

    if (arr.isEmpty()) {
        arr.rear = arr.front = -1;
    }

    return return_value;
}

void printArray(Array &arr) {
    for (int i = 0; i < arr.count; i++) {
        cout << arr.arr[(arr.front + i) % arr.size] << " ";
    }
    cout << endl;
}


int max_value = 99;
int min_value = 10;
int max_size = 7;


int main() {
    // Seed the random number generator
    srand(time(0));

    // Declaration of Double ended arrays
    Array arr1(max_size);
    Array arr2(max_size);
    Array arr3(max_size);

    // Initializing with random numbers
    for (int i = 0; i < max_size; i++) {
        int random_number1 = rand() % (max_value - min_value + 1) + min_value;
        insertQatEnd(arr1, random_number1);

        int random_number2 = rand() % (max_value - min_value + 1) + min_value;
        insertQatEnd(arr2, random_number2);
    }

    // Print arrays with random number
    cout << "arr1: ";
    printArray(arr1);

    cout << "arr2: ";
    printArray(arr2);

    cout << "arr3: ";
    printArray(arr3);
    cout << "\n";

    // Interaction with arrays
    int popped_num1 = delQBeg(arr1);
    int popped_num2 = delQBeg(arr2);

    insertQatBeg(arr3, popped_num1);
    insertQatBeg(arr3, popped_num2);

    // Printing result of interactions
    cout << "arr1: ";
    printArray(arr1);

    cout << "arr2: ";
    printArray(arr2);

    cout << "arr3: ";
    printArray(arr3);

    return 0;
}