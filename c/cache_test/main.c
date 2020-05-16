#include <stdio.h>
#include <stdlib.h>
#include <time.h>

float scalarproduct(float *array1, float *array2, float *dest, size_t N) {
  float sum = 0.0f;
  uint UNROLL = 512;
  //for (size_t outer = 0; outer < N / UNROLL; outer++) {
  //  for (size_t inner = 0; inner < UNROLL; inner++) {
  //    size_t i = outer * UNROLL + inner;
  for (size_t i = 0; i < N; ++i) {
      dest[i] = array1[i] * array2[i];
     }
  //}
  return sum;
}

float *newArray(int N) {
  float *x = (float *)malloc(N * sizeof(float));
  for (size_t i = 0; i < N; ++i) {
    x[i] = 2 * ((float)rand() / (float)RAND_MAX) - 1;
  }
  return x;
}

int main(int argc, const char *argv[])
{
  srand(time(NULL));

  clock_t t;
  int N = atoi(argv[1]);
  int K = 1000;
  int LOOPS = 1 * 1000000;

  float **xx = (float **)malloc(sizeof(float **) * K);
  float **yy = (float **)malloc(sizeof(float **) * K);
  float **zz = (float **)malloc(sizeof(float **) * K);

  for (int i = 0; i < K; ++i) {
    xx[i] = newArray(N);
    yy[i] = newArray(N);
    zz[i] = newArray(N);
  }

  float sum = 0.0;

  t = clock();
  for (int k = 0; k < K; ++k) {
    float *x = xx[k];
    float *y = yy[k];
    float *z = zz[k];
    for (int i = 0; i < LOOPS / K; ++i) {
      scalarproduct(x, y, z, N);
    }
    for (size_t i = 0; i < N; ++i) {
      sum += z[i];
      if (k + 1 < K) xx[k + 1][i] *= z[i];
    }
  }
  t = clock() - t;
  double time_taken = ((double)t)/CLOCKS_PER_SEC;

  //printf("x * y for two arrays of size %d over %d loops:\n", N, LOOPS);
  fprintf(stderr, "%f\n", sum);
  //fprintf(stderr, "%f %f %f\n", z[0], z[10], z[100]);
  //printf("fun() took %f seconds to execute \n", time_taken);
  printf("N = %d, K = %d, L/K = %d:\t%2.4f\n", N, K, LOOPS/K, time_taken);

  return 0;
}
