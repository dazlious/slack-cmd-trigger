import argparse
from slacker import Slacker

settings = None

def init_settings():
	parser = argparse.ArgumentParser()

	parser.add_argument('-t', '--token', help='Slack API token', required=True, type=str)
	parser.add_argument('-c', '--channel', help='Slack channel', required=True, type=str)
	parser.add_argument('-cmd', '--command', help='Slack command', required=True, type=str)
	parser.add_argument('-i', '--instruction', help='Slack instruction for command', required=True, type=str)

	args = parser.parse_args()
	return args

def main():
	global settings
   
	try:
		settings = init_settings()
		slack = Slacker(settings.token)
		channel_id = slack.channels.get_channel_id(settings.channel)
		slack.chat.command(
	        channel=channel_id,
	        command='/' + settings.command,
	        text=settings.instruction
		)
		
	except (KeyboardInterrupt, SystemExit):
		print "-> Aborted through user interaction"


if __name__ == "__main__":
	main()