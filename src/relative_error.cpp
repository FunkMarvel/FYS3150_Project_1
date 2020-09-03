#include <iostream>
#include <armadillo>
#include <cmath>
#include "functions.h"

using namespace std;
using namespace arma;

double find_relative_error(vec& u, vec& u_anal, int N)
{
  /* Calculates log10 of relative error in all steps, and returns
  *  the maximum of these values.
  */
  double eps;
  vec epsilon = zeros<vec>(N);
  for (int i=1; i<N-1; ++i){
    epsilon[i] = log10( abs((u[i]-u_anal[i]) / u_anal[i]) );

  }
  eps = max(epsilon);
  return eps;
}
