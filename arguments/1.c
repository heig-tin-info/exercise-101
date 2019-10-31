/**
 * Écrire un programme qui affiche le nombre d'arguments passés à un programme,
 * ignorant le nom du programme.
 */
#include <stdio.h>

int main(int argc, char* argv[]) {
    printf("%d", argc - 1);
}
