#include <iostream>
#include <armadillo>
#include <cmath>
#include "functions.h"
#include "time.h"

using namespace std;
using namespace arma;

void LU_main(int N, double h, vec& u_anal, vec& x)
{
  mat A = zeros<mat>(N,N);          // Matrix to use with LU decomposition
  mat L,U;                          // Matrices to store LU decomposition
  vec b_twiddle = zeros<vec>(N);    // Vector for function value (times h^2)

  // Generating values for input function
  for (int i = 0; i<N; ++i){
    b_twiddle[i] = h*h*100*exp(-10*x[i]);
  }

  // Generate matrix values to use with LU decomposition
  A(0,0) = 2;
  A(0,1) = -1;
  A(N-1,N-1) = 2;
  A(N-1,N-2) = -1;
  for (int i = 1; i<N-1; ++i){
    A(i,i-1) = -1;
    A(i,i) = 2;
    A(i,i+1) = -1;
  }

  // Declaring variables for CPU time measurement
  clock_t start, finish;

  // Start of general algorithm
  start = clock();

  // LU decomposition with armadillo
  lu(L,U,A);

  // Solving resulting equation sets
  vec y = solve(U,b_twiddle);
  vec u = solve(L,y);

  // General algorithm finished
  finish = clock();

  // Print time spent
  double LU_cputime = ( double(finish - start)/CLOCKS_PER_SEC );
  cout << "Solving with LU decomposition took " << LU_cputime << " seconds to finish."
       << endl;

  // Calculate maximum of log10 of relative error
  double eps_LU = find_relative_error(u,u_anal,N);
  cout << "Maximum (log10 of) relative error with the LU decomposition solver with " << N
       << " steps: " << eps_LU << endl;
}
