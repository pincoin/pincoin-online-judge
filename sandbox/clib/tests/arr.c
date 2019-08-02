#include <stdio.h>

#define MAX 2000000

int main(int argc, char *argv[]) {
    auto int a[MAX] = {1};

    for (int i = 0; i < MAX; i++) {
        a[i] = i;
    }

    printf("%d %ld\n", a[MAX-1], sizeof(a));

    return 0;
}
