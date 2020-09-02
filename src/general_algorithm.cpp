#include <iostream>
#include <armadillo>
#include <cmath>
#include "functions.h"

using namespace std;
using namespace arma;

void general_forward(vec& a, vec& b, vec& c, vec& b_twiddle, int N)
{
  //forward loop
  for (int i = 1; i<N; ++i){
    b[i] = b[i]- a[i-1]*c[i-1]/b[i-1];
    b_twiddle[i] = b_twiddle[i]- a[i-1]*b_twiddle[i-1]/b[i-1];
  }
}

void general_backward(vec& b, vec& b_twiddle, vec& c, vec& u, int N)
{
  //setting first element
  u[N-1] = b_twiddle[N-1]/b[N-1];

  //backward loop
  for (int i = N-1; i>=1;--i){
    u[i-1] = (b_twiddle[i-1] - c[i-1]*u[i])/b[i-1];
  }
}
