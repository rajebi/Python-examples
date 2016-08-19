
print ("hello world")

# simple rectangle class
class Rectangle:

	def __init__(self, len, width):
		self.len = len
		self.width = width
	
	def area(self):
		ar = self.len * self.width
		return ar


rec = Rectangle(10,5)
print ("area = ", rec.area())

#---------------------------------
# File read and print
#---------------------------------
class FileRead:
	def __init__(self, filename):
		file = open(filename, 'r') # note "file" is a in-built class
		val = file.read().split(',')
		self.val = val           # val is a member in class FileRead
		
	def	printVal(self,i,j):
		self.test = 0            # test is another member
		print(self.val[i][j]) 

TestFile = FileRead("test1.csv")
i = 0;
while i < 7:
	TestFile.printVal(i,0)
	i = i + 1
