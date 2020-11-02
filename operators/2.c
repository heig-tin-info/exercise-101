/**
 * Le carrefour de la Bourdonette à Lausanne est composé
 * de quatre passages à niveau qui doivent tous être baissé si
 * un M1 passe dans un sens ou dans l'autre.
 * 
 * En cas de défaillance le programme doit retourner 1 sur son 
 * status de sortie, sinon 0.
 * 
 * Les valeurs de `crossing_x` ont vraies si les barrières sont fermées.
 */

#include <stdlib.h>
#include <stdbool.h>

int main(int argc, char *argv[]) {
    if (argc < 6) return 1;
    bool m1_to_flon = (bool)atoi(argv[1]);
    bool m1_to_renens = (bool)atoi(argv[2]);

    bool crossing_1 = (bool)atoi(argv[3]);
    bool crossing_2 = (bool)atoi(argv[4]);    
    bool crossing_3 = (bool)atoi(argv[5]);    
    bool crossing_4 = (bool)atoi(argv[6]);    

    return !((m1_to_flon || m1_to_renens) && (
        crossing_1 && crossing_2 &&
        crossing_3 && crossing_4
    ));
}
