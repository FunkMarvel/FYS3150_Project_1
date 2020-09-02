#ifndef FUNCTION_HEADER
#define FUNCTION_HEADER

#include <armadillo>
using namespace arma;

// general_algorithm.cpp:

void general_forward(vec& a, vec& b, vec& c, vec& b_twiddle, int N);
void general_backward(vec& b, vec& b_twiddle, vec& c, vec& u, int N);

// relative_error.cpp:

double find_relative_error(vec& u, vec& u_anal, int N);

#endif
