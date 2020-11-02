/**
 * Écrire un programme qui écrit à l'écran le cube de la variable foo
 * sans utiliser l'opérateur de multiplication
 */

#include <math.h>
#include <stdio.h>

double foo = 5;

int main() {
    printf("%d", (int)pow(foo, 3));
}
