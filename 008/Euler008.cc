/*
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this
product?
*/

#include <iostream>
#include <string>
#include <vector>
#include <fstream>

std::string extract_file_info(std::string filename) {
    // start an input filestream
    std::ifstream ifs {filename};

    // add all lines to a string out
    std::string s;
    std::string out = "";
    while (std::getline(ifs, s)) {
        out += s;
    }

    return out;
}

std::vector<int> convert_str_to_vector_integers(const std::string& input_string) {
    // convert n to a vector of char
    std::vector<char> v_char(input_string.begin(), input_string.end());

    // convert each char to an int
    std::vector<int> v_int;     // vecvtor of size v_char.size()
    for (auto c : v_char) {
        v_int.push_back(c - '0');
    }

    return v_int;
}

uint64_t get_max_product(const std::vector<int> v_int, const int& num_factors) {

    uint64_t max_product = 0;
    for (int i = 0; i < v_int.size() + 1 - num_factors; ++i) {
        uint64_t product = 1;
        for (int j = i; j < i + num_factors; ++j) {
            product *= v_int[j];
        }

        if (product > max_product) {
            max_product = product;
        }
    }

    return max_product;
}

int main() {

    std::string file = "number_block.txt";
    std::string out = extract_file_info(file);
    std::vector<int> vec_int = convert_str_to_vector_integers(out);

    uint64_t res;
    res = get_max_product(vec_int, 13);

    std::cout << "ans == " << res << std::endl;

    return 0;    
}