/**
 * Écrire un programme qui affiche, votre nom votre date de naissance et votre numéro de téléphone.
 *
 * Chacune des valeurs doit être issue d'une variable et les valeurs doivent être
 * affichées en utilisant le bon format.
 *
 * Votre numéro de téléphone doit respecter le format E.123 (e.g. +41 791234567)
 *
 * Remplacer les points de suspension par la structure idoine.
 */
#include <stdio.h>
#include <stdint.h>

int main(void) {
    char birth_year = 51; // Format 00..99 for 00: 2000 and 99: 1999
    char full_name[] = "John Doe";
    int_least8_t country_code = 41;
    int64_t phone = 1234567;

    printf("Name:        %s\n", );
    printf("Birth Year:  %d\n", );
    printf("Mobile:      +%d %ld\n", );

    return 0;
}
