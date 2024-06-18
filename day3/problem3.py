# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
#
# For example, given the following Node class
#
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'
DELIMITER = "#"
class Codec:
    def serialize(self,root):

        def traverse(node):
            if node:
                temp_vals.append(str(node.val))
                traverse(node.left)

        temp_vals = []
        traverse(root)
        return ' '.join(temp_vals)

    def deserialize(self,data):

        def build():
            val = next(temp_vals)
            if val == DELIMITER:
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        temp_vals = iter(data.split())
        return build()

