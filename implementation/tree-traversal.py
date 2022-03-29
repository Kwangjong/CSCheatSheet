class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val


#  self -> left -> right
def pre_order(node):
	if node is None:
		return ""
	
	output = node.val
	output += pre_order(node.left)
	output += pre_order(node.right)
	
	return output

# left -> self -> right
def in_order(node):
	if node is None:
		return ""
	
	output = pre_order(node.left)
	output += node.val
	output += pre_order(node.right)
	
	return output

# right -> left -> self
def post_order(node):
	if node is None:
		return ""

	output = node.val
	output += pre_order(node.right)
	output += pre_order(node.left)
	
	return output

# implement using queue
def level_order(root):
	queue = [root]

	output = ""
	while len(queue) > 0:
		curr = queue.pop()

		if curr is not None:
			output += curr.val

			queue.insert(0, curr.left)
			queue.insert(0, curr.right)
	
	return output


# build tree:
#        A   
#      /   \
#    B       C
#   / \     / \
#  D   E   F   G
#     / \     /
#    H   I   J
root = Node("A")

curr = root #A
curr.left = Node("B")
curr.right = Node("C")

curr = root.left #B
curr.left = Node("D")
curr.right = Node("E")

curr = curr.right #E
curr.left = Node("H")
curr.right = Node("I")

curr = root.right #C
curr.left = Node("F")
curr.right = Node("G")

curr = curr.right	#G
curr.left = Node("J")




# run traversal methods
print(pre_order(root))  #ABDEHICFGJ
print(in_order(root))   #BDEHIACFGJ
print(post_order(root)) #ACFGJBDEHI
print(level_order(root)) #ABCDEFGHI