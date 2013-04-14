import cmd
import sys
import readline

class InteractiveShell(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self, 'tab', sys.stdin, sys.stdout)
	
	def do_lol(self, args):
		return "lol ", args
	def complete_lol(self, text, line, begidx, endidx):
		return ['hest']
