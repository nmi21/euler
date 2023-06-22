/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
*/

#include <iostream>

bool is_prime(const int& n) {
    if (n < 2) {
        return false;
    }

    if (n == 2) {
        return true;
    }

    if (n % 2 == 0) {
        return false;
    }

    for (int i = 3; i*i <= n; i += 2) {
        if (n % i == 0) {
            return false;
        }
    }

    return true;
}

int main() {

    int limit = 10001;
    int prime_counter = 0;
    int i = 0;
    while (prime_counter <= limit) {
        ++i;

        if (is_prime(i)) {
            prime_counter += 1;
        }
    }

    std::cout << "ans == " << i << std::endl;

    return 0;
}