/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

-- 
*/

#include <iostream>

int main() {

    // start with 1
    // see if all numbers 1:20 can divide into it (start backwards)
    // if yes, exit and you found number
    // if no, increment by 1 and try again

    int64_t i = 0;
    bool searching = true;
    while (searching) {
        ++i;

        // Check over all values from 20:1 to make sure that they are divisors
        for (int j = 20; j > 0; --j) {
            if (i % j != 0) {
                break;
            }

            // If you reach j = 1, it's the end and you've found your number
            if (j == 1) {
                searching = false;
            }
        }

    }

    std::cout << "ans == " << i << std::endl;

    return 0;
}