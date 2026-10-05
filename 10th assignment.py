import numpy as np

data = np.arange(1, 11)

print("Original Array:")
print(data)

print("\nFirst five elements:")
print(data[:5])

print("\nElements from index 2 to 6:")
print(data[2:7])

print("\nLast three elements:")
print(data[-3:])

print("\nAlternate elements:")
print(data[::2])

print("\nStatistical Measures:")
print("Sum     :", np.sum(data))
print("Mean    :", np.mean(data))
print("Maximum :", np.max(data))
print("Minimum :", np.min(data))

data = data + 5

print("\nArray after adding 5 using broadcasting:")
print(data)

data = data * 2

print("\nArray after multiplying by 2 using broadcasting:")
print(data)