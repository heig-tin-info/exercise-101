/**
 * Écrire un programme qui compte le nombre de voyelles
 * passées dans une chaîne de caractère passée sur `stdin`
 *
 * et affiche le nombre à l'écran.
 */

int main(void) {
    char buffer[1024];

    if (scanf("%s", &buffer) == 0) {
        return 2; // Erreur, aucune chaîne capturée :(
    }

    // Ici vous devez faire une boucle `while` tant que le caractère du buffer
    // n'est pas égal à `\0`.

    return 0;
}
