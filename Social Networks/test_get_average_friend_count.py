import unittest
import network_functions

class TestGetAverageFriendCount(unittest.TestCase):

  def test_get_average_empty(self):
    param = {}
    actual = network_functions.get_average_friend_count(param)
    expected = 0.0
    msg = "Expected {}, but returned {}".format(expected, actual)
    self.assertEqual(actual, expected, msg)


  def test_get_average_one_person_one_friend(self):
    param = {'Jay Pritchett': ['Claire Dunphy']}
    actual = network_functions.get_average_friend_count(param)
    expected = 1.0
    msg = "Expected {}, but returned {}".format(expected, actual)
    self.assertEqual(actual, expected, msg)  
    
    
  def test_get_average_one_person_multiple_friends(self):
    param = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado']}
    actual = network_functions.get_average_friend_count(param)
    expected = 3.0
    msg = "Expected {}, but returned {}".format(expected, actual)
    self.assertEqual(actual, expected, msg)    
    
  
  def test_get_average_multiple_people_one_friend(self):
    param = {'Jay Pritchett': ['Claire Dunphy'], 'Alex Dunphy': ['Luke Dunphy'], 
             'Haley Gwendolyn Dunphy': ['Dylan D-Money']}
    actual = network_functions.get_average_friend_count(param)
    expected = 1.0
    msg = "Expected {}, but returned {}".format(expected, actual)
    self.assertEqual(actual, expected, msg)  
    
    
  def test_get_average_multiple_people_multiple_friends(self):
    param = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado'], 
             'Claire Dunphy': ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy'], 
             'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'],
             'Cameron Tucker': ['Gloria Pritchett', 'Mitchell Pritchett']}
    actual = network_functions.get_average_friend_count(param)
    expected = 2.75
    msg = "Expected {}, but returned {}".format(expected, actual)
    self.assertEqual(actual, expected, msg)     
  
    
if __name__ == '__main__':
    unittest.main(exit=False)