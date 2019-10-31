/**
 * Écrire un programme qui affiche tous les arguments passés.
 *
 * Exemple:
 *
 *    $ ./a.out foo bar baz qux 42
 *    1. foo
 *    2. bar
 *    3. baz
 *    4. qux
 *    5. 42
 *
 * Indice: Utilisez une boucle...
 */

#include <stdio.h>
int main(int argc, char* argv[]) {
    for (int i = 0; i < argc; i++) {
        printf("%d. %s\n", i, argv[i]);
    }
}
