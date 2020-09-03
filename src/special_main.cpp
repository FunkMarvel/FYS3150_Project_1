#include <iostream>
#include <armadillo>
#include <cmath>
#include "functions.h"
#include "time.h"

using namespace std;
using namespace arma;

void special_main(int N, double h) {
  vec u = zeros<vec>(N);                         // Vector for numerical solution
  vec b_twiddle = zeros<vec>(N);
  vec b_recip = zeros<vec>(N);
  vec u_anal = zeros<vec>(N);
  //mat A = zeros<mat>(N,N);          // Matrix to use with LU decomposition

  // scoping for temporary variables:
  {
    // Generating values for input function
    vec x = linspace<vec>(0,1,N);     // temp Vector for x-values.
    for (int i = 0; i<N; ++i){
      b_twiddle[i] = h*h*100*exp(-10*x[i]);
    }
    // Generating values for analytic solution
    for (int i=0; i<N; ++i){
      u_anal[i] = 1 - (1 - exp(-10))*x[i] - exp(-10*x[i]);
    }
  }

  // Calculating 1/b where b is the diagonal elements.
  for (int i = 1; i < N+1; ++i) {
    b_recip[i-1] = i/(i + 1.0);
  }

  // Declaring variables for CPU time measurement
  clock_t start, finish;

  // Start of special algorithm
  start = clock();

  special_forward(b_recip, b_twiddle, N);
  special_backward(b_recip, b_twiddle, u, N);

  // Special algorithm finished
  finish = clock();

  // Print time spent
  double special_cputime = ( double(finish - start)/CLOCKS_PER_SEC );
  cout << "Special algorithm took " << special_cputime << " seconds to finish."
       << endl;

  // Calculate maximum of log10 of relative error
  double eps_special = find_relative_error(u,u_anal,N);
  cout << "Maximum (log10 of) relative error in special algorithm with " << N
       << " steps: " << eps_special << endl;
}
