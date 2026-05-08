#include <iostream>
#include <vector>
#include <string>
#include <random>
#include <algorithm>
#include <map>

auto main() -> int {
    std::vector<std::string> s = {"🍒", "🍉", "🥭", "🔔", "⭐"};
    std::map<std::string, int> p = {{"🍒", 3}, {"🍉", 4}, {"🥭", 5}, {"🔔", 10}, {"⭐", 20}};
    int b = 100;
    std::random_device rd;
    std::mt19937 g(rd());
    std::uniform_int_distribution<> d(0, s.size() - 1);

    std::cout << "**********************\nWelcome to C++ Slots\nSymbols: 🍒 🍉 🥭 ⭐ 🔔\n**********************\n";

    while (b > 0) {
        std::cout << "Current balance: $" << b << "\nPlace your bet amount: ";
        std::string t;
        if (!(std::cin >> t)) break;
        if (!std::all_of(t.begin(), t.end(), ::isdigit)) {
            std::cout << "Enter a valid number\n";
            continue;
        }
        int v = std::stoi(t);
        if (v > b) {
            std::cout << "Insufficient amount\n";
            continue;
        }
        if (v <= 0) {
            std::cout << "Bet must be greater than 0\n";
            continue;
        }
        b -= v;
        std::vector<std::string> r(3);
        std::generate(r.begin(), r.end(), [&]() { return s[d(g)]; });
        std::cout << "*************\n" << r[0] << " | " << r[1] << " | " << r[2] << "\n*************\n";
        if (std::all_of(r.begin(), r.end(), [&](const std::string& x) { return x == r[0]; })) {
            int w = v * p[r[0]];
            std::cout << "You won $" << w << "\n";
            b += w;
        } else {
            std::cout << "Sorry you lose this round\n";
        }
    }
    return 0;
}
