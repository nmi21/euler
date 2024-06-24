/*
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

----

Method:
- may be able to do some clever method where you determine the max in each row, col, and diag dynamically, but the
set is small enough that brute force should be ok
*/

// Need to extract the number block

#include <iostream>
#include <string>
#include <vector>
#include <fstream>



std::vector<std::string> get_file_lines(std::string file_name) {
    // start an input file stream
    std::ifstream ifs {file_name};
    
    std::vector<std::string> s_vec;
    std::string s;
    while (std::getline(ifs, s)) {
        s_vec.push_back(s);
    }

    return s_vec;
}



int main() {

    std::string file = "number_block.txt";

    std::vector<std::string> block_lines = get_file_lines(file);

    return 0;
}