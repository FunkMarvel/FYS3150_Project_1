#ifndef FUNCTION_HEADER
#define FUNCTION_HEADER

#include <armadillo>
using namespace arma;

//general_algorithm.cpp:

void general_forward(vec& a, vec& b, vec& c, vec& f, vec& b_twiddle, vec& f_twiddle, int N);
void general_backward(vec& b_twiddle, vec& f_twiddle, vec& c, vec& u,int N);

#endif
