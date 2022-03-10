from hashlib import new
import unittest
from modules import Activity
from modules import ToDo

class Test_Activity(unittest.TestCase):
    def test_min_length_title(self):
        act = Activity('more than 5 chars')

        with self.assertRaises(ValueError):
            act.setTitle('less')

        with self.assertRaises(ValueError):
            act2 = Activity('less')


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
        self.assertEqual(newManager.list, [])

    def test_remove_from_list(self):
        newManager = ToDo()
        with self.assertRaises(IndexError):
            newManager.remove(5)
        with self.assertRaises(IndexError):
            newManager.remove(0)
        with self.assertRaises(IndexError):
            newManager.remove(-1)
        with self.assertRaises(TypeError):
            newManager.remove('a')


    def test_edit_from_list(self):
        newManager = ToDo()
        with self.assertRaises(IndexError):
            newManager.editTitle(5, '123456')
        with self.assertRaises(IndexError):
            newManager.editTitle(0, '123456')
        with self.assertRaises(IndexError):
            newManager.editTitle(-1, '123456')
        with self.assertRaises(TypeError):
            newManager.editTitle('a')
        with self.assertRaises(ValueError):
            newManager.add('123456')
            newManager.editTitle(0, 'less')



    def test_toggle_done(self):
        newManager = ToDo()
        with self.assertRaises(IndexError):
            newManager.toggleDone(5)
        with self.assertRaises(IndexError):
            newManager.toggleDone(0)
        with self.assertRaises(IndexError):
            newManager.toggleDone(-1)
        with self.assertRaises(TypeError):
            newManager.toggleDone('a')


if __name__ == '__main__':
    unittest.main()