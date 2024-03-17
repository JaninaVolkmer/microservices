# migrate the models from main

from main import app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

migrate = Migrate(app, db)

manager = Manager(app)
# db command to run migrations
manager.add_command("db", MigrateCommand)


if __name__ == "__main__":
    manager.run()
