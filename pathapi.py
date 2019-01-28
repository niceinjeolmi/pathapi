#!/usr/bin/env python
#coding:utf8
import re

path = "/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.nk"

def project(path):
	"""
	경로를 넣으면 project 이름을  반환한다.
	"""
	p = re.findall('/project/(\S[^/]+)', path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 project 정보를 가지고 올 수 없습니다."
	return p[0], None

def seq(path):
	"""
	경로를 넣으면 seq 이름을 반환한다.
	"""
	p = re.findall('/shot/(\S[^/]+)', path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 seq 정보를 가지고 올 수 없습니다"
	return p[0], None

def shot(path):
	"""
	경로를 넣으면 shot 이름을 반환한다.
	"""
	p = re.findall('/shot/\w+/(\w+)', path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 shot 정보를 가지고 올 수 없습니다"
	return p[0], None
	
def task(path):
	"""
	경로를 넣으면 task 이름을 반환한다.
	"""
	p = re.findall('/shot/\w+/\w+/(\w+)', path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 task 정보를 가지고 올 수 없습니다"
	return p[0], None

def ver(path):
	"""
	경로를 넣으면  version을 반환한다.
	"""
	p = re.findall("_v(\d+)",path)
	if len(p) != 1:
		return -1, "경로에서 버전 정보를 가지고 올 수 없습니다"
	return int(p[0]), None

def seqnum(path):
	"""
	경로를 넣으면 seq number를 반환한다.
	"""
	p = re.findall('\.(\d+)\.', path.replace("\\","/"))
	if len(p) != 1:
		return -1, "경로에서 seq number 정보를 가지고 올 수 없습니다"
	return int(p[0]), None

#test.py가 없다면?
#if __name__ == "__main__":
	#path = "/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.nk"
	#projectName, err = project(path)
	#if err:
		#print err
	#print projectName
