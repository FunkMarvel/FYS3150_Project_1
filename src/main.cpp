#include <iostream>
#include <armadillo>
#include <cmath>
#include "functions.h"
#include "time.h"

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
  double h = 1.0/(N+1);

  for (int i = 0; i<N; ++i){
    b_twiddle[i] = h*h*100*exp(-10*x[i]);
  }

  vec u_anal = zeros<vec>(N);
  for (int i=0; i<N; ++i){
    u_anal[i] = 1 - (1 - exp(-10))*x[i] - exp(-10*x[i]);
  }

  //declaring variables for CPU time measurement
  clock_t start, finish;

  //start of general algorithm
  start = clock();

  //Forward part call
  general_forward(a, b, c, b_twiddle, N);

  //Backward part call
  general_backward(b, b_twiddle, c, u, N);

  //general algorithm finished
  finish = clock();
  double general_cputime = ( double(finish - start)/CLOCKS_PER_SEC );
  cout << "General algorithm took " << general_cputime << " seconds to finish."
       << endl;

  return 0;
}
