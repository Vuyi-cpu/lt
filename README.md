Vuyisa Msipa

This program identifies the column positions of the “Student Number” and “Mark” fields in a CSV file and uses this information to determine the top-performing student based on their mark. The program dynamically reads the header row to locate the correct columns, allowing it to work with different column orders across datasets. It then processes the remaining rows to find the student with the highest mark. Two unit tests were written using the unittest framework to verify both the column detection and top student functionality. The tests were implemented in a separate file to improve scalability and support future testing. Initial bugs were identified where loop counters in both functions were not being incremented correctly; these were fixed by properly updating the iterators within each loop. Development and testing were carried out on a separate branch to ensure the main branch remained stable.

To run the code: python3 getbest.py 
To run the tests: python3 -m unittest test_gettopstudent.py & python3 -m unittest test_getcolumnwithdata.py


