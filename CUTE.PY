#!/usr/bin/python
import sys
import os

namestr = 'CUTEBASIC'

version = '2.0a'

keywords = {
	'lang' 		: 	'shorthand', 
	'dialects' 	: 	'none', 
	'use' 		: 	'use', 
	'def' 		: 	'def',
	'bef' 		: 	'bef',
	'aft' 		: 	'aft',
	'ret' 		: 	'ret',
	'opt'		:	'opt',
	'newline'	:	'newline',
	'0+'		:	'0+',
	'1+'		:	'1+',
	'choose'	:	'choose',
	'incl' 		:	'incl',
	'name'		:	'name',
	'none'		:	'none',
	'asm'		:	'asm',
	'asmstart'	:	'asmstart',
	'cbstart'	:	'cbstart',
	'asmend'	:	'asmend',
	'cbend'		:	'cbend',
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

useage = {
	'def' : {
			'bef' : ['none'], 
			'aft' : [
					'newline', 'use', 'stmt', 
					'newline', 'bef', '1+', 'var', 
					'newline', 'aft', '1+', 'var',
					'newline', 'ret', '1+', 'var',
					'newline', 'choose', 'asmstart', 'cutestart'
					'newline', '1+', 'stmt',
					'newline', 'choose', 'asmend', 'cuteend'
			],
			'ret' : ['none'],
			'use' : ""
	}
	
}

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
							keywords[replaces[1].strip()] = replaces[0].strip()
							keywords[replaces[0].strip()] = replaces[1].strip()
						if len(replaces) > 2:
							if keywords.get(replaces[2].strip()) == 'use':
								if useage.get(replaces[0].strip()) == None:
									useage[replaces[0].strip()] = {'bef' : [], 'aft' : [], 'ret' : [], 'use': "" }
								useage[replaces[0].strip()]['use'] = " ".join(replaces[3:])
	print namestr + " " + version + " for " + keywords['lang'],
	if keywords['dialects'] != "":
		print "- " + keywords['dialects']

def printuseage( key ):
	

