n = int(input())

count = {
	1: 0,
	2: 0,
	3: 0
}
curr = [1, 2, 3]
for _ in range(n):
	a, b, guess = map(lambda x: int(x)-1, input().split())
	# swap a and b
	curr[a], curr[b] = curr[b], curr[a]
	# find the number she guessed and increment it's count by 1
	count[curr[guess]] += 1

print(max(count.values()))