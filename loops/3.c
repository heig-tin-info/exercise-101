/**
 * Faire un programme qui écrit les lettres de 'A' à 'F' à l'écran
 * en utilisant une boucle `while`
 *
 * Séparer chaque lettre par '-': A-B-C-D
 *
 */
#include <stdio.h>

int main(void) {
    char c = 'A';
    while(c < 'F') {
        printf("%c-", c++);
    }
    printf("%c", c);
}
