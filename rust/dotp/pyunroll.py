from string import ascii_letters
#print(len(ascii_letters), ascii_letters)

tokens = ascii_letters

MAX = 8
BREAK = 4

for y in range(MAX // BREAK):
  for x in range(BREAK):
    i = y * BREAK + x
    a = 'let x_{} = _mm256_loadu_ps(a.as_ptr().offset({}));'
    b = 'let y_{} = _mm256_loadu_ps(b.as_ptr().offset({}));'
    c = 'let r_{} = _mm256_loadu_ps(c.as_ptr().offset({}));'
    d = '_mm256_storeu_ps(c.as_mut_ptr().offset({}), _mm256_fmadd_ps(x_{}, y_{}, r_{}));'
    print(a.format(tokens[i], i * 8))
    print(b.format(tokens[i], i * 8))
    print(c.format(tokens[i], i * 8))
    print(d.format(i * 8, tokens[i], tokens[i], tokens[i]))
    print('//')
