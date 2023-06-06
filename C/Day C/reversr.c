#include <iostream>
#include <string>

using namespace std;

int main() {
  string str = "Hello, world!";
  for(int i = str.length() - 1; i >= 0; i--) {
    cout << str[i];
  }
  return 0;
}
