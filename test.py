prices = [100, 102, 101, 105]

returns = []

for i in range(1, len(prices)):
    r = prices[i] / prices[i - 1] - 1
    returns.append(r)

print(returns)