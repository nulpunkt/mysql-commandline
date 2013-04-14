import cmd
import sys
import readline

class InteractiveShell(cmd.Cmd):
	def __init__(self, path):
		cmd.Cmd.__init__(self, 'tab', sys.stdin, sys.stdout)
		self.path = path
	
	def do_ls(self, args):
		print ' '.join(self.path.ls())
	
	def do_cd(self, args):
		self.path.cd(args)
	def complete_cd(self, text, line, begidx, endidx):
		return self.path.ls()
