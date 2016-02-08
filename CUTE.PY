#!/usr/bin/python
import sys
import os

keywords = {
	'lang' 		: 	'shorthand', 
	'dialects' 	: 	'none', 
	'use' 		: 	'use', 
	'def' 		: 	'def',
	'bef' 		: 	'bef',
	'aft' 		: 	'aft',
	'ret' 		: 	'ret',
	'incl' 		:	'incl',
	'asm'		:	'asm',
	'asmstart'	:	'asmstart',
	'asmend'	:	'asmend',
	'start'		:	'start',
	'end'		:	'end',
	'var'		:	'var',
	'stmt'		:	'stmt',
	'ig'		:	'ig',
	'exit'		:	'exit',
	'let'		:	'let',
	'='			:	'=',
	'is'		:	'is',
	'if'		:	'if',
	'elif'		:	'elif',
	'else'		:	'else',
	'endif'		:	'endif',
	'while'		:	'while',
	'endwhile'	:	'endwhile',
	'breakloop'	:	'breakloop',
	'breakif'	:	'breakif',
	'lbl'		:	'lbl',
	'goto'		:	'goto'
}

useage = {}

if __name__ == "__main__":
	if len(sys.argv) > 1:
		with open(sys.argv[1]) as f:
			for line in f:
				replaces = line.split()
				if len(replaces) > 1:
					if keywords.get(replaces[0].strip()) != None:
						if replaces[0].strip() == 'lang' or replaces[0].strip() == 'dialects':
							keywords[replaces[0].strip()] = replaces[1].strip()
						else:
							keywords[replaces[1].strip()] = keywords[replaces[0].strip()]
							del keywords[replaces[0].strip()]
	print "Using language " + keywords['lang'],
	if keywords['dialects'] != "":
		print "specifically dialects " + keywords['dialects']
		print keywords
		
