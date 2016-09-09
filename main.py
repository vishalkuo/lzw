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

	# Check last run to see if it needs to be added to result
	if len(current_run) > 0:
		resultant_code.append(dictionary[current_run])

	return resultant_code

def decode(l):
	# Reverse dictionary
	dictionary = dict((c, chr(c)) for c in range(ASCII_SIZE))
	max_index = ASCII_SIZE
	# Add our first entry and set our run
	s = dictionary[l[0]]
	r = s
	for n in l[1:]:
		# Number doesn't exist, we add our current run to first elem
		if n not in dictionary:
			entry = s + s[0]
		else:
			entry = dictionary[n] 
		r += entry
		dictionary[max_index] = s + entry[0]
		max_index += 1
		s = entry

	return r


def main():
	if len(sys.argv) < 2:
		raise ValueError("No string provided provided!")
	s_to_encode = sys.argv[1]
	print(encode(s_to_encode))


if __name__ == '__main__':
	main()
	