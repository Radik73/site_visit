from xml.dom.minidom import *

def parse(object):
	test = xml.dom.minidom.parse("content.xml")
	data = test.getElementsByTagName(object)[0].childNodes[0]
	return data