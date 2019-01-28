#!/usr/bin/env python
#coding:utf8
import unittest
from pathapi import *

class Test_path(unittest.TestCase):
	def test_project(self):
		self.assertEqual(project("/project/circle"), ("circle", None))
		self.assertEqual(project("/project/circle/"), ("circle", None))
		self.assertEqual(project("\\\\10.20.30.40\\project\\circle\\"), ("circle", None))
		self.assertEqual(project("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001,nk"), ("circle", None))

	def test_seq(self):
		self.assertEqual(seq("/project/circle/shot/FOO"), ("FOO", None))
		self.assertEqual(seq("/project/circle/shot/FOO/"), ("FOO", None))
		self.assertEqual(seq("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.nk"), ("FOO", None))

	def test_shot(self):
		self.assertEqual(shot("/project/circle/shot/FOO/0010"), ("0010", None))
		self.assertEqual(shot("/project/circle/shot/FOO/0010/"), ("0010", None))
		self.assertEqual(shot("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.nk"), ("0010", None))

	def test_task(self):
		self.assertEqual(task("/project/circle/shot/FOO/0010/comp"), ("comp", None))
		self.assertEqual(task("/project/circle/shot/FOO/0010/comp/"), ("comp", None))
		self.assertEqual(task("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.nk"), ("comp", None))

	def test_ver(self):
		self.assertEqual(ver("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.nk"), (1, None))

	def test_seqnum(self):
		self.assertEqual(seqnum("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.1001.exr"), (1001, None))

if __name__ == "__main__":
	unittest.main()
