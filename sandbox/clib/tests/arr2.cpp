#include <iostream>
#include <cstdlib>
#define MAX 10000000
using namespace std;

int main(int argc, char *argv[]) {
    int *a = (int *)malloc(sizeof(int) * MAX);

    for (int i = 0; i < MAX; i++) {
        *(a+i) = i;
    }

    cout << a[MAX-1] << " " << sizeof(a) << endl;

    return 0;
}
