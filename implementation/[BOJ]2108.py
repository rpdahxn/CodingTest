import sys
from collections import Counter

# n = int(input())
n = int(sys.stdin.readline())
numbers = []
for _ in range(n):
    # numbers.append(int(input()))
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

print(round(float(sum(numbers)/len(numbers))))
print(numbers[len(numbers)//2])


def mode(numbers):
    count = Counter(numbers).most_common()

    if (len(numbers) >= 2):
        if count[0][1] == count[1][1]:
            return count[1][0]
        else:
            return count[0][0]
    else:
        return count[0][0]


print(mode(numbers))
print(max(numbers) - min(numbers))
