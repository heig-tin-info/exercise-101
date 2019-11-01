/**
 * Complétez les chaînes de caractères suivantes pour répondre aux
 * questions.
 *
 * /!\ Double échappez \n comme ceci \\n pour qu'il apparaisse à l'écran
 * convenablement.
 */
#include <stdio.h>

int i = 7, i1, i2, i3;
float f = 7.0f, f1;


int main(void) {
    // Exemple: Que doit être la sortie sur l'écran de:
    // printf("hello %d\n", 42)
    char q0[] = "hello 42\\n";

    // Que doit être la sortie sur l'écran de:
    // printf("z%dz%6dz\n", i, i);
    char q1[] = "";

    // Que doit être la sortie sur l'écran de
    // printf("%d%f\n", i, f);
    char q2[] = "";

    // Que doit être la sortie sur l'écran de
    // printf("%o,%x,%X\n", 30, 30, 30);
    char q3[] = "";

    // Que doit être la sortie sur l'écran de
    // printf("%d%1.0f\n", i, f);
    char q4[] = "";


    // Affichage pour les tests
    printf("Q1. '%s'\nQ2. '%s'\nQ3. '%s'\nQ4. '%s'\n", q1, q2, q3, q4);
}
