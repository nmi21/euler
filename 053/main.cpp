#include "../../cpp_book/std_lib_facilities.h"

uint64_t factorial(int n) {
    if (n == 0) {
        return 1;
    }
    return n * factorial(n - 1);
}

uint64_t comb(int n, int r) {
    return factorial(n) / (factorial(r) * factorial(n - r));
}


int main() {

    int threshold = 1000000;
    int s = 0;
    for (int n = 23; n <= 100; n++) {
        cout << "Checking " << n << endl;
        // for (int r = 0; r <= n; r++) {
        //     if (comb(n, r) > threshold) {
        //         s += n - 2*r + 1;
        //         break;
        //     }
        // }
        cout << factorial(n) << endl;
    }

    cout << endl << s << endl;
}