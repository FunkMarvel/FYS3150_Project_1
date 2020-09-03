#include <iostream>
#include "functions.h"

using namespace std;

int main(int argc, char** argv)
{
  int N = atoi(argv[1]);            // Step count
  double h = 1.0/(N+1);             // Step length

  // Performing general algorithm with benchmark.
  general_main(N,h);

  // Performing special algorithm with benchmark.
  special_main(N,h);

  // Solving with LU decomposition with benchmark.
  LU_main(N,h);  

  return 0;
}
