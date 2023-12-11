# Given probabilities from the tables in the attachment
P_B = 0.001  # Probability of Burglary
P_notB = 0.999  # Probability of not Burglary
P_E = 0.002  # Probability of Earthquake
P_notE = 0.998  # Probability of not Earthquake

# Conditional probabilities from the tables
P_A_given_BE = 0.95
P_A_given_B_notE = 0.94
P_A_given_notB_E = 0.29
P_A_given_notB_notE = 0.001

P_J_given_A = 0.9  # Probability of John calling given Alarm
P_J_given_notA = 0.05  # Probability of John calling given no Alarm

# Compute P(Alarm) using total probability
P_A = (P_A_given_BE * P_B * P_E) + \
      (P_A_given_B_notE * P_B * P_notE) + \
      (P_A_given_notB_E * P_notB * P_E) + \
      (P_A_given_notB_notE * P_notB * P_notE)

# Compute P(John Calls = +j) using total probability
P_J = (P_J_given_A * P_A) + (P_J_given_notA * (1 - P_A))

# Compute P(John Calls = +j | Burglary)
# This is the total probability of John calling when there is a burglary,
P_J_given_B = (P_J_given_A * (P_A_given_BE * P_E + P_A_given_B_notE * P_notE)) + \
              (P_J_given_notA * (1 - (P_A_given_BE * P_E + P_A_given_B_notE * P_notE)))

P_B_given_J = (P_J_given_B * P_B) / P_J

P_B_given_J

# Compute P(John Calls = +j | no Burglary)
P_J_given_notB = (P_J_given_A * (P_A_given_notB_E * P_E + P_A_given_notB_notE * P_notE)) + \
                 (P_J_given_notA * (1 - (P_A_given_notB_E * P_E + P_A_given_notB_notE * P_notE)))

# Compute P(no Burglary | John Calls = +j)
P_notB_given_J = (P_J_given_notB * P_notB) / P_J

# Create the distribution table
distribution_table = {
    'Burglary': P_B_given_J,
    'No Burglary': P_notB_given_J
}

# Print the distribution table
for condition, probability in distribution_table.items():
    print(f"P({condition} | John Calls = +j): {probability:.4f}")

distribution_table
