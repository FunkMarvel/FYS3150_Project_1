#include <iostream>
#include <armadillo>
#include <cmath>
#include "functions.h"

using namespace std;
using namespace arma;

void general_forward(vec& a, vec& b, vec& c, vec& f, vec& b_twiddle, vec& f_twiddle, int N)
{
  //setting first elements
  b_twiddle[0] = b[0];
  f_twiddle[0] = f[0];

  //forward loop
  for (int i = 1;i<=N;++i){
    b_twiddle[i] = b[i] - a[i-1]*c[i-1]/b_twiddle[i-1];
    f_twiddle[i] = f[i] - a[i-1]*f_twiddle[i-1]/b_twiddle[i-1];
  }
}

void general_backward(vec& b_twiddle, vec& f_twiddle, vec& c, vec& u,int N)
{
  //setting first element
  u[N] = f_twiddle[N]/b_twiddle[N];

  //backward loop
  for (int i = N-1; i>=0;--i){
    u[i] = (f_twiddle[i] - c[i]*u[i+1])/b_twiddle[i];
  }
}
