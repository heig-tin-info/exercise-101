/**
 * Un affichage 7 segments est le suivant:
 *         a
 *        __
 *    f /   / b
 *      ---
 *  e / g / c
 *    ---
 *     d
 *
 * Chaque segment est représenté par un numéro de bit. Par
 * exemple le nombre 5 est représenté par le nombre binaire:
 * 0b01101101
 *
 * L'etat de l'afficheur est donné par la variable `digit`.
 * Pour une valeur donnée, afficher la valeur 7 segments
 */

#include <stdbool.h>

int main(int argc, char* argv[]) {
    if (argc < 2) return 1;

    int value = atoi(argv[1]);

    bool a;
    bool b;
    bool c;
    bool d;
    bool e;
    bool f;
    bool g;


    if (a)
        printf("---\n");
    else
        printf("\n");

    if (f)
        printf("/   ");
    else
        printf("    ");

    if (b)
        printf("/\n");
    else
        printf("\n");

    if (g)
        printf("---\n");
    else
        printf("\n");

    if (e)
        printf("/   ");
    else
        printf("    ");

    if (c)
        printf("/\n");
    else
        printf("\n");

    if (d)
        printf("---\n");
    else
        printf("\n");
}
