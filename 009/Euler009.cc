/*
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
*/

#include <iostream>

int main() {
    int target = 1000;
    for (int a = 1; a < target; ++a) {
        for (int b = 1; b < target; ++b) {
            int c = target - a - b;
            if (a*a + b*b == c*c) {
                int prod = a * b * c;
                std::cout << "ans == " << prod << std::endl;
                return 0;   
            }
        }
    }
}