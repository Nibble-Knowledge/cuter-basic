#!/usr/bin/python
import sys
import os

keywords = {
	'lang' 		: 	'shorthand', 
	'dialects' 	: 	'', 
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
		
	print "Using language " + keywords['lang'] + "",
	if keywords['dialects'] != "":
		print " specifically dialects " + keywords['dialects']
	
