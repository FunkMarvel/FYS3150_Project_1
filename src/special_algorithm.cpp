#include <iostream>
#include <armadillo>
#include <cmath>
#include "functions.h"

using namespace std;
using namespace arma;

void special_forward(vec& b_recip, vec& b_twiddle, int N)
{
  //forward loop
  for (int i = 1; i<N; ++i){
    b_twiddle[i] = b_twiddle[i] + b_twiddle[i-1]*b_recip[i-1];
  }
}

void special_backward(vec& b_recip, vec& b_twiddle, vec& u, int N)
{
  //setting first element
  u[N-1] = b_twiddle[N-1]/b_recip[N-1];

  //backward loop
  for (int i = N-1; i>=1; --i){
    u[i-1] = (b_twiddle[i-1] + u[i])/b_recip[i-1];
  }
}
