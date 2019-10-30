/**
 * Écrire un programme qui affiche la moyenne de tous les
 * nombres reçu sur `stdin`. Les nombres sont des entiers, la moyenne 
 * est un `double` affiché avec 4 décimales.
 * 
 * Exemple: 
 *    $ echo "5 6 12 66 55 9 3" | ./a.out
 *    22.2857
 * 
 * Indice: 
 *    https://stackoverflow.com/questions/8094702/how-use-eof-stdin-in-c
 */
#include <stdio.h>

int main(void) {
    float mean = 0;
    int number;
    int i = 0;
    while(!feof(stdin) && scanf("%d", &number)) {
        mean += number;
        i++;
    }
    printf("%.4f", mean / i);
}