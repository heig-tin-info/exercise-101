/**
 * Faire un programme qui écrit les lettres de 'a' à 'z' à l'écran
 * en utilisant une boucle `for`
 *
 * Les lettres seront séparées par une espace.
 */
#include <stdio.h>

int main(void) {
    for(char c = 'a'; c <= 'z'; c++) {
        printf("%c ", c);
    }
}
