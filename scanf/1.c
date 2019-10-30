/**
 * Écrire un programme qui lit sur `stdin` un nombre entier signé et affiche
 * son contenu sur `stdout` et retourne 1 en cas d'erreur
 */

#include <stdio.h>

int main(void) {
    int value = -1;
    if (scanf("%d", &value) != 1) {
        return 1;
    }
    printf("%d\n", value);
    return 0;
}