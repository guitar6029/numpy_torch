import numpy as np, random

# Generate a random integer using Python's built-in random module
x = random.randint(0, 100)
print("rand int X:", x)

# Generate a random array using NumPy
x = np.random.rand(2)
print("rand X:", x)

# Generate a random array using NumPy's randint function
arr = np.random.randint(0, 100, size=5)  # Generates an array of 5 random integers between 0 and 99
print("arr:", arr)

random_arr = np.random.rand(2,2)
print("random_arr:", random_arr)

#choice example
arr_example = np.random.choice([3,6,2,8], size=(2,25))
print("arr_example: \n", arr_example)