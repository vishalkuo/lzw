import sys

ASCII_SIZE = 256

def encode(s):
	# Produce dict keyed by ascii characters with appropriate index value
	dictionary = dict((chr(c), c) for c in range(ASCII_SIZE))
	max_index = ASCII_SIZE
	resultant_code = []
	current_run = ""
	for c in s:
		# Set our run to the letter in the string + our current run
		run = c + current_run
		# Case when we already have this in our dict (can be compressed further)
		if run in dictionary:
			current_run = run
		else:
			# Update dict and result, reset current run to our current character
			dictionary[run] = max_index
			resultant_code.append(dictionary[current_run])
			max_index += 1
			current_run = c

	# Check last string
	if len(current_run) > 0:
		resultant_code.append(dictionary[current_run])

	return resultant_code


def main():
	# if len(sys.argv) < 2:
	# 	raise ValueError("No string provided provided!")
	# s_to_encode = sys.argv[1]
	print(encode("thisisthe"))


if __name__ == '__main__':
	main()
	