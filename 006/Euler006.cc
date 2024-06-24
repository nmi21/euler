/*
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

--
*/

#include <iostream>

int main() {

    int limit = 100;

    int sum_of_squares = 0;
    int square_of_sums = 0;
    for (int i = 1; i <= limit; ++i) {
        sum_of_squares += i * i;
        square_of_sums += i;
    }
    square_of_sums *= square_of_sums;
    
    int ans = square_of_sums - sum_of_squares;

    std::cout << "ans == " << ans << std::endl;

    return 0;
}