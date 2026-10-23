"""Controlli finiti di calcoli ed esempi; non sostituiscono le prove generali."""
from fractions import Fraction
from itertools import product
from math import gcd, isqrt, lcm
import json
from pathlib import Path


def run():
    checks = {}
    universe = set(range(4))
    subsets = [{x for x in universe if mask & (1 << x)} for mask in range(16)]
    for a, b, c in product(subsets, repeat=3):
        assert (a ^ b) ^ c == a ^ (b ^ c)
        assert (a | b) & c == (a & c) | (b & c)
        assert (a & b) | c == (a | c) & (b | c)
        assert (a ^ b) & c == (a & c) ^ (b & c)
        assert universe - (a | b) == (universe - a) & (universe - b)
        assert universe - (a & b) == (universe - a) | (universe - b)
    checks['identita_insiemi'] = {'terne': 16 ** 3, 'esito': True}

    fractions_checked = 0
    for a, b, c, d in product(range(-3, 4), repeat=4):
        if not b or not d:
            continue
        for u, v in [(2, -3), (-2, 5)]:
            x, y = Fraction(a, b), Fraction(c, d)
            assert Fraction(a * u, b * u) == x
            assert Fraction(a * u * d * v + c * v * b * u, b * u * d * v) == x + y
            assert Fraction(a * u * c * v, b * u * d * v) == x * y
            fractions_checked += 1
    checks['cambi_rappresentante_razionali'] = fractions_checked

    f = lambda n: 2 * n - 3 if n % 2 == 0 else n + 1
    images = [f(n) for n in range(-500, 501)]
    assert len(set(images)) == len(images)
    assert all(y % 2 == 0 or y % 4 == 1 for y in images)
    assert 3 not in images
    checks['funzione_intera_a_tratti'] = {'punti': len(images), 'esito': True}

    plane_cases = 0
    for x, y in product([Fraction(i, 3) for i in range(-15, 16)], repeat=2):
        u, v = y ** 3, x * (y * y + 1)
        assert v / (1 + y * y) == x
        assert (Fraction(x), Fraction(y)) == (v / (1 + y * y), y)
        assert u == y ** 3
        plane_cases += 1
    checks['inversa_piano_sostituzione_esatta'] = plane_cases

    division_cases = 0
    for a, b in product(range(-80, 81), repeat=2):
        if b:
            r = a % abs(b)
            q = (a - r) // b
            assert a == b * q + r and 0 <= r < abs(b)
            assert gcd(a, b) == gcd(b, r)
            division_cases += 1
        if (a, b) != (0, 0):
            assert gcd(a, b) * lcm(a, b) == abs(a * b)
            g = gcd(a, b)
            assert gcd(a // g, b // g) == 1
    checks['divisione_con_segni_e_passo_euclideo'] = division_cases
    assert gcd(72, 420) == 12 == 6 * 72 - 420
    assert gcd(-12, 16) == 4
    checks['esempio_bezout_72_420'] = [12, 6, -1]

    primes = [n for n in range(2, 400) if all(n % d for d in range(2, isqrt(n) + 1))]
    assert [p for p in primes if p <= 20] == [2, 3, 5, 7, 11, 13, 17, 19]
    support = lambda n: {p for p in primes if n % p == 0}
    assert support(1) == set() and support(4) == {2} and support(12) == {2, 3}
    assert support(30) == {2, 3, 5} and support(7) == {7}
    for n in range(1, 400):
        assert (support(n) == {5}) == (n in {5 ** k for k in range(1, 5)})
        assert (support(n) == {2, 3}) == any(n == 2 ** a * 3 ** b for a in range(1, 9) for b in range(1, 6))
    checks['supporto_primo_e_fibre'] = {'intervallo': [1, 399], 'esito': True}

    for t in range(10000):
        odd, m = t + 1, 0
        while odd % 2 == 0:
            odd //= 2
            m += 1
        n = (odd - 1) // 2
        assert 2 ** m * (2 * n + 1) - 1 == t
    checks['codifica_coppie_inverse'] = 10000

    assert Fraction(1) == sum(Fraction(1, 2 ** n) for n in range(1, 30)) + Fraction(1, 2 ** 29)
    for length in range(1, 9):
        codes = [sum((Fraction(2 * digit, 3 ** (i + 1)) for i, digit in enumerate(bits)), Fraction())
                 for bits in product([0, 1], repeat=length)]
        assert len(codes) == len(set(codes))
    checks['codifica_ternaria_prefissi'] = {'lunghezze': [1, 8], 'esito': True}
    checks['limite'] = 'Controlli su insiemi finiti e intervalli dichiarati; le prove generali sono nel testo.'
    target = Path(__file__).resolve().parents[1] / 'CONTROLLI_MATEMATICI_2026-10-23.json'
    target.write_text(json.dumps(checks, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(checks, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    run()
