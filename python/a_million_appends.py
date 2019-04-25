def test():
    with open('million_appends.txt','a+') as f:
        f.write('Append\n')

if __name__ == '__main__':
    import timeit
    N = 10000
    time_taken = timeit.timeit("test()", setup="from __main__ import test", number=N)
    print(f'A single append takes {time_taken / N:.5f} seconds (or {N * (1 / time_taken):.0f} appends per second)')
