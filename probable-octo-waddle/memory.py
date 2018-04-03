# class written by Carter Davis
class memory:
	def __init__(self):
		self.length = 100
		self.values = [0 for i in range(self.length)]

	def __getitem__(self, i):
		return self.values[i] 

	def __setitem__(self, i, value):
		self.values[i] = value

	def __str__(self):
		retVal = ""
		for i in range (11):
			if i > 0:
				retVal += str('{:>7}'.format(i-1))
			else:
				retVal += str('{:>7}'.format(""))

		retVal += "\n\n"

		for i in range (0, self.length, 10):
			retVal += str('{:>7}'.format(i))
			for j in range(0, 10, 1):
				retVal += str('{:>7}'.format(self.values[i + j]))
			retVal += "\n"
		return str(retVal)
		
