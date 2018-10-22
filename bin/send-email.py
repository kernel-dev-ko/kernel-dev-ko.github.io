#!/bin/python3
import argparse
import subprocess
import getpass

def init_cmd(pw):
	cmd = ['git', 'send-email']
	smtp_config = {
		'smtp-server':'smtp.gmail.com',
		'smtp-server-port':'587',
		'smtp-encryption':'tls',
		'smtp-user':'kernel.dev.ko@gmail.com',
		'smtp-pass':pw
	}

	for item in smtp_config.items():
		k, v = item
		option = '--' + k
		cmd.append(option)
		cmd.append(v)

	return cmd

def read_address(filename_addr):
	address = []
	with open(filename_addr) as f:
		lines = f.readlines()
		for line in lines:
			addr = line.strip()
			address.append(addr)

	return address

def send_email(cmd_base, address, filename_content):
	for addr in address:
		cmd = cmd_base[:]
		cmd.append('--to')
		cmd.append(addr)
		cmd.append(filename_content)

		ret = subprocess.run(cmd, stdout=subprocess.PIPE)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'--address',
		type = str,
		required = True,
		help = 'filename for email address'
	)
	parser.add_argument(
		'--content',
		type = str,
		required = True,
		help = 'filename for content'
	)
	FLAGS, unparsed = parser.parse_known_args()

	pw = getpass.getpass('Enter your Password: ')
	cmd = init_cmd(pw)
	address = read_address(FLAGS.address)
	send_email(cmd, address, FLAGS.content)
