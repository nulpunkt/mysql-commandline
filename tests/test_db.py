import sys
import unittest
from src import db

class MySQLTest(unittest.TestCase):
	def test_map(self):
		fixture = (('information_schema',), ('nulpunkt_db',), ('nulpunkt_fgdb',), ('nulpunkt_timereg',)) 
		mysql = db.MySql()
		result = mysql.map_database_result(fixture);

		self.assertEquals(['nulpunkt_db', 'nulpunkt_fgdb', 'nulpunkt_timereg'], result);

if __name__ == '__main__':
	unittest.main()
