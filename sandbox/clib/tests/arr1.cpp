#include <iostream>
#define MAX 2000000
using namespace std;

int a[MAX] = {1};

int main(int argc, char *argv[]) {
    for (int i = 0; i < MAX; i++) {
        a[i] = i;
    }

    cout << a[MAX-1] << " " << sizeof(a) << endl;

    return 0;
}
