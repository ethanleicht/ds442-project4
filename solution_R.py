import numpy as np

# The prior probabilities for Burglary (B) and Earthquake (E)
P_B = np.array([0.001, 0.999])  # [P(+b), P(-b)]
P_E = np.array([0.002, 0.998])  # [P(+e), P(-e)]

# The conditional probabilities of Alarm (A) given Burglary (B) and Earthquake (E)
P_A_given_B_E = np.array([
    [[0.95, 0.94], [0.29, 0.001]],  # P(A|+b,+e), P(A|+b,-e)
    [[0.05, 0.06], [0.71, 0.999]]   # P(A|-b,+e), P(A|-b,-e)
])

# The conditional probabilities of John calling (J) given Alarm (A)
P_J_given_A = np.array([
    [0.9, 0.05],  # P(J|+a), P(J|-a)
    [0.1, 0.95]   # P(J|+a'), P(J|-a')
])

# Compute the full joint probability table P(B,E,A,J)
P_BEAJ = np.zeros((2, 2, 2, 2))

# Nested loops to calculate the full joint distribution
for b in [0, 1]:  # b = 0 for +b, b = 1 for -b
    for e in [0, 1]:  # e = 0 for +e, e = 1 for -e
        for a in [0, 1]:  # a = 0 for +a, a = 1 for -a
            P_BEAJ[b, e, a, :] = P_B[b] * P_E[e] * P_A_given_B_E[a, b, e] * P_J_given_A[:, a]

# Variable elimination: sum out E and A
P_BJ = np.sum(P_BEAJ, axis=(1, 2))

# Normalize to get P(B|J=j+)
P_B_given_J = P_BJ[:, 0] / np.sum(P_BJ[:, 0])

print(f"(P(Burglary | John Calls = +j)): {P_B_given_J[0]:.5f}")
print(f"(P(~Burglary | John Calls = +j)): {P_B_given_J[1]:.5f}")
