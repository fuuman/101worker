#! /usr/bin/env python

import os
import sys
import json

sys.path.append('../../libraries/101meta')
import const101
import tools101

wikiDump = json.load(open(const101.wikiDump, 'r'))
mappings = json.load(open('../../libraries/mediawiki/Mappings.json'))['wikify']



def findNamespaceMembers(namespace, instanceof):
    members = []
    for page in wikiDump['wiki']['pages']:
        pageData = page['page']
        if pageData['page']['p'] == namespace and not pageData['page']['n'] == namespace:
            if (instanceof and instanceof in pageData.get('instanceOf',[])) or not instanceof:
                members.append(pageData['page']['n'])
    members.sort()
    return [s.encode('latin_1') for s in members]
    #return members

def findAndWrite(dirname, namespace, instanceof=None):
    members = findNamespaceMembers(namespace, instanceof)
    path = os.path.join(const101.tRoot, dirname, 'members.json')
    tools101.makedirs(os.path.dirname(path))
    json.dump(members, open(path, 'w'))

print "Trying to find namespaces..."

for folderName in mappings.keys():
    namespace = mappings[folderName]
    if namespace == '':
        namespace = None
    findAndWrite(folderName, namespace)

findAndWrite('',              'Namespace', {'p': 'Namespace', 'n': 'Namespace'})