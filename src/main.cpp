#include <iostream>
#include <armadillo>
#include <cmath>


using namespace std;
using namespace arma;

int main(int argc, char** argv)
{

  int N = atoi(argv[1]);

  vec x = linspace<vec>(0,1,N);

  vec f = zeros<vec>(N);
  for (int i = 0; i<N; ++i){
    f[i] = 100*exp(-10*x[i]);
  }
  cout << f << endl;

  return 0;
}
