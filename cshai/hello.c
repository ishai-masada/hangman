#include "stdio.h"

int main(int argc, char *argv[])
{
    if (argc == 1) {
        // ask for name
        printf("What is your name? ");
        char name[50];
        scanf("%s", name);
        printf("hello, %s\n", name);
    } else {
        // names were provided
        for (int i = 1; i < argc; i++) {
            printf("hello, %s\n", argv[i]);
        }
    }

    return 0;
}
