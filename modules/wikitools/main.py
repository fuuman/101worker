# -*- coding: utf-8 -*-

import pprint # Used for formatting the output for viewing, not necessary for most code
from wikitools import wiki, api, page
import re
import random, string
from document import Section
from pipeline import Pipeline, Step
from utils import *

site = wiki.Wiki('http://101companies.org/api.php')
params = {'action':'query',
    'titles':'101implementation:syb'
}
req = api.APIRequest(site, params)
res = req.query(querycontinue=True)
pprint.pprint(res)

wikipage = page.Page(site, title='101implementation:syb')
wikidata = wikipage.getWikiText(True).decode('utf-8', 'replace')
#pprint.pprint(wikidata)

OUTPUT_BASE = "tex/"

def rand_string(length=10, chr_set=string.ascii_uppercase + string.digits):
	output = ''
	for n in range(length):
		output += random.choice(chr_set)
	return output

def page2sections(page):
	l = page.split("==")
	l.pop(0)
	#print len(l[::2])
	#print len(l[1::2])
	zipped = zip(l[::2], l[1::2])
	doc = []
	for s in zipped:
	 	title = s[0].strip()
	 	print title
	 	content  = s[1].strip()
	 	if title.startswith('='):
	 		sec = doc[-1]
	 		sec.addSubsection(Section(title.strip().replace('=','').strip(), content))
	 	else:
	 		doc.append(Section(title, content))

	return doc		

def extractSourceFragments(page):
	for section in page:
		#print section.title
		#print section.content
		#for every section extract the source code fragments into a separate file
		pattern = '<syntaxhighlight\slang="(.*?)">(.*?)<\/syntaxhighlight>'; 
		rg = re.compile(pattern,re.IGNORECASE|re.DOTALL|re.MULTILINE)
		print section.title
		for source in rg.findall(section.content):
			#print str(source[1])
			fname = rand_string() + '.src'
			sourceText = str(source[1])
			f = open(OUTPUT_BASE+'/sources/' + fname, 'w')
			f.write(sourceText)
			f.close()
			replacement = '\lstinputlisting[xleftmargin=5pt, language=' + str(source[0]) +']{\\texgen/sources/' + fname + '}' 
			#print "TO REPLACE: " + rg.search(section.content).group(0)
			section.content = section.content.replace(rg.search(section.content).group(0),replacement)
			#print "NEW: " + section.content

		if(len(section.subsections) > 0):	
			print "Processing subsections..."
			extractSourceFragments(section.subsections)

	return page	

def page2tex(page):
	tex = ''
	cmd_prefix = 'LanguageMeta'
	for section in page:
		tex += '\\newcommand{\\'+ cmd_prefix + getTexCommandName(section.title) +'}{'
		tex += section.content + '}\n'
		if(len(section.subsections) > 0):
			for section in section.subsections:
				tex += '\n\\newcommand{\\' + cmd_prefix + getTexCommandName(section.title) +'}{'
				tex += section.content + '}\n'		
	return tex			

def main():
	pileline = Pipeline()
	step1 = Step(page2sections, "Extract sections from the page")
	pileline.addStep(step1)
	pileline.addStep(Step(extractSourceFragments, "Extract source fragments from the sections into separate files"))
	pileline.addStep(Step(page2tex, "Generate final tex for the page"))

	doc = pileline.execute(wikidata)
	f = open(OUTPUT_BASE+'macros.tex', 'w')
	f.write(toTex(doc))
	f.close()

if __name__ == "__main__":
	main()


