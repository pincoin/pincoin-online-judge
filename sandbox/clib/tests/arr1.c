#include <stdio.h>

#define MAX 2000000

int a[MAX] = {1};

int main(int argc, char *argv[]) {
    for (int i = 0; i < MAX; i++) {
        a[i] = i;
    }

    printf("%d %ld\n", a[MAX-1], sizeof(a));

    return 0;
}
