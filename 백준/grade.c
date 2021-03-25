#include <stdio.h>

int main(void){

    int a,b;
    scanf("%d %d", &a, &b);

    if(a!=0){
        if(b-45<0){
            b = b + 60 - 45;
            a = a - 1;
        }
        else{
            b = b - 45;
        }
    }

    else{
        if(b-45<0){
            b = b + 60 - 45;
            a = a - 1 + 24;
        }
        else{
            b = b - 45;
        }        
    }

    printf("%d %d\n",a,b);

    return 0;
}