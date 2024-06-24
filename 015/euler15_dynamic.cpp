#include <iostream>
#include <vector>

int main() {

    int grid_x = 20;
    int grid_y = 20;
    
    std::vector<std::vector<long long>> full_grid(grid_x + 1, std::vector<long long>(grid_y + 1, 0));

    for (int i = 0; i <= grid_x; i++) {
        for (int j = 0; j <= grid_y; j++) {
            if (i == 0 || j == 0) {
                // ensure that all of the grid locations on left and top are 1
                full_grid[i][j] = 1;
            } else {
                // add the left and top adjacent cells
                full_grid[i][j] = full_grid[i-1][j] + full_grid[i][j-1];
            }
        }
    }

    std::cout << full_grid[grid_x][grid_y] << std::endl;

    return 0;
}