#!/usr/bin/env python3

from pathlib import Path
import sys, os, re, itertools

api_key_min_entropy_ratio = 0.5
api_key_min_length = 20

def pairwise(iterable):
	"s -> (s0,s1), (s1,s2), (s2, s3), ..."
	a, b = itertools.tee(iterable)
	next(b, None)
	return zip(a, b)

def token_is_api_key(token):
	"""
	Returns True if the token is an API key or password.
	"""
	if len(token) < api_key_min_length:
		return (False, '')
	entropy = 0
	for a, b in pairwise(list(token)):
		if not ((str.islower(a) and str.islower(b)) or (str.isupper(a) and\
			str.isupper(b)) or (str.isdigit(a) and str.isdigit(b))):
			entropy += 1
	return (float(entropy) / len(token) > api_key_min_entropy_ratio, float(entropy) / len(token))

def line_contains_api_key(line, regex_str=None):
	"""
	Returns True if any token in the line contains an API key or password.
	"""
	for token in re.findall(regex_str, line):
		result = token_is_api_key(token)
		if result[0]:
			return (True, result[1])
	return (False, '')

def scan_file(fpath):
	"""
	Prints out lines in the specified file that probably contain an API key or password.
	"""
	print(f'Scanning {fpath}...')
	f = open(fpath)
	number = 1
	for line in f:
		## Searching for lines w/ potential api key declaration
		regex_str = '(?i)(.*project.*=.*|.*api_key.*=.*)'
		result = line_contains_api_key(line, regex_str)
		if result[0]:
			print(f'\033[1m{fpath}: Line {number} : Entropy {result[1]}\033[0m')
			print(line)
			raise ValueError(f'API key found in file {fpath}: Line {number}')

		number += 1

def scan_dir(path, ext):
	for f in Path(path).glob(f"**/*.{ext}"):
		scan_file(str(f))



if __name__ == "__main__":
	if len(sys.argv) == 1:
		print('Please specify path.')
		sys.exit(0)

	path = str(sys.argv[1])
	
	print(f'Scanning directory: {path}') 
	print(f'For tokens with minimum API key length: {api_key_min_length}')
	print(f'For tokens with minimum entropy ratio: {api_key_min_entropy_ratio}')

	scan_dir(path, ext='ipynb')
	scan_dir(path, ext='md')
	