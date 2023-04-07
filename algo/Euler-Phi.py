def euler_phi(N):
    phi = int(N > 0 and N)
    for p in range(2, int(N ** 0.5) + 1):
        if not N % p:
            phi -= phi // p
            while not N % p:
                N //= p
    if N > 1:
        phi -= phi // N
    return phi
