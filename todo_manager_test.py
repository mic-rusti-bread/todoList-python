import unittest
from modules import *
from modules import Activity
from modules import ToDo

class Test_Activity(unittest.TestCase):
    def test_min_length_title(self):
        act = Activity('more than 5 chars')
        with self.assertRaises(ValueError):
            act.title = 'less'

        with self.assertRaises(ValueError):
            act2 = Activity('lss')


    def test_default_done(self):
        act = Activity('thisIsActivity')
        self.assertFalse(act.done)

    def test_toggle_done(self):
        act = Activity('thisIsActivity')
        act.setToggleDone()
        self.assertTrue(act.done)
        

class Test_ToDo(unittest.TestCase):
    def test_load_from_storage(self):
        newManager = ToDo()

        #non passo nessun file 
        with self.assertRaises(FileNotFoundError):
            newManager.loadFromStorage()
        


if __name__ == '__main__':
    unittest.main()