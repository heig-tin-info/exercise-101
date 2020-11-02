/**
 * Un affichage 7 segments est le suivant :
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
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    if (argc < 2) return 1;

    int value = atoi(argv[1]);
 
    // À vous de compléter ceci avec la logique nécessaire
    bool a = value & (1 << 0);
    bool b = value & (1 << 1);
    bool c = value & (1 << 2);
    bool d = value & (1 << 3);
    bool e = value & (1 << 4);
    bool f = value & (1 << 5);
    bool g = value & (1 << 6);

    // Pas besoin de toucher à ceci
    printf(a && f ? "┌" : " ");
    printf("%s", a ? "───" : "");
    printf("%s", a && b ? "┐" : " ");
    printf("\n");
    printf("%s", f ? "|   " : "    ");
    printf("%s\n", b ? "|" : "");
    if (e && f && g) printf("├");
    else if (e && f && !g) printf("│");
    else if (e && !f && g) printf("┌");
    else if (!e && f && g) printf("└"); 
    else printf(" ");
    printf("%s", g ? "───" : "   ");
    if (b && c && g) printf("┤");
    else if (b && c && !g) printf("│");
    else if (b && !c && g) printf("┘");
    else if (!b && c && g) printf("┐");
    printf("\n");
    printf("%s", e ? "|   " : "    ");
    printf("%s\n", c ? "|" : "");
    printf("%s", d && e ? "└" : " ");
    printf("%s", d ? "───" : "");
    printf("%s", c && d ? "┘" : " ");
}
