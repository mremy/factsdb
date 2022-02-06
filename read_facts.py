#!/usr/bin/python3
# -*- coding: utf-8 -*-
# SOF

import getopt
import json
import sys
import yaml

# https://oznetnerd.com/2017/05/21/understanding-ansible-output-structure/

# https://stackoverflow.com/questions/10540712/reading-a-json-response-recursively-with-python

def read_dict(c_level, m_dict ):
	print(f"\n{c_level} :d: {m_dict}\n")
	for clef,valeur in m_dict.items():
		if( isinstance(valeur,dict) is True):
			read_dict(f"{c_level}#{clef}",valeur)
		elif( isinstance(valeur,list) is True):
			read_list(f"{c_level}#{clef}",valeur)
		elif( isinstance(valeur,str) is True or isinstance(valeur,int) or isinstance(valeur,bool) ):
			print(f"niveau: {c_level} <> Clef {clef}: {valeur} <> {type(valeur)}")
		else:
			print(f"Type:d clef {clef}  {type(valeur)}")

def read_list(c_level, m_list):
	print(f"\n{c_level} :l: {m_list}\n")
	for valeur in m_list:
		if( isinstance(valeur,dict) is True):
			read_dict(f"{c_level}#list",valeur)
		elif( isinstance(valeur,list) is True):
			read_list(f"{c_level}#list",valeur)
		elif( isinstance(valeur,str) or isinstance(valeur,int) or isinstance(valeur,bool) ):
			print(f"niveau: {c_level} <> {valeur} <> {type(valeur)}")
		else:
			print(f"Type:l {type(valeur)} # valeur")

# __main__
def main( argv ):
	# Default value
	inputfile = "facts.json"
	try:
		opts, args = getopt.getopt(argv,"hi:",["ifile="])
	except getopt.GetoptError:
		print( f"{sys.argv[0]} -i <inputfile>" )
		sys.exit(2)
	for opt, arg in opts:
		if opt in ('-h', "--help"):
			print( "Read the code dude!" )
		elif opt in ("-i", "--ifile"):
			inputfile = arg

	with open( inputfile ) as fd:
		data = fd.read()
		facts = json.loads(data)
		print(f"Format facts: {type(facts)}")
		print(f"Instance dict: {isinstance(facts,dict)}")
		read_dict("root", facts)

	sys.exit(0)

if __name__ == "__main__":
   main(sys.argv[1:])

# vim: set tabstop=4 autoindent fileencoding=utf-8 :
# EOF
