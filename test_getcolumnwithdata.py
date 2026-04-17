
import unittest
import getbest


class test_getColumns(unittest.TestCase): #changed the ; to :#
      def test_getCols(self): # tests given data in the csv
        f = open("bestdat0.csv", "r") #opens file in the directory#
        #change edit from oPen to open#
        num_col, mark_col = getbest.getCols(f)
        f.close()# good coding practice to close files to avoid system resources getting wasted like memory#
        self.assertEqual(num_col, 1)
        self.assertEqual(mark_col, 2) #changed mark from capital to lowercase#

      def test_getColumn_differentorder(self): # tests csv with get colums in a different order#
        f = open("Different_order_columns.csv", "r")# added .csv to file name and changed the apostrophe from '' to ""#
        num_col, mark_col = getbest.getCols(f)
        f.close()
        self.assertEqual(num_col, 2)# fixed column numbers expexted as return#
        self.assertEqual(mark_col, 0)# fixed column numbers expexted as return#

      if __name__ == '__main__': #removed extra underscores#
       unittest.main()
  