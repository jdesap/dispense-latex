"""Riscontri finiti sugli esempi delle lezioni 21–24. Eseguire con Python 3."""
from itertools import permutations
from math import gcd


def perm(n, *cycles):
    result = list(range(n + 1))
    for cycle in cycles:
        for i, point in enumerate(cycle):
            result[point] = cycle[(i + 1) % len(cycle)]
    return tuple(result)


def compose(a, b):
    return tuple(a[i] for i in b)


def inverse(a):
    return tuple(a.index(i) for i in range(len(a)))


def conjugate(a, h):
    return compose(compose(h, a), inverse(h))


def cyclic(a):
    identity = tuple(range(len(a)))
    group = {identity}
    x = a
    while x != identity:
        group.add(x)
        x = compose(x, a)
    return group


def symmetric(n):
    return [(0,) + x for x in permutations(range(1, n + 1))]


def sign(p):
    return (-1) ** sum(x > y for i, x in enumerate(p) for y in p[i + 1:])


def main():
    s, t = perm(6, (1, 4, 2, 5, 3)), perm(6, (1, 3, 5), (2, 6))
    assert compose(s, t) == perm(6, (2, 6, 5, 4))
    assert compose(t, s) == perm(6, (1, 4, 6, 2))
    assert conjugate(s, t) == perm(6, (3, 4, 6, 1, 5))
    assert conjugate(t, s) == perm(6, (4, 1, 3), (5, 6))

    s = perm(12, (1, 3), (2, 5, 7), (11, 4, 9, 8))
    t = (0, 3, 4, 1, 2, 5, 9, 7, 6, 8, 11, 10, 12)
    assert conjugate(s, t) == perm(12, (3, 1), (4, 5, 7), (10, 2, 8, 6))
    target = perm(12, (7, 8), (1, 4, 3), (2, 9, 11, 6))
    assert conjugate(s, (0, 7, 1, 8, 9, 4, 5, 3, 6, 11, 10, 2, 12)) == target
    # Cercare le immagini punto per punto, imponendo h(s(x)) = target(h(x)).
    def extend(mapping):
        if all(mapping):
            return 1
        point = mapping.index(None) + 1
        count = 0
        for image in set(range(1, 13)).difference(mapping):
            trial = mapping.copy()
            x, y = point, image
            while trial[x - 1] is None and y not in trial:
                trial[x - 1] = y
                x, y = s[x], target[y]
            if x == point and y == image:
                count += extend(trial)
        return count

    assert extend([None] * 12) == 144
    s6 = symmetric(6)
    for p, count in [(perm(6, (1, 4, 5)), 18), (perm(6, (1, 2), (5, 6, 3)), 6),
                     (perm(6, (1, 3), (2, 4)), 16)]:
        assert sum(compose(h, p) == compose(p, h) for h in s6) == count
    s4 = symmetric(4)
    assert all(sign(compose(a, b)) == sign(a) * sign(b) for a in s4 for b in s4)
    a4 = [x for x in s4 if sign(x) == 1]
    assert len(a4) == 12 and sum(len(cyclic(x)) == 3 for x in a4) == 8
    assert {len(cyclic(x)) for x in s4} == {1, 2, 3, 4}
    h = cyclic(perm(3, (1, 2)))
    x = perm(3, (1, 3))
    assert {compose(a, x) for a in h} == {x, perm(3, (1, 3, 2))}
    assert {compose(x, a) for a in h} == {x, perm(3, (1, 2, 3))}
    for n in range(3, 13):
        r = perm(n, tuple(range(1, n + 1)))
        reflection = (0,) + tuple(1 + ((2 - i) % n) for i in range(1, n + 1))
        rotations = cyclic(r)
        group = rotations | {compose(x, reflection) for x in rotations}
        center = [x for x in group if all(compose(x, y) == compose(y, x) for y in group)]
        assert len(group) == 2 * n and len(center) == gcd(n, 2)
    for m in range(2, 101):
        units = [a for a in range(m) if gcd(a, m) == 1]
        assert all(pow(a, len(units), m) == 1 for a in units)
    print('Verificati esempi di permutazioni, 144 coniugatori, centralizzanti, segni, ordini, laterali, diedrali e unità modulari.')


if __name__ == '__main__':
    main()
