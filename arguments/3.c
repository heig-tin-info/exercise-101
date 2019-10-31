/**
 * Écrire un programme qui affiche le nombre le plus petit
 * de tous les arguments passés
 *
 * Exemple:
 *    $ ./a.out 5 6 12 66 55 9 3
 *    3
 */
#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

int main(int argc, char * argv[]) {
    int min = INT_MAX;
    for(int i = 1; i < argc; i++) {
        int num = atoi(argv[i]);
        if (num < min) {
            min = num;
        }
    }
    printf("%d\n", min);
}
