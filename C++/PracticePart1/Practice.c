#include <stdio.h>
#include "./src/Calculator.h"

int add(int op1, int op2);

int main(void)
{
    printf("Lets have a look on how it will work using VS Code");
    int result = add(3,5);

    printf("3 + 5 is: %i", result);
    return 0;
}
