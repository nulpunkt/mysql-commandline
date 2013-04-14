class Path:
	def __init__(self, db):
		self.db = db
	def ls(self):
		return ' '.join(self.db.show_databases())
