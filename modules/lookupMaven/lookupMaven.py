import os
import json

def run(context, c):
    # dispatch the modified file
    if c['type'] == 'NEW_FILE':
        print(context, c['file'])
    elif c['type'] == 'FILE_CHANGED':
        print(context, c['file'])
    else: 
        print(context, c['file'])
