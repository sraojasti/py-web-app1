Testing Setup
Add tests directory to the src directory and then create following files
**init**.py
conftest.py
pytest.ini
test_config.py
test_ping.py

pytest will autodiscover test files that start or end with test (test\__.py or _\_test.py)

Test functions must begin with test\_
Test classes must also begin with Test
