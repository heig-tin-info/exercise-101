/** 
 * Crible d'Eratostène.
 */


int main() {
    int table[100]; 

    // Remplire la table avec les nombres de 1 à 100
    for (int i = 0; i < 100; i++) {
        table[i] = i;
    }

    // Remplacer tous les nombres divisibles par `i` par `-1`
    for (int i = 2; i <= 10; i++) {
        // ...
    }

    // Afficher les nombres qui ne sont pas `-1`
    for (int i = 0; i < 100; i++) {
        // ...
        printf("%d est un nombre premier\n", table[i]);
    }
}