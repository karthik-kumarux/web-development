#include <stdio.h>

int sum(int n) {
    if (n == 1) {
        return 1;  // Base case: sum of 1 is 1
    }
    return n + sum(n - 1);  // Recursive case: n + sum of previous numbers
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);

    printf("Sum from 1 to %d is: %d\n", n, sum(n));
    return 0;
}
