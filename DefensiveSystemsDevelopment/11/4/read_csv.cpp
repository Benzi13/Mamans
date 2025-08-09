#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cctype>
#include <vector>

bool isNumber(const std::string& s) {
    if (s.empty()) return false;
    std::istringstream iss(s);
    double d;
    char c;
    return (iss >> d) && !(iss >> c); // Checks if the whole string is a valid number
}

int main() {
    std::ifstream file("C:\\Users\\Raz\\Desktop\\Programing\\Mamans\\DefensiveSystemsDevelopment\\11\\4\\example_data\\example_input.csv");
    std::string line;
    std::vector<double> columnSums;

    if (file.is_open()) {
        while (std::getline(file, line)) {
            std::stringstream ss(line);
            std::string item;
            double sum = 0.0;
            size_t colIdx = 0;

            while (std::getline(ss, item, ',')) {
                if (columnSums.size() <= colIdx) {
                    columnSums.push_back(0.0);
                }
                if (isNumber(item)) {
                    double val = std::stod(item);
                    sum += val;
                    columnSums[colIdx] += val;
                }
                colIdx++;
            }
            std::cout << "Total of line: " << sum << std::endl;
        }
        file.close();

        std::cout << "Sums of columns:\n ";
        for (size_t i = 0; i < columnSums.size(); ++i) {
            std::cout << columnSums[i];
            if (i < columnSums.size() - 1) std::cout << " ";
        }
        std::cout << std::endl;
    } else {
        std::cout << "Unable to open file" << std::endl;
    }

    return 0;
}