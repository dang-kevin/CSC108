import unittest
import network_functions

class TestGetFamilies(unittest.TestCase):

  def test_get_families_empty(self):
    param = {}
    actual = network_functions.get_families(param)
    expected = {}
    msg = "Expected {}, but returned {}".format(expected, actual)
    self.assertEqual(actual, expected, msg)


  def test_get_families_one_person_one_friend_diff_family(self):
    param = {'Jay Pritchett': ['Claire Dunphy']}
    actual = network_functions.get_families(param)
    expected = {'Pritchett': ['Jay'], 'Dunphy': ['Claire']}
    msg = "Expected {}, but returned {}".format(expected, actual)
    self.assertEqual(actual, expected, msg)

  def test_get_families_one_person_one_friend_same_family(self):
    param = {'Jay Prichett': ['Gloria Prichett']}
    actual = network_functions.get_families(param)
    expected = {'Prichett': ['Gloria', 'Jay']}
    msg = "Expected {}, but returned {}".format(expected, actual)
    self.assertEqual(actual, expected, msg)    
  
  
  def test_get_families_one_person_multiple_friends_diff_family(self):
    param = {'Jay Pritchett': ['Claire Dunphy', 'Manny Delgado']}
    actual = network_functions.get_families(param)
    expected = {'Pritchett': ['Jay'], 'Dunphy': ['Claire'], 'Delgado': ['Manny']}
    msg = "Expected {}, but returned {}".format(expected, actual)
    self.assertEqual(actual, expected, msg)    
    
  def test_get_familiies_one_person_multiple_friends_same_family(self):
    param = {'Jay Pritchett': ['Gloria Pritchett', 'Mitchell Pritchett']}
    actual = network_functions.get_families(param)
    expected = {'Pritchett': ['Gloria', 'Jay', 'Mitchell']}
    msg = "Expected {}, but returned {}".format(expected, actual)
    self.assertEqual(actual, expected, msg)    
  
  
  def test_get_families_multiple_people_one_friend_diff_family(self):
    param = {'Haley Gwendolyn Dunphy': ['Dylan D-Money'], 'Cameron Tucker': ['Gloria Pritchett']}
    actual = network_functions.get_families(param)
    expected = {'Dunphy': ['Haley Gwendolyn'], 'D-Money': ['Dylan'], 'Tucker': ['Cameron'], 'Pritchett': ['Gloria']}
    msg = "Expected {}, but returned {}".format(expected, actual)
    self.assertEqual(actual, expected, msg)
    
  
  def test_get_families_multiple_people_one_friend_same_family(self):
    param = {'Alex Dunphy': ['Luke Dunphy'], 'Phil Dunphy': ['Claire Dunphy']}
    actual = network_functions.get_families(param)
    expected = {'Dunphy': ['Alex', 'Claire', 'Luke', 'Phil']}
    msg = "Expected {}, but returned {}".format(expected, actual)
    self.assertEqual(actual, expected, msg)
    
  
  
  def test_get_families_multiple_people_multiple_friends_mixed(self):
    param = {'Dylan D-Money': ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'], 'Claire Dunphy': ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy']}
    actual = network_functions.get_families(param)
    expected = {'D-Money': ['Dylan'], 'D-Cat': ['Chairman'], 'Dunphy': ['Claire', 'Haley Gwendolyn', 'Phil'], 'Pritchett': ['Jay', 'Mitchell']}
    msg = "Expected {}, but returned {}".format(expected, actual)
    self.assertEqual(actual, expected, msg)    
  
  
  def test_get_families_multiple_people_multiple_friends_same_family(self):
    param = {'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'], 'Alex Dunphy': ['Luke Dunphy', 'Claire Dunphy']}
    actual = network_functions.get_families(param)
    expected = {'Dunphy': ['Alex', 'Claire', 'Luke', 'Phil']}
    msg = "Expected {}, but returned {}".format(expected, actual)
    self.assertEqual(actual, expected, msg)    



if __name__ == '__main__':
    unittest.main(exit=False)