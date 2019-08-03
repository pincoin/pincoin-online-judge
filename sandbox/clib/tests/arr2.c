#include <stdio.h>
#include <stdlib.h>

#define MAX 60000000

int main(int argc, char *argv[]) {
    int *a = (int *)malloc(sizeof(int) * MAX);

    for (int i = 0; i < MAX; i++) {
        *(a+i) = i;
    }

    printf("%d %ld\n", *(a+MAX-1), sizeof(a));

    return 0;
}
