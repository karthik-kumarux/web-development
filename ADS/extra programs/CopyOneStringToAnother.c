#include <stdio.h>

void copyString(char source[], char destination[], int index) {
    if (source[index] == '\0') { 
        destination[index] = '\0';  // Base case: End of string
        return;
    }
    destination[index] = source[index];  // Copy character
    copyString(source, destination, index + 1);  // Recursive call for next character
}

int main() {
    char source[100], destination[100];

    printf("Enter a string: ");
    scanf("%s", source);

    copyString(source, destination, 0);

    printf("Copied string: %s\n", destination);

    return 0;
}
