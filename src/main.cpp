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
  vec b_twiddle = zeros<vec>(N);
  vec f_twiddle = zeros<vec>(N);
  double h = 1.0/(N+1);

  vec f = zeros<vec>(N);
  for (int i = 0; i<N; ++i){
    f[i] = h*h*100*exp(-10*x[i]);
  }

  vec u_anal = zeros<vec>(N);
  for (int i=0; i<N; ++i){
    u_anal[i] = 1 - (1 - exp(-10))*x[i] - exp(-10*x[i]);
  }


  //Forward part call
  general_forward(a,b,c,f,b_twiddle,f_twiddle,N);

  //Backward part call
  general_backward(b_twiddle,f_twiddle,c,u,N);

  cout << max(u-u_anal) << endl;
  return 0;
}
