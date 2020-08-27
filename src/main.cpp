#include <iostream>
#include <armadillo>


using namespace std;
using namespace arma;

int main(int argc, char** argv)
{
  int N = atoi(argv[1]);
  vec x = linspace<vec>(0, 1, N);

  cout << x << N << endl;

  return 0;
}
