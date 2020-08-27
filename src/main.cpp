#include <iostream>
#include <armadillo>
#include <cmath>


using namespace std;
using namespace arma;

int main(int argc, char** argv)
{
  int n = atoi(argv[1]);

  vec x = linspace<mat>(0,1,n);

  vec f = zeros<mat>(n);
  for (int i = 0; i<n; ++i){
    f[i] = 100*exp(-10*x[i]);
  }

  return 0;
}
