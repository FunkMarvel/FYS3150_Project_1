#include <iostream>
#include <armadillo>
#include <cmath>
#include "functions.h"
#include "time.h"

using namespace std;
using namespace arma;

void general_main(int N, double h, vec& u_anal, vec& x)
{
  vec a(N-1); a.fill(-1);           // Vector for lower diagonal.
  vec b(N); b.fill(2);              // Vector for diagonal.
  vec c(N-1); c.fill(-1);           // Vector for upper diagonal.
  vec u(N);                         // Vector for numerical solution
  vec b_twiddle = zeros<vec>(N);    // Vector for function value (times h^2)

  // Generating values for input function
  for (int i = 0; i<N; ++i){
    b_twiddle[i] = h*h*100*exp(-10*x[i]);
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

  u[0] = 0;
  u[N-1] = 0;

  // Print time spent
  double general_cputime = ( double(finish - start)/CLOCKS_PER_SEC );
  cout << "General algorithm took " << general_cputime << " seconds to finish."
       << endl;

  // Calculate maximum of log10 of relative error
  double eps_general = find_relative_error(u,u_anal,N);
  cout << "Maximum (log10 of) relative error in general algorithm with " << N
       << " steps: " << eps_general << endl;

  u.save("u_general.bin", raw_binary);
}
