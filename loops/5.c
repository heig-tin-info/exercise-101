/**
 * Crible d'Eratostène.
 */
#include <stdio.h>

int main() {
    int table[100];

    // Remplire la table avec les nombres de 1 à 100
    for (int i = 0; i < 100; i++) {
        table[i] = i + 1;
    }

    // Remplacer tous les nombres divisibles par `i` par `-1`
    for (int i = 0; i < 100; i++) {
        for (int divisor = 2; divisor <= 10; divisor++) {
            if (table[i] % divisor == 0 && table[i] != divisor) table[i] = -1;
        }
    }

    // Afficher les nombres qui ne sont pas `-1`
    for (int i = 0; i < 100; i++) {
        if (table[i] > 0)
            printf("%d est un nombre premier\n", table[i]);
    }
}
