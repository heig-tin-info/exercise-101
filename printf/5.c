/**
 * Écrire un programme qui écrit la valeur décimales des variables déclarées
 * sur l'écran, espacés par des tabulations `\t`.
 *
 */
#include <stdio.h>

int foo = 23;
float bar = 3.1415;
double baz = 6.28;
char qux = 'c';

int main(void) {
    printf("%d\t%f\t%lf\t%d", foo, bar, baz, (int)qux);
    return 0;
}
