#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <vector>
using namespace std;

struct Node {
    int val;
    Node* left;
    Node* right;

    Node(int val) : val(val), left(nullptr), right(nullptr) {}
};

class BinaryTree {
public:
    Node* root;

    BinaryTree() : root(nullptr) {}

    // Add node to tree function
    void addNode(int val) {
        if (!root) {
            root = new Node(val);
            return;
        }

        Node* current = root;
        Node* parent = nullptr;

        while (current) {
            parent = current;
            current = val > current->val  ? current->right : current->left;
        }

        // Insert the new node as a child of the found parent node
        if (val > parent->val) {
            parent->right = new Node(val);
        } else {
            parent->left = new Node(val);
        }
    }

    // Delete Function and helper functions
    void deleteNode(int val) {
        Node* parent = nullptr;
        Node* node_to_delete = findNodeWithParent(val, parent);

        // Check if the node exists
        if (!node_to_delete) {
            cout << "Value not found in the tree." << endl;
            return;
        }

        // CASE 1: Node has no left child
        if (!node_to_delete->left) {
            replaceChild(parent, node_to_delete, node_to_delete->right);
            delete node_to_delete;
            return;
        }

        // CASE 2: Node has no right child
        if (!node_to_delete->right) {
            replaceChild(parent, node_to_delete, node_to_delete->left);
            delete node_to_delete;
            return;
        }

        // CASE 3: Node has two children
        // Find the minimum node in the right subtree (inorder successor)
        Node* minParent = node_to_delete;
        Node* minNode = findMinNode(node_to_delete->right, minParent);

        // Replace node_to_delete's value with minNode's value
        node_to_delete->val = minNode->val;

        // deleting the min node
        replaceChild(minParent, minNode, minNode->right);
        delete minNode;
    }

    // does node exists?
    void findNode(int val) {
        Node* current = root;

        while (current) {
            if (current->val == val) {
                cout << endl << val << " exist in tree" << endl;
                return;
            }

            current = val > current->val ? current->right : current->left;
        }
        cout << val << " not exist in tree" << endl;
    }
    
    // Getting sorted array
    vector<int> inorderTraversal() {
        vector<int> sortedValues;
        inorderHelper(root, sortedValues);
        cout << "\n";
        for (int i = sortedValues.size() - 1; i >= 0; i--) {
            cout << sortedValues[i] << " -> ";
        }
        cout << "nullptr" << endl;
        return sortedValues;

    }

    // Saving tree to json file
    void saveTree(const string& filename) {
        ofstream file(filename);
        exportToJson(file, root);
        file.close();
    }

private:

    Node* findNodeWithParent(int val, Node*& parent) {
        Node * current = root;
        parent = nullptr;

        while (current) {
            if (current->val == val) {
                return current;
            }
            parent = current;
            current = val > current->val ? current->right : current->left;
        }
        return nullptr;
    }

    Node* findMinNode(Node* node, Node*& parent) {
        if (!node->left) {
            return node;
        }
        parent = node;
        while (node->left) {
            parent = node;
            node = node->left;
        }
        return node;
    };

    void replaceChild(Node* parent, Node* oldChild, Node* newChild) {
        if (!parent) {
            root = newChild;
        } else if (parent->left == oldChild) {
            parent->left = newChild;
        } else {
            parent->right = newChild;
        }
    }

    void inorderHelper(Node* node, vector<int>& sortedValues) {
        if (!node) 
            return;
        
        inorderHelper(node->left, sortedValues);
        sortedValues.push_back(node->val);
        inorderHelper(node->right, sortedValues);
    }


    
    // json stuff for connecting with matplotlib
    void exportToJson(ofstream& file, Node* node) {
        if (!node) {
            file << "null";
            return;
        }
        file << "{ \"val\": " << node->val << ", \"left\": ";
        exportToJson(file, node->left);
        file << ", \"right\": ";
        exportToJson(file, node->right);
        file << " }";
    }
};

int main() {
    BinaryTree tree;
    int choice, val;
    cout << "Please add at least 2 node\n" << endl;

    while (true) {
        cout << "1. Add Node\n2. Delete Node\n3. View Sorted Tree(stack)\n4. does num exist?\n5. Exit" << endl;
        cout << "Enter the choice: ";
        cin >> choice;

        switch(choice) {
            case 1:
                cout << "Enter value to add: ";
                cin >> val;
                tree.addNode(val);
                tree.saveTree("tree.json");
                break;
            case 2:
                cout << "Enter value to delete: ";
                cin >> val;
                tree.deleteNode(val);
                tree.saveTree("tree.json");
                break;
            case 3:
                tree.inorderTraversal();
                break;
            case 4:
                cout << "Enter val which you wanna know exists: ";
                cin >> val;
                tree.findNode(val);
                break;
            case 5:
                cout << "Terminating the process..." << endl;
                exit(0);
        }
        cout << "\n";
    }
    return 0;
}
