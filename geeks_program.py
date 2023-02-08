def Solution(s, n):


	s1 = s

	for i in range(1, n):
		
		# Concatenating strings
		s += s1

	return s


s1 = "abc"
n1 = 3
program = Solution(s1, n1)
print(program)
