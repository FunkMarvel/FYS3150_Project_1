#include <iostream>
#include <armadillo>
#include <cmath>
#include "functions.h"
#include "time.h"

using namespace std;
using namespace arma;

void special_main(int N, double h, vec& u_anal, vec& x) {
  vec u = zeros<vec>(N);          // Vector for numerical solution
  vec b_twiddle = zeros<vec>(N);  // Vector with known points.
  vec b_recip = zeros<vec>(N);    // Vector with 1/b.

  // Generating values for input function
  for (int i = 0; i<N; ++i){
    b_twiddle[i] = h*h*100*exp(-10*x[i]);
  }


  // Declaring variables for CPU time measurement
  clock_t start, finish;

  // Start of special algorithm
  start = clock();

  // Calculating 1/b where b is the diagonal elements.
  for (int i = 1; i < N+1; ++i) {
    b_recip[i-1] = i/(i + 1.0);
  }

  special_forward(b_recip, b_twiddle, N);
  special_backward(b_recip, b_twiddle, u, N);

  // Special algorithm finished
  finish = clock();

  // setting known values:
  u[0] = 0;
  u[N-1] = 0;

  // Print time spent
  double special_cputime = ( double(finish - start)/CLOCKS_PER_SEC );
  cout << "Special algorithm took " << special_cputime << " seconds to finish."
       << endl;

  // Calculate maximum of log10 of relative error
  double eps_special = find_relative_error(u,u_anal,N);
  cout << "Maximum (log10 of) relative error in special algorithm with " << N
       << " steps: " << eps_special << endl;

  u.save("u_special" + std::to_string(N) + ".bin", raw_binary);
  // u.save("u_special" + std::to_string(N) + ".txt", arma_ascii);
}
