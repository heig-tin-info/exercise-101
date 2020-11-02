#include <stdio.h>

int main()
{
    int a = 125, b = 12345;
    long ax = 1234567890;
    short s = 4043;
    float x = 2.13459;
    double dx = 1.1415927;
    char c = 'W';
    unsigned long ux = 2541567890;

    printf("a + c = %d\n", a + c); // e.g. 123
    printf("x + c = %.2f\n", x + c); // e.g. 1.23 (2 décimales)
    printf("dx + x = %+08.2f\n", dx + x); // e.g. +0001.23 (8 digits, 2 décimales)
    printf("((int) dx) + ax = %ld\n", ((int) dx) + ax); // e.g 123
    printf("a + s = 0x%04x\n", a + s); // e.g. 0x1234 (hexadécimal)
    printf("s + b = 0%o\n", s + b); // e.g. 0123 (octal avec un zéro devant)
    printf("ax * ux = %ld\n", ax * ux); // e.g 123 (long int)

    return 0;
}
