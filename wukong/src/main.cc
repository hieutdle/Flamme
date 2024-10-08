// main.cc
#include <iostream>
#include <pwd.h>
#include <unistd.h>
#include <repl.h>

int main() {
    // Get the current user's username
    const passwd *pw = getpwuid(getuid());
    const std::string userName = pw ? pw->pw_name : "User";

    // Welcome message
    std::cout << "Hello " << userName
            << "! This is the Wukong programming language!" << std::endl;
    std::cout << "Feel free to type in commands" << std::endl;

    // Start the REPL (Read-Eval-Print Loop)
    Start(std::cin, std::cout);

    return 0;
}
