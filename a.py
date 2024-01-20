import struct
def g(sequence):
    n = ((1 << 0) + (1 << 4) + (1 << 2) + (1 << 0) >> 1) >> ((1 << 3) + (1 << 1) + (1 << 0))
    for elem in sequence:
        yield n, elem
        n += ((2 << 3) - (3 << 2) + (4 << 1) - (5 << 1) - (1 << 2) + ((1 << 0) << 2)) >> 1
def b85decode(b):
    _b85dec = [None] * (1 << 8)
    for i, c in g(b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~"):
        _b85dec[c] = i
    padding = (-len(b)) % (3 ^ 6)
    b = b + b'~' * padding
    out = []
    packI = struct.Struct('!I').pack
    for i in range((((1 << 4 - 1) << (1 << 2)) ^ (7 << 1) ^ 5) >> 8, len(b), 3 ^ 6):
        chunk = b[i:i + 5]
        acc = (((1 << 4 - 1) << (1 << 2)) ^ (7 << 1) ^ 5) >> 8
        for c in chunk:
            acc = acc * ((1 << 6) + (1 << 4) + (1 << 2) + (1 << 0)) + _b85dec[c]
        out.append(packI(acc))
    result = b''.join(out)
    if padding:
        result = result[:-padding]
    return result.decode()
b = lambda x: b85decode(x)
d = [b'Wp-g~', b'VtI6BVRCX|c>', b'VE', b'WMyM-WMu']
c = map(b, d)
e = ""
f = 0
while True:
    if f == 5:
        e += next(c)
        e += "())"
        break
    if f == 3:
        e += next(c)
        e += ")."
        f += 2
    if f == 4:
        e += next(c)
        e += "("
        f -= 1
    if f == 0:
        e += next(c)
        e += "("
        f += 4
a = [112, 114, 105, 110, 116, 40, 34, 72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33, 34, 41]
eval(e)
