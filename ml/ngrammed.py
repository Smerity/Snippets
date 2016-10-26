def ngrammed(word, N=3):
  for n in range(1, N + 1):
    for i in range(len(word) - n + 1):
      yield word[i:i+n]

if __name__ == '__main__':
  print(list(ngrammed('worded')))
