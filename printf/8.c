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

    printf("a + c =  ...\n", a + c);
    printf("x + c = ...\n", x + c);
    printf("dx + x = ...\n", dx + x);
    printf("((int) dx) + ax =  ...\n", ((int) dx) + ax);
    printf("a + x = ...\n", a + x);
    printf("s + b =  ...\n", s + b);
    printf("ax + b = ...\n", ax + b);
    printf("s + c =  ...\n", s + c);
    printf("ax + c = ...\n", ax + c);
    printf("ax + ux = ...\n", ax + ux);

    return 0;
}