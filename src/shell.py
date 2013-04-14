import cmd
import sys
import readline

class InteractiveShell(cmd.Cmd):
	def __init__(self, path):
		cmd.Cmd.__init__(self, 'tab', sys.stdin, sys.stdout)
		self.path = path
	
	def do_ls(self, args):
		print self.path.ls()
