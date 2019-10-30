/**
 * Écrire un programme qui écrit la valeur de la variable foo avec
 * les caractéristiques suivantes:
 *
 * - Nombres de chiffres après la virgule 2
 * - Nombre de 0 devant le nombre 5
 *
 * Exemple: 00042.12
 *
 */
#include <stdio.h>

int main(void) {
    double foo = 42.125;
    printf("%07.2f\n", foo);
    return 0;
}
