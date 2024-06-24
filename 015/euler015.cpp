#include <iostream> 

uint64_t find_path(int x, int y) {
    if ((x == 0) || (y == 0)) {
        return 1;
    }

    return find_path(x - 1, y) + find_path(x, y - 1);
}

int main() {

    int end = 20;

    std::cout << "test" << std::endl;

    for (int i = 1; i < end + 1; ++i) {
        std::cout << "{" << i << "}: ";
        std::cout << find_path(i, i) << std::endl;
    }

    // Notice that at a 17x17 grid, we have a negative number, which means that our container for find_path is too small
    //      thus, make find_path output a 64 bit integer

    // Even then, this method is still too slow
    //      thus, implement dynamic programming

    return 0;
}