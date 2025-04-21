x = 0.7
epsilon = 0.01

P = 0
n = 1
term = x  # ilk termin -x

while abs(term) >= epsilon:
    term = (x**n) / n
    P -= term
    n += 1

print(f"P cəmi ≈ {P:.4f} (ε = {epsilon})")
