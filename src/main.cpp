#include <iostream>
#include "functions.h"

using namespace std;

int main(int argc, char** argv)
{
  int N = atoi(argv[1]);            // Step count
  double h = 1.0/(N+1);             // Step length
  //mat A = zeros<mat>(N,N);          // Matrix to use with LU decomposition

  // Performing general algorithm with benchmark.
  general_main(N,h);

  // Performing special algorithm with benchmark.
  special_main(N,h);


  // Generate matrix values to use with LU decomposition
  //A[0,0] = 2;
  //A[0,1] = -1;
  //A[N-1,N-1] = 2;
  //A[N-1,N-2] = -1;
  //for (int i = 1; i<N-1; ++i){
  //  A[i,i-1] = -1;
  //  A[i,i] = 2;
  //  A[i, i+1] = -1;
  //}

  return 0;
}
