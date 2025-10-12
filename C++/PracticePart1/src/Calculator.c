#include "Calculator.h"

int add(int op1, int op2)
{
    int retval = 0;
    retval = op1 + op2;
    return retval; 
}

int sub(int op1, int op2)
{
    int retval = 0;
    retval = op1 - op2;
    return retval;
}

int mult(int op1, int op2)
{
    int retval = 0;
    retval = op1 * op2;
    return retval;
}

int div(int op1, int op2)
{
    int retval = 0;
    if(op2 != 0)
        retval = (int)(op1 / op2);
    
    return retval; 
}