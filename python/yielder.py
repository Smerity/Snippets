def example(x):
    for i in range(x):
        yield i ** 2

def batcher(gen):
    results = []
    for i in gen:
        results.append(i)
        if len(results) == 4:
            yield results
            results = []
    if results:
        yield results

for res in batcher(example(17)):
    print(res)
