/*
There are some prime values, p, for which there exists a positive integer, n, such that the expression n^3 + p*n^2
is a perfect cube.

For example, when
p = 19,
8^3 + 19*8^2 = 12^3.

What is perhaps most surprising is that for each prime with this property the value of n is unique, and there are only
four such primes below one-hundred.

How many primes below one million have this remarkable property?

--
We know:
n + p = x^3 / n^2
thus x^3 / n^2 must be an integer
and therefore n^2 must be a factor of x^3

Other constraints
p < 1,000,000
n < x

Forms of the equation:
n^3 + n^2 * p = x^3
p = (x^3 / n^2) - n
p = (x^3 - n^3) / n^2

Factor x^3 - n^3:
x^3 - n^3 = (x - n) * (x^2 + x*n + n^2)


This is interesting. Because it means that p = [(x - n) / n^2] * [(x^2 + x*n + n^2) / n^2]

Since the definition of a prime is that its only factors are 1 and itself, it must mean that:
[(x - n) / n^2] is a factor of p
[(x^2 + x*n + n^2) / n^2] is the other factor of p

Another way to look at the set of equations is:
n^3 + n^2 * p = x^3
n^3 * (1 + p/n) = x^3
n * (1 + p/n)^1/3 = x
From this... we know that if n and x are to be integers, then (1 + p/n)^1/3 must also be an integer
Rewrite it:
(1 + p/n) ^ 1/3
((n + p) / n) ^ 1/3     Let n+p = a^3; Let n = b^3
(a^3 / b^3) ^ 1/3
a^3 / b^3 is a perfect cube to make (1 + p/n)^1/3 an integer

using Let n+p = a^3; Let n = b^3 :
p = a^3 - n     Let n = b^3
p = a^3 - b^3       Again we can use that expansion!
p = (a - b) * (a^2 + ab + b^2)

Again we have a-b and a^2 + ab + b^2 as factors of a prime number!
One of them must be == 1, and that is going to be a-b because we know that the numbers are all postive integers
a - b = 1
a = b + 1

Interestingly, the a and b are consecutive numbers!

So we can just continue to check all the numbers until the difference is above the limit.

Then compare that against a list of primes below the limit and see how many overlap!
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

std::vector<bool> sieve_of_eratosthenes(const int& limit) {
    std::vector<bool> sieve(limit + 1, true);
    sieve[0] = false;
    sieve[1] = false;

    for (int i = 4; i < limit + 1; i += 2) {
        sieve[i] = false;
    }

    for (int i = 3; i < limit + 1; i += 2) {
        if (sieve[i]) {
            for (int j = 3 * i; j < limit + 1; j += 2*i) {
                sieve[j] = false;
            }
        }
    }

    return sieve;
}

std::vector<int> get_primes(const int& limit) {
    std::vector<bool> sieve = sieve_of_eratosthenes(limit);

    std::vector<int> primes;
    for (int i = 0; i < sieve.size(); ++i) {
        if (sieve[i]) {
            primes.push_back(i);
        }
    }

    return primes;
}

std::vector<int> get_cube_diffs(const int& limit) {
    std::vector<int> cube_diffs;

    int a = 2;
    while (true) {
        int diff = pow(a, 3) - pow(a - 1, 3);
        
        if (diff > limit) {
            break;
        }

        cube_diffs.push_back(diff);
        a += 1;
    }

    return cube_diffs;
}

int main() {

    int limit = 1000000;

    std::vector<int> c_diffs = get_cube_diffs(limit);
    std::vector<int> primes = get_primes(limit);
    // std::sort(primes.begin(), primes.end());

    int counter = 0;
    for (const auto & diff : c_diffs) {
        if (std::binary_search(primes.begin(), primes.end(), diff)) {
            counter += 1;
        }
    }

    int ans = counter;
    std::cout << "ans == " << ans << std::endl;

    return 0;
}
