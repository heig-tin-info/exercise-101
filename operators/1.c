/**
 * L'alarme du réacteur nucléaire doit retentir si
 * l'une des 4 pompes est en défaut. L'état
 * des pompes est donné par les variables globales.
 *
 * Le programme doit afficher "Alaaaaaarme !!" dans le cas ou
 * une alarme se produit sinon "Ouf, nous sommes encore en vie !"
 * 
 * écrire le programme minimal effectuant ce test.
 * 
 * Les valeurs de l'état des pompes ne doit pas être modifié.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(int argc, char *argv[]) {
    if (argc < 4) return 1;
    bool alarm_pump1 = (bool)atoi(argv[1]);
    bool alarm_pump2 = (bool)atoi(argv[2]);
    bool alarm_pump3 = (bool)atoi(argv[3]);
    bool alarm_pump4 = (bool)atoi(argv[4]);    

    if (alarm_pump1 || alarm_pump2 || alarm_pump3 || alarm_pump4)
        printf("Alaaaaaarme !!\n");
    else
        printf("Ouf, nous sommes encore en vie !\n");
}
