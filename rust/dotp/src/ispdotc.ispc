export void dotp(uniform const float X[], uniform const float Y[], uniform float Z[]) {
    foreach(i = 0 ... 1024) {
        Z[i] += X[i] * Y[i];
    }
}
