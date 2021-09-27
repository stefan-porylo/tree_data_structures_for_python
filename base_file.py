class BinaryTree(object):
	"""class that creates binary trees"""
	def __init__(self, value):
		self.value = value
		self.left_child = None
		self.right_child = None

	def insert_left(self, value):
		if self.left_child == None:
			self.left_child = BinaryTree(value)
		else:
			new_node = BinaryTree(value)
			self.left_child = new_node

	def insert_right(self, value):
		if self.right_child == None:
			self.right_child = BinaryTree(value)
		else:
			 new_node = BinaryTree(value)
			 self.right_child = new_node


a_node = BinaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')

# b_node = a_node.left_child
# b_node.insert_right('d')

# c_node = a_node.right_child
# c_node.insert_right('f')
# c_node.insert_left('e')


print(a_node.value)
print(type(a_node))

print('-' * 15)
