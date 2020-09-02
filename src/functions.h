#ifndef FUNCTION_HEADER
#define FUNCTION_HEADER

#include <armadillo>
using namespace arma;

//general_algorithm.cpp:

void general_forward(vec& a, vec& b, vec& c, vec& b_twiddle, int N);
void general_backward(vec& b, vec& b_twiddle, vec& c, vec& u, int N);


//special_algorithm.cpp:

void special_forward(vec& b_recip, vec& b_twiddle, int N);
void special_backward(vec& b_recip, vec& b_twiddle, vec& u, int N);

#endif
