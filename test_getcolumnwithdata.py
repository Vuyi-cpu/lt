import unittest
import getbest


class test_getColumns(unittest.TestCase):
      def test_getCols(self): # tests given data in the csv
        f = open("bestdat0.csv", "r")
        num_col, mark_col = getbest.getCols(f)
        f.close()
        self.assertEqual(num_col, 1)
        self.assertEqual(mark_col, 2)

      def test_getCols(self): # tests csv with get colums in a different order
        f = open("Different_order_columns", "r")
        num_col, mark_col = getbest.getCols(f)
        f.close()
        self.assertEqual(num_col, 3)
        self.assertEqual(mark_col, 1)

      if __name__ == '__main__':
       unittest.dev()
  