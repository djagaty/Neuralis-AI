def prime_factors(n):
    if n <= 1:
        return []
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


if __name__ == "__main__":
    assert prime_factors(100) == [2, 5]
    assert prime_factors(17) == [17]
    assert prime_factors(1) == []
    assert prime_factors(0) == []
    assert prime_factors(-5) == []
    assert prime_factors(2) == [2]
    assert prime_factors(360) == [2, 3, 5]
    assert prime_factors(97 * 89) == [89, 97]
    print("all tests passed")
