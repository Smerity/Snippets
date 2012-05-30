// http://xn13.com/xn13.c
// Ben Olmstead -- author of Malbolge
#include<stdio.h>
int/* XN13 */main
(){int i=1,j;for(
;i>0;puts(""))for
(j=i,i=2*i^i/2;j;
j/=2)putchar(" X"
[j&1]);return 0;}
