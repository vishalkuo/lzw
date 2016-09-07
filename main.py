import sys
import string

chars = string.ascii_lowercase
dictionary = dict(zip(chars, [ord(c) - 97 for c in chars]))

def encode(s):
	pass

def main():
	if len(sys.argv) < 2:
		raise ValueError("No string provided provided!")
	s_to_encode = sys.argv[1]


if __name__ == '__main__':
	main()
	