import pandas as pd
import numpy as np

values = pd.Series(np.random.randint(1, 101, 10))

print("Original Series:")
print(values)

print("\nElement at index 3:")
print(values[3])

print("\nFirst five elements:")
print(values[:5])

print("\nNumbers greater than 50:")
print(values[values > 50])

print("\nStatistical Operations:")
print("Mean   :", values.mean())
print("Median :", values.median())
print("Minimum:", values.min())
print("Maximum:", values.max())