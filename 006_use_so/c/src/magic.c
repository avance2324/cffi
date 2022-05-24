// magic.c
// Implementation of magic.
#include "magic.h"
int add(int a, int b)
{

    int c = a + b ;
    printf("add(%d, %d) ... \n", a, b) ;
    if (c > 2) {
        printf(" a + b > 2 \n");
    }
    else{
        printf(" a + b <= 2 \n");

    }
    do_print(c) ;
    do_print( glob_var_10 + 31 ) ;
    do_print( glob_var_20 + 98 ) ;
    return a+b+2;
}


