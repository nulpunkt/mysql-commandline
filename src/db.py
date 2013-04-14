import MySQLdb as mdb
import sys

class MySql:
	def connect(self):
		self.conn = mdb.connect('mysql1.gigahost.dk', 'nulpunkt', 'dot.42pass', '')
	def close(self):
		self.conn.close()
	
	def show_databases(self):
		result = self.execute_and_fetchall('SHOW DATABASES')
		return self.map_database_result(result)

	def map_database_result(self, result):
		dbs = []
		for e in result[1:]:
			dbs.append(e[0])
		return dbs

	def execute_and_fetchall(self, sql):
		cur  = self.conn.cursor()
		cur.execute(sql)
		return cur.fetchall()
