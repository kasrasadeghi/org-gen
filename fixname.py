#!/usr/local/bin/python3
"""
script to fix relative links during documentation generation

called like ag -l '\[\[(?!http)[^ /].*?\]' "$temp" | while read l; do ./fixname.py "$l"; done
"""
import re
import sys
_, *files = sys.argv

http_path = '/docs/'
local_path = 'fixdocs/'

for filename in files:
    print(" ", filename)
    split = filename.rsplit('/', 1)
    basename = split[1] if len(split) == 2 else ""
    parent = filename[len(local_path):-len(basename)]
    with open(filename, "r") as f:
        c = f.read()
        matches = re.findall('\[\[(?!http)[^ /].*?\]', c)
        for match in matches:
            linked_filename = match[2:-1]
            replacement = '[[http:' + http_path + parent + linked_filename + ']'
            print("    ", match, '->', replacement)
            c = c.replace(match, replacement)
    with open(filename, 'w') as f:
        f.write(c)
