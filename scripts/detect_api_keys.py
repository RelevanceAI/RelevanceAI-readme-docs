#!/usr/bin/env python3

from pathlib import Path
import sys, os, re, itertools
from typing import Iterable, Union
import logging
import argparse

API_KEY_MIN_ENTROPY_RATIO = 0.5
API_KEY_MIN_LENGTH = 20

def pairwise(iterable: Iterable):
	"s -> (s0,s1), (s1,s2), (s2, s3), ..."
	a, b = itertools.tee(iterable)
	next(b, None)
	return zip(a, b)

def token_is_api_key(token: str):
	"""
	Returns True if the token is an API key or password.
	"""
	if len(token) < API_KEY_MIN_LENGTH:
		return (False, '')
	entropy = 0
	for a, b in pairwise(list(token)):
		if not ((str.islower(a) and str.islower(b)) or (str.isupper(a) and\
			str.isupper(b)) or (str.isdigit(a) and str.isdigit(b))):
			entropy += 1
	return (float(entropy) / len(token) > API_KEY_MIN_ENTROPY_RATIO, float(entropy) / len(token))

def line_contains_api_key(line: str, regex_str=None):
	"""
	Returns True if any token in the line contains an API key or password.
	"""
	for token in re.findall(regex_str, line):
		result = token_is_api_key(token)
		if result[0]:
			return (True, result[1])
	return (False, '')

def scan_file(fpath: Union[Path, str]):
	"""
	Prints out lines in the specified file that probably contain an API key or password.
	"""
	print(f'Scanning {fpath}...')
	f = open(fpath)
	number = 1
	for line in f:
		## Searching for lines w/ potential api key declaration
		regex_str = '(?i)(.*project.*=.*|.*api_key.*=.*|.*token.*=.*)'
		result = line_contains_api_key(line, regex_str)
		if result[0]:
			print(f'\033[1m{fpath}: Line {number} : Entropy {result[1]}\033[0m')
			print(line)
			raise ValueError(f'API key found in file {fpath}: Line {number}')

		number += 1


def get_files(path: Union[Path, str], ext: Union['md', 'ipynb']):
	return Path(path).glob(f"**/*.{ext}")


def main(args):
	logging_level = logging.DEBUG if args.debug else logging.INFO
	logging.basicConfig(format='%(asctime)s %(message)s', level=logging_level)

	logging.info(f'Scanning directory: {args.path}') 
	logging.info(f'For tokens with minimum API key length: {API_KEY_MIN_LENGTH}')
	logging.info(f'For tokens with minimum entropy ratio: {API_KEY_MIN_ENTROPY_RATIO}')

	md_files = get_files(args.path, ext='md')
	notebooks = get_files(args.path, ext='ipynb')

	for f in itertools.chain(md_files, notebooks):
		scan_file(str(f))


if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	ROOT_PATH = Path(__file__).parent.resolve() / '..'

	parser.add_argument("-d", "--debug", default=False, help="Run debug mode")
	parser.add_argument("-p", "--path", default=ROOT_PATH, help="Path of root folder")
	parser.add_argument("-ml", "--min-length", default=API_KEY_MIN_LENGTH, help="Minimum length of API key")
	parser.add_argument("-er", "--entropy-ratio", default=API_KEY_MIN_ENTROPY_RATIO, help="Minimum entropy ratio of API key")

	args = parser.parse_args()

	main(args)
