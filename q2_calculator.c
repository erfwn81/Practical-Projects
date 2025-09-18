/*
 * Erfan Mirzaee HW1 Q2
 * Simple Calculator Program
 * Does add, subtract, multiply, divide
 * Then evaluates: ((x + y + z) * x) / ((z - y - x) * y)
 */

#include <stdio.h>

// add three numbers
int add(int x, int y, int z) {
    return x + y + z;
}

// subtract: (z - y - x)
int subtract(int x, int y, int z) {
    return z - y - x;
}

// multiply two numbers
int multiply(int a, int b) {
    return a * b;
}

// divide two numbers (make sure denominator != 0)
double divide(double a, double b) {
    return a / b;
}

int main(void) {
    // example numbers
    int x = 2, y = 3, z = 10;

    // do the math step by step
    int sum = add(x, y, z);                  // (x + y + z)
    int top = multiply(sum, x);              // numerator = (x + y + z) * x
    int sub = subtract(x, y, z);             // (z - y - x)
    int bottom = multiply(sub, y);           // denominator = (z - y - x) * y

    // check if denominator is zero before dividing
    if (bottom == 0) {
        printf("Error: cannot divide by zero.\n");
        return 1; // stop program
    }

    // final division
    double result = divide(top, bottom);

    // show result
    printf("For x=%d, y=%d, z=%d, result of expression = %.6f\n", x, y, z, result);

    return 0;
}

