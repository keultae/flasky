#!/usr/bin/env python
import os
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)
# 유닛 테스트는 @manager.command를 사용하여 manager.py에 커스텀 커맨드로 추가 되어서
# ./manager.py test로 실행할 수 있다.
# 커스텀 커맨드가 추가로 필요하면 @manager.command를 사용하면 됩니다.

if __name__ == '__main__':
    manager.run()
