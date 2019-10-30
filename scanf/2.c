/**
 * Écrire un programme qui lit 2 entiers sur `stdin` et affiche la somme de ces
 * nombres à l'écran. N'utilisez qu'une seule fois `scanf`.
 * 
 * Le programme retourne 1 en cas d'erreur
 */
#include <stdio.h>

int main(void) {
    int a, b;
    if (scanf("%d %d", &a, &b) != 2) {
        return 1;
    }
    printf("%d\n", a + b);
    return 0;
}