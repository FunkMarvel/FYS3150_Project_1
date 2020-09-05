#include <iostream>
#include <string>
#include "functions.h"

using namespace std;

int main(int argc, char** argv)
{
  int N = atoi(argv[1]);            // Step count
  double h = 1.0/(N+1);             // Step length
  vec u_anal = zeros<vec>(N);     // Vector for analytical solution.
  vec x = linspace<vec>(0,1,N);     // Vector for x-values.

  // Generating values for analytic solution
  for (int i=0; i<N; ++i){
    u_anal[i] = 1 - (1 - exp(-10))*x[i] - exp(-10*x[i]);
  }
  x.save("x" + std::to_string(N) + ".bin", raw_binary);
  u_anal.save("u_anal" + std::to_string(N) + ".bin", raw_binary);

  // Performing general algorithm with benchmark.
  general_main(N, h, u_anal, x);

  // Performing special algorithm with benchmark.
  special_main(N, h, u_anal, x);

  // Solving with LU decomposition with benchmark.
  // LU_main(N, h, u_anal, x);

  return 0;
}
