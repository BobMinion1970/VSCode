#include <stdio.h>
#include "src/Calculator.h"

int main(void)
{
    int result = 0;
    int op1;
    int op2;
    printf("Lets have a look on how it will work using VS Code");
    printf("\nOperand 1: ");
    scanf("%d", &op1);
    printf("\nOperand 2: ");
    scanf("%d", &op2);
    result = add(op1,op2);
    printf("%d + %d is: %d\n", op1, op2, result);
    
    result = sub(op1, op2);
    printf("%d + %d is: %d\n", op1, op2, result);
    
    return 0;

}
