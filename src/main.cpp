#include <iostream>
#include <armadillo>
#include <cmath>
#include "functions.h"

using namespace std;
using namespace arma;

int main(int argc, char** argv)
{

  int N = atoi(argv[1]);

  vec x = linspace<vec>(0,1,N);     // vector for x-values.
  vec a(N-1); a.fill(-1);       // vector for lower diagonal.
  vec b(N); b.fill(2);      // vector for diagonal.
  vec c(N-1); c.fill(-1);       // vector for upper diagonal.
  vec u(N);     // vector for numerical solution

  vec f = zeros<vec>(N);
  for (int i = 0; i<N; ++i){
    f[i] = 100*exp(-10*x[i]);
  }

  double h = 1.0/(N+1);

  cout << decomp_and_forward_sub(a, b, c, x) << endl; // testing function call.

  return 0;
}
