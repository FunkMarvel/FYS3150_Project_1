#include <iostream>
#include <armadillo>
#include <cmath>


using namespace std;
using namespace arma;

int main(int argc, char** argv)
{
<<<<<<< HEAD
  int N = atoi(argv[1]);
  vec x = linspace<vec>(0, 1, N);

  cout << x << N << endl;
=======
  int n = atoi(argv[1]);

  vec x = linspace<mat>(0,1,n);

  vec f = zeros<mat>(n);
  for (int i = 0; i<n; ++i){
    f[i] = 100*exp(-10*x[i]);
  }
>>>>>>> 834ee3c222ea880e11bcc78673f509b7c29951b0

  return 0;
}
