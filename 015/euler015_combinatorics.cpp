// This problem can be thought of in terms of combinatorics

#include <iostream>
#include <

int main() {

    // A 20x20 grid means that we must make 20x moves down among the columns and 20x right among the rows
    // In nCr, it should be (grid total down + right moves) Choose (total moves required to get to the end)

    for (int i = 1; i <= 20; ++i) {
        std::cout << i + i << " choose " << i << " == ";
        std::cout << combination(i + i, i) << std::endl;
    }

    return 0;
}