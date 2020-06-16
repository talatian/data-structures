

string = '([]{)}'
stack = []

pairs = {'{':'}','(':')','[':']'}

print(stack[-1:])

for char in string:
	if stack[-1:] in pairs:
		if pairs[stack[-1:]] == char:
			stack.pop()
		else:
			stack.append(string[i])
	else:
		print('bad string')
		break
if len(stack) == 0:
	print('good string')

print(stack)
		
	
	
