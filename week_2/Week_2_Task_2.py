s1 = input("Enter a string:")
digits = [int(ch) for ch in s1 if ch.isdigit()]

total = sum(digits)
average = total / len(digits) if digits else 0

print("Sum is:", total)
print("Average is:", average)