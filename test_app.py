import unittest
from app import hello_world

class TestHellloWorld(unittest.TestCase) : 
def test_hello_world_message(self):
  self.assertEqual ( hello_world(),     "Hello, Devops!" ) 
  
  if__name__ == "__main__": 
  unittest.main()
