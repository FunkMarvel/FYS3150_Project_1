#include <iostream>
#include <armadillo>
#include <cmath>
#include "functions.h"
#include "time.h"

using namespace std;
using namespace arma;

int main(int argc, char** argv)
{

  int N = atoi(argv[1]);            // Step count
  vec x = linspace<vec>(0,1,N);     // Vector for x-values.
  vec a(N-1); a.fill(-1);           // Vector for lower diagonal.
  vec b(N); b.fill(2);              // Vector for diagonal.
  vec c(N-1); c.fill(-1);           // Vector for upper diagonal.
  vec u(N);                         // Vector for numerical solution
  double h = 1.0/(N+1);             // Step length
  mat A = zeros<mat>(N,N);          // Matrix to use with LU decomposition

  // Generating values for input function
  vec b_twiddle = zeros<vec>(N);
  for (int i = 0; i<N; ++i){
    b_twiddle[i] = h*h*100*exp(-10*x[i]);
  }

  // Generating values for analytic solution
  vec u_anal = zeros<vec>(N);
  for (int i=0; i<N; ++i){
    u_anal[i] = 1 - (1 - exp(-10))*x[i] - exp(-10*x[i]);
  }

  // Declaring variables for CPU time measurement
  clock_t start, finish;

  // Start of general algorithm
  start = clock();

  // General algorithm calls
  general_forward(a, b, c, b_twiddle, N);
  general_backward(b, b_twiddle, c, u, N);

  // General algorithm finished
  finish = clock();

  // Print time spent
  double general_cputime = ( double(finish - start)/CLOCKS_PER_SEC );
  cout << "General algorithm took " << general_cputime << " seconds to finish."
       << endl;

  // Calculate maximum of log10 of relative error
  double eps_general = find_relative_error(u,u_anal,N);
  cout << "Maximum (log10 of) relative error in general algorithm with " << N
       << " steps: " << eps_general << endl;

  // Generate matrix values to use with LU decomposition
  A[0,0] = 2;
  A[0,1] = -1;
  A[N-1,N-1] = 2;
  A[N-1,N-2] = -1;
  for (int i = 1; i<N-1; ++i){
    A[i,i-1] = -1;
    A[i,i] = 2;
    A[i, i+1] = -1;
  }

  cout << max(u-u_anal) << endl;

  vec b_recip = zeros<vec>(N); // array for 1/b.
  for (int i = 1; i < N+1; ++i) {
    b_recip[i-1] = i/(i + 1.0);
  }
  u.fill(0);

  for (int i = 0; i<N; ++i){
    b_twiddle[i] = h*h*100*exp(-10*x[i]);
  }

  special_forward(b_recip, b_twiddle, N);
  special_backward(b_recip, b_twiddle, u, N);

  cout << max(u-u_anal) << endl;

  return 0;
}
