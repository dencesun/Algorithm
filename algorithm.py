#! /usr/bin/env python
# -*- coding: utf-8 -*-

# class Tree():
# 	def __init__(self, ltree = 0, rtree = 0, data = 0):
# 		self.data = data
# 		self.ltree = ltree
# 		self.rtree = rtree

# class Btree():
# 	def __init__(self, base = 0):
# 		self.base = base
# 	def _Empty(self):
# 		if self.base == 0:
# 			return True
# 		else:
# 			return False
# 	def qout(self, tree_base):
# 		if tree_base == 0:
# 			return
# 		print tree_base.data
# 		self.qout(tree_base.ltree)
# 		self.qout(tree_base.rtree)

# tree1 = Tree(data = 8)
# tree2 = Tree(data = 9)
# tree3 = Tree(tree1, data = 6)
# tree4 = Tree(tree2, 0, data = 7)
# base = Tree(tree3, tree4, 5)
# btree = Btree(base)
# btree.qout(base)

class Node(object):
	def __init__(self, elem = -1, lchild = None, rchild = None):
		self.elem = elem
		self.lchild = lchild
		self.rchild = rchild

class Tree(object):
	def __init__(self):
		self.root = Node()

	def add(self, elem):
		node = Node(elem)
		if self.root.elem == -1:
			self.root = node
		else:
			myQueue = []
			treeNode = self.root
			myQueue.append(treeNode)
			while myQueue:
				treeNode = myQueue.pop(0)
				if treeNode.lchild == None:
					treeNode.lchild = node
					return 
				elif treeNode.rchild == None:
					treeNode.rchild = node
					return 
				else:
					myQueue.append(treeNode.lchild)
					myQueue.append(treeNode.rchild)
	def preprint(self, root):
		if root == None:
			return
		print root.elem
		self.preprint(root.lchild)
		self.preprint(root.rchild)

btree = Tree()
btree.add(1)
btree.add(2)
btree.add(3)
btree.preprint(btree.root)





























