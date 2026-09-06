# Bubble Sort Implementation - Student Marks Ordering

marks = [72, 45, 89, 33, 60]

print("=== BUBBLE SORT - Student Marks ===")
print("Original Marks:", marks)
print()

n = len(marks)

for i in range(n - 1):
    print(f"--- Pass {i + 1} ---")
    for j in range(n - 1 - i):
        if marks[j] > marks[j + 1]:
            marks[j], marks[j + 1] = marks[j + 1], marks[j]
            print(f"  Swapped: index {j} and {j+1} -> {marks}")
        else:
            print(f"  No swap : index {j} and {j+1} -> {marks}")
    print(f"  After Pass {i + 1}: {marks}")
    print()

print("=== Sorted Marks (Ascending Order) ===")
print("Final Sorted Marks:", marks)
