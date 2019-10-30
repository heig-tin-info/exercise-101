/**
 * Écrire un programme qui écrit à l'écran le cube de la variable foo
 */

#include <math.h>
#include <stdio.h>

double foo = 5;

int main(void) {
    printf("%d", (int)pow(foo, 3));
    return 0;
}
