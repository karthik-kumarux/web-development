#include <stdio.h>
#include <string.h>

int isPalindrome(char str[], int start, int end) {
    if (start >= end) {
        return 1;  // Base case: If indices cross, it's a palindrome
    }
    if (str[start] != str[end]) {
        return 0;  // If mismatch found, it's not a palindrome
    }
    return isPalindrome(str, start + 1, end - 1);  // Recursive check for next characters
}

int main() {
    char str[100];

    printf("Enter a string: ");
    scanf("%s", str);  // Takes input (ignores spaces)

    int length = strlen(str);
    
    if (isPalindrome(str, 0, length - 1)) {
        printf("\"%s\" is a palindrome.\n", str);
    } else {
        printf("\"%s\" is not a palindrome.\n", str);
    }

    return 0;
}
