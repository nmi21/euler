/*
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

--

*/

#include <iostream>
#include <string>
#include <math.h>


bool is_palindrome(const int& n) {
    // Convert to a string
    std::string original_str = std::to_string(n);

    // Create a new string and add elements from original_str in reverse order
    std::string reverse_str = "";
    for (int i = original_str.size() - 1; i >= 0; --i) {
        reverse_str += original_str[i];
    }

    // Compare the two strings
    return (original_str == reverse_str);
}

int main() {

    // 3 digit numbers will start at 999 and work down through 100
    int upper_limit = 999;
    int lower_limit = 100;

    int highest_prod = 0;
    // Start at high numbers and work down
    for (int i = upper_limit; i >= lower_limit; --i) {
        for (int j = i; i >= lower_limit; --j) {
            
            int prod = i * j;

            // if product is less than current highest prod, terminate this search loop
            if (prod < highest_prod) {
                break;
            }

            // Check if palindrome
            if (is_palindrome(prod)) {
                // Replace highest_prod whenever you can
                if (prod > highest_prod) {
                    highest_prod = prod;
                }
            }
        }
    }

    std::cout << "ans == " << highest_prod << std::endl;


    return 0;
}