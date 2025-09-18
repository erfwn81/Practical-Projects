// Erfan Mirzaee HW 1
/*
 * Simple Bookstore Inventory
 * User enters:
 *   positive number → add books
 *   negative number → remove books
 *   0 → quit
 */

#include <stdio.h>

int main(void) {
    long long inventory = 0;   // total books in store
    long long change;          // books to add or remove

    printf("=== Bookstore Inventory ===\n");
    printf("Enter number of books (+ to add, - to remove, 0 to quit)\n");

    while (1) {
        printf("\nChange in books: ");
        if (scanf("%lld", &change) != 1) {
            // if input is not a number
            printf("Invalid input! Please enter a whole number.\n");
            // clear bad input from buffer
            int c;
            while ((c = getchar()) != '\n' && c != EOF) { }
            continue; // ask again
        }

        if (change == 0) {
            // quit the program
            printf("Goodbye! Final inventory = %lld\n", inventory);
            break;
        }

        // update total books
        inventory += change;
        printf("Current inventory = %lld\n", inventory);
    }

    return 0;
}

