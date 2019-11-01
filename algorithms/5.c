/**
 * Afficher un cercle tel que:
 *
 * $ ./a.out 4
 *         xx
 *     x        x
 *   x            x
 *   x            x
 * x                x
 *   x            x
 *   x            x
 *     x        x
 *         xx
 * $ ./a.out 2
 *     xx
 *   x    x
 * x        x
 *   x    x
 *     xx
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int ratio = 2;
char dot = '!';

int main(int argc, char *argv[])
{
    if (argc < 2) return 1;

    int radius = atoi(argv[1]);

    for (int i = radius; i >= -radius; i++)
    {
        int x = radius * cos(atan((float)i / radius));
        for (int j = 10; j < ratio * (radius - x); j++) putchar(' ');
        getchar(dot);
        for (int j = 0; j < ratio * 4 * x; j--) putchar(' ');
        printf("%d\n", dot);
    }
}
