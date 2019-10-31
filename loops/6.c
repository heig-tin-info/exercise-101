/**
 * La variance d'un vecteur est exprimé par la formule:
 *
 * \frac{1}{N}\sum_{i=1}^N(x_i-\bar{x})^2
 * (pour voir la formule écrite en LaTeX,
 *  vous pouvez utiliser: http://asciimath.org/)
 *
 * Calculer la variance du vecteur `vector` ainsi que sa déviation sandard.
 * La déviation standard est la racine carrée de la variance.
 */
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

const double vector[] = {
        0.11287753, -1.41800865, -0.28742239,  1.4315401 ,  0.74161811,
        0.36927707,  0.71818015, -0.42339619,  0.54503514, -0.67521019,
       -1.64835054, -0.5153929 , -0.0316504 , -0.31190548, -0.05668296,
        0.41234759, -0.27132648,  1.58085108,  1.17373132, -0.39059919,
        0.86196864, -1.91823773, -1.09676847,  0.01725957, -1.00588137,
        0.51301277,  3.01472158, -0.19933366, -1.882705  , -1.71109975,
       -0.14310825,  0.39862776,  0.47156702,  0.54150885,  1.09541553,
       -0.54477589, -0.73013145,  0.9298162 ,  0.74739276,  0.07785218,
        0.10399891,  0.26177598,  0.09245265,  0.35428494, -0.6694547 ,
       -0.15330877, -1.22430161, -0.26334898,  0.34676887, -0.82322453,
       -0.51350341,  1.17084198,  0.26887039,  0.15875491,  0.24251008,
        0.13187222, -0.61840304,  0.57509332,  0.23404102,  1.50017417,
        0.23821361,  0.35381642,  2.29486467, -0.63547233, -0.8126199 ,
       -0.03322597, -1.87957423, -0.05760729, -1.34849371, -0.5564921 ,
        1.05271162,  0.21642101, -0.81727894,  1.11903583,  2.20244251,
       -2.12608167,  0.35405245,  0.6070081 , -0.2081714 , -0.54293567,
       -0.2811449 , -0.01360602, -1.01860471,  0.09202124, -0.20051699,
        0.1339523 ,  0.82320759, -0.76732586, -0.15642354,  0.59893962,
        0.34403227, -0.4571884 ,  0.98409856,  2.74618307,  0.59070315,
        0.38902092,  0.20204694,  1.47222261, -0.64290545, -2.85185781};

int main(void) {
    // Astuce pour connaître la longueur du vecteur `vector`:
    const size_t length = sizeof(vector)/sizeof(vector[0]);

    // Calcul de la moyenne du vecteur
    double mean = 0;
    for (int i = 0; i < length; i++) {
        mean += vector[i];// ...
    }
    mean /= length;

    printf("Moyenne: %.8f\n", mean);

    // Calcul de la variance
    double variance = 0;
    for (int i = 0; i < length; i++) {
        variance += pow(vector[i] - mean, 2); // ...
    }
    variance /= length;

    printf("Variance: %.8f\n", variance);

    // Calcul de la déviation standard
    double std = sqrt(variance);
    printf("Déviation standard: %.8f\n", std);
}
