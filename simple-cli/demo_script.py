import argparse


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('message')
	args = parser.parse_args()
	print(args.message)

main()
