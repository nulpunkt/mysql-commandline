from src import db, state, shell

# Bootstrap the app, and start the eventloop
mysql = db.MySql()
mysql.connect()
path = state.Path(mysql)
prg = shell.InteractiveShell(path)
prg.cmdloop()
mysql.close()
