def grayCode(n):
	base = ['0','1']
	if n == 0:
		return [0]

	result = base
	for i in range(n-1):
		left = list(map(lambda x: '0' + x,result))
		right = list(map(lambda x: '1' + x, result[::-1]))
		result = left + right
	return list(map(lambda x: int(x,2),result))


print(grayCode(1))
