def is_disarium(num):
    num_str = str(num)
    total = 0
    for i, digit in enumerate(num_str):
        total += int(digit) ** (i + 1)
    return total == num

def find_first_n_disarium(n):
    disarium_numbers = []
    num = 1
    while len(disarium_numbers) < n:
        if is_disarium(num):
            disarium_numbers.append(num)
        num += 1
    return disarium_numbers

def find_disarium_between(start, end):
    disarium_numbers = []
    for num in range(start, end + 1):
        if is_disarium(num):
            disarium_numbers.append(num)
    return disarium_numbers

# Example usage:
n = 5  # Find the first 5 Disarium numbers
start = 100
end = 200  # Find Disarium numbers between 100 and 200

first_n_disarium = find_first_n_disarium(n)
disarium_between_range = find_disarium_between(start, end)

print("First", n, "Disarium numbers:", first_n_disarium)
print("Disarium numbers between", start, "and", end, ":", disarium_between_range)
