#manage.py
from flask.cli import FlaskGroup
from src import app, db

cli = FlaskGroup(app)

#Register recreate_db command to the cli.  This allows to run recreate_db from command line
@cli.command('recreate_db')
def recreate_db():
  db.drop_all()
  db.create_all()
  db.session.commit()

if __name__ == '__main__':
  cli()

