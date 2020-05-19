export void dotp(uniform const float X[], uniform const float Y[], uniform float Z[], uniform const uint N) {
    foreach(i = 0 ... 1024) {
        Z[i] += X[i] * Y[i];
    }
}
