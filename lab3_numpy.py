"""CSC350 Lab 3: NumPy hands-on
Name:
Roll number:

Run this file after every task:  python lab3_numpy.py
Commit after every task (git add, git commit -m "Task N done").
"""
import numpy as np

print("NumPy version:", np.__version__)

# ================= TASK 1 =================
print("\n=== Task 1 ===")

# 1a
temps = np.array([31, 28, 35, 30, 33, 29, 36])
print("Temperatures:", temps)
print("Dtype:", temps.dtype)
print("Shape:", temps.shape)
print("Size:", temps.size)

# 1b
months = np.arange(1, 13).reshape(3, 4)
print("\nMonths:")
print(months)
print("Shape:", months.shape)

# 1c
print("\nZeros:", np.zeros(5))
print("Ones:")
print(np.ones((2, 3)))

# 1d
rng = np.random.default_rng(42)
dice = rng.integers(1, 7, size=10)
print("\nDice:", dice)


# ================= TASK 2 =================
print("\n=== Task 2 ===")

# 2a
print("First temperature:", temps[0])
print("Last temperature:", temps[-1])

# 2b
print("Weekend:", temps[-2:])

# 2c
print("Reverse:", temps[::-1])

# 2d
hot = temps[temps > 32]
print("Hot days:", hot)
print("Number of hot days:", len(hot))
print("Average:", hot.mean())

# 2e
selected = temps[(temps >= 29) & (temps <= 33)]
print("Temperature 29 to 33:", selected)

# 2f
labels = np.where(temps >= 33, "Hot", "OK")
print("Labels:", labels)


# ================= TASK 3 =================
print("\n=== Task 3 ===")

names = np.array(["Ali", "Sara", "Usman", "Hina", "Bilal"])

marks = np.array([
    [78, 85, 62, 90],
    [92, 88, 95, 79],
    [45, 60, 48, 70],
    [88, 94, 91, 85],
    [65, 42, 75, 58]
])

# 3a
print("Shape:", marks.shape)

# 3b
print("Usman marks:", marks[2])
print("Subject 3 marks:", marks[:, 2])

# 3c
print("Subject average:", marks.mean(axis=0))
print("Student average:", marks.mean(axis=1))

# 3d
avg = marks.mean(axis=1)
top = np.argmax(avg)
print("Highest average student:", names[top])

# 3e
weights = np.array([0.3, 0.3, 0.2, 0.2])
total = np.sum(marks * weights, axis=1)
print("Weighted total:", np.round(total, 1))

# 3f
new_marks = np.clip(marks + 5, 0, 100)
print("New marks:")
print(new_marks)

# 3g
failed = np.sum(marks < 50, axis=0)
print("Failed students:", failed)


# ================= TASK 4 =================
print("\n=== Task 4 ===")

img = np.array([
    [10, 10, 200, 10, 10],
    [10, 10, 220, 10, 10],
    [210, 230, 250, 230, 210],
    [10, 10, 220, 10, 10],
    [10, 10, 200, 10, 10]
])

# 4a
print("Shape:", img.shape)
print("Darkest:", img.min())
print("Brightest:", img.max())

# 4b
inverted = 255 - img
print("Inverted image:")
print(inverted)

# 4c
bw = (img > 128).astype(int)
print("Black and white:")
print(bw)

# 4d
normalized = np.round(img[2] / 255, 2)
print("Normalized row 2:", normalized)

# 4e
center = img[1:4, 1:4]
print("Center 3x3:")
print(center)
