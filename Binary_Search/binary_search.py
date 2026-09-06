# Binary Search Implementation - Student Registration Lookup

roll_numbers = [101, 105, 110, 115, 120, 125, 130]
target = 120

print("=== BINARY SEARCH - Student Record Search ===")
print("Sorted Roll Numbers:", roll_numbers)
print(f"Searching for Roll Number: {target}\n")

low = 0
high = len(roll_numbers) - 1
found = False
step = 1

while low <= high:
    mid = (low + high) // 2

    print(f"Step {step}:")
    print(f"  Low = {low}, High = {high}, Mid = {mid}")
    print(f"  Middle element = roll_numbers[{mid}] = {roll_numbers[mid]}")

    if roll_numbers[mid] == target:
        print(f"  {roll_numbers[mid]} == {target} --> FOUND!\n")
        print(f"Roll Number {target} found at index {mid} (Position {mid + 1}).")
        found = True
        break

    elif roll_numbers[mid] < target:
        print(f"  {roll_numbers[mid]} < {target} --> Search RIGHT half\n")
        low = mid + 1

    else:
        print(f"  {roll_numbers[mid]} > {target} --> Search LEFT half\n")
        high = mid - 1

    step += 1

if not found:
    print(f"Roll Number {target} was NOT found in the list.")
