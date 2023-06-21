/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
*/

#include <iostream>
#include <vector>

std::vector<bool> sieve_of_eratosthenes(int limit) {
    std::vector<bool> sieve;
    for (int i = 0; i <= limit; ++i) {
        sieve.push_back(true);
    }

    sieve[0] = false;
    sieve[1] = false;

    for (int i = 4; i <= limit; i += 2) {
        sieve[i] = false;
    }

    for (int i = 3; i <= limit; i += 2) {
        if (sieve[i]) {
            for (int j = 3*i; j <= limit; j += 2*i) {
                sieve[j] = false;
            }
        }
    }

    return sieve;
}

int main() {

    int limit = 2000000;
    std::vector<bool> primes_sieve = sieve_of_eratosthenes(limit);
    uint64_t sum = 0;
    for (int i = 0; i < primes_sieve.size(); ++i) {
        if (primes_sieve[i]) {
            sum += i;
        }
    }

    std::cout << "ans == " << sum << std::endl;

    return 0;
}