import argparse
from slacker import Slacker

settings = None

def init_settings():
	parser = argparse.ArgumentParser()
	parser.add_argument('-t', '--token', help='Slack API token', required=True, type=str)
	args = parser.parse_args()
	return args

def main():
	global settings
   
	try:
		settings = init_settings()
		slack = Slacker(settings.token)
		
	except (KeyboardInterrupt, SystemExit):
		print "-> Aborted through user interaction"


if __name__ == "__main__":
	main()