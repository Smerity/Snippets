#include <stdio.h>
#include <stdlib.h>
#include <time.h>

float scalarproduct(float *array1, float *array2, size_t length) {
  float sum = 0.0f;
  for (size_t i = 0; i < length; ++i) {
    sum += array1[i] * array2[i];
  }
  return sum;
}

float *newArray(int N) {
  float *x = (float *)malloc(N * sizeof(float));
  for (unsigned int outer = 0; outer < N / 128; outer++) {
    for (unsigned int inner = 0; inner < 128; inner++) {
      unsigned int i = outer * 128 + inner;
      x[i] = 2 * ((float)rand() / (float)RAND_MAX) - 1;
    }
  }
  return x;
}

int main(int argc, const char *argv[])
{
  srand(time(NULL));

  clock_t t;
  int N = atoi(argv[1]);
  int LOOPS = 10000000;

  float *x = newArray(N);
  float *y = newArray(N);
  float *z = newArray(N);

  float sum = 0.0;

  t = clock();
  for (int i = 0; i < LOOPS; i++) {
    sum += scalarproduct(x, y, N);
  }
  t = clock() - t;
  double time_taken = ((double)t)/CLOCKS_PER_SEC;

  //printf("x * y for two arrays of size %d over %d loops:\n", N, LOOPS);
  fprintf(stderr, "%f\n", sum);
  //printf("fun() took %f seconds to execute \n", time_taken);
  printf("N = %d:\t%2.4f\n", N, time_taken);

  return 0;
}
