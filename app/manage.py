from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from main import app, db

POSTGRES = {
    'user': 'postgres',
    'pw': 'Sakura23!',
    'db': 'app',
    'host': 'localhost',
    'port': '5432',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Sakura23!@localhost:5432/app'

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()