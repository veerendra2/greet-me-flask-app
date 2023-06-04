import unittest
from datetime import datetime
from greet_me import greet_client

class GreetClientTestCase(unittest.TestCase):

    def test_greet_client_morning(self):
        # Test case for morning time
        client_time = "2023-06-04T08:00:00.000Z"
        expected_greeting = "Good morning!"
        self.assertEqual(greet_client(client_time), expected_greeting)

    def test_greet_client_afternoon(self):
        # Test case for afternoon time
        client_time = "2023-06-04T14:00:00.000Z"
        expected_greeting = "Good afternoon!"
        self.assertEqual(greet_client(client_time), expected_greeting)

    def test_greet_client_evening(self):
        # Test case for evening time
        client_time = "2023-06-04T20:00:00.000Z"
        expected_greeting = "Good evening!"
        self.assertEqual(greet_client(client_time), expected_greeting)

    def test_greet_client_invalid_time(self):
        # Test case for invalid time format
        client_time = "2023-06-04T18:00:00Z"  # Missing milliseconds
        with self.assertRaises(ValueError):
            greet_client(client_time)

    def test_greet_client_future_time(self):
        # Test case for future time
        current_time = datetime.now()
        future_time = current_time.replace(year=current_time.year + 1)
        client_time = future_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

        if future_time.time() < datetime.strptime('12:00', '%H:%M').time():
            expected_greeting = "Good morning!"
        elif future_time.time() < datetime.strptime('18:00', '%H:%M').time():
            expected_greeting = "Good afternoon!"
        else:
            expected_greeting = "Good evening!"

        self.assertEqual(greet_client(client_time), expected_greeting)

if __name__ == '__main__':
    unittest.main()
