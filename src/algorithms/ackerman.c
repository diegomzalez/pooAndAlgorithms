#include <stdio.h>

int A(m, n) {
  if (m == 0){
    return n + 1;
  }
  if (m > 0 && n == 0){
    return A(m - 1, 1);
  }
  if (m > 0 && n > 0){
    return A(m - 1, A(m, n - 1));
  }
}
int main() {
  printf(A(3, 0));
}