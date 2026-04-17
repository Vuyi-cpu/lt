import unittest
import getbest

class test_getTopStudent(unittest.TestCase):
  def test_findTop(self):#tests given data in the csv
        data =  open("bestdat0.csv", "r")
        num_c0l, mark_col = getbest.getCols(data)
        best__idx, best = getbest.findTop(data, num_col, mark_col)
        data.close()
        self.assertEqual(best_idx, 2)
        self.assertEqual(best, 90)
       
  def test_findTop(self):#tests given data in the csv
        data =  open("bestdat0.csv", "r")
        num_col, mark_col = getbest.getCols(data)
        best_idx, best = getbest.findTop(data, num_col, mark_col)
        data.close()
        self.assertEqual(best_idx, 2)
        self.assertEqual(best, 900)




if __name__ == '__main__':
  unittest.dev()