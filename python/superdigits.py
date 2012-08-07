superdigits = {'0': '\xe2\x81\xb0',
    '1': '\xc2\xb9',
    '2': '\xc2\xb2',
    '3': '\xc2\xb3',
    '4': '\xe2\x81\xb4',
    '5': '\xe2\x81\xb5',
    '6': '\xe2\x81\xb6',
    '7': '\xe2\x81\xb7',
    '8': '\xe2\x81\xb8',
    '9': '\xe2\x81\xb9'
}

def num_to_superdigits(x):
    return''.join(superdigits[i] for i in str(x))

if __name__ == "__main__":
    for k,v in sorted(superdigits.items()):
        print "%s => %s" % (k,v)
    print

    message = [num_to_superdigits(x) for x in map(ord, "Happy birthday Dom")]
    for chunk in message:
        print "Do%sm" % chunk,
