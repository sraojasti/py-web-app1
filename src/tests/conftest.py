#src/tests/conftest.py

"""
Fixtures are reusable objects for tests.
They have scope associated with them which indicate how often the fixture is invoked.
1.  function - Once per test function (default)
2.  class - once per test class
3.  module -- once per test module
4. session -- once per test session
More details about fixtures - Testing Flask Application with Pytest
"""

import pytest

from src import app, db

@pytest.fixture(scope='module')
def test_app():
  app.config.from_object("src.config.TestingConfig")
  with app.app_context():
    yield app # testing happens here

@pytest.fixture(scope='module')
def test_database():
  db.create_all()
  yield db  #testing heppens here
  db.session.remove()
  db.drop_all()

