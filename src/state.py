class Path:
	def __init__(self, db):
		self.db = db
		self.database = None

	def ls(self):
		if self.database == None:
			return self.db.show_databases()
		else:
			return self.db.show_tables(self.database)

	def cd(self, folder):
		self.database = folder
