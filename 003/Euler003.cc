/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

--
Go through all prime numbers from 1 to sqrt(N) and see if they divide out
*/

#include <math.h>
#include <iostream>

bool is_prime(const int& n) {
    // Deal with numbers that are too small    
    if (n < 2) {
        return false;
    }

    if (n == 2) {
        return true;
    }

    // Deal with numbers that are even
    if (n % 2 == 0) { 
        return false;
    }

    // Determine if odd numbers can divide
    for (int i = 3; i*i <= n; i += 2) {
        if (n % i == 0) {
            return false;
        } 
    }

    return true;
}

int main() {

    int64_t N = 600851475143; 
    int largest_prime;

    for (uint64_t i = 1; i*i <= N; ++i) {
        if (is_prime(i) & (N % i == 0)) {
            largest_prime = i;
        }
    }

    std::cout << "ans == " << largest_prime << std::endl;

    return 0;
}