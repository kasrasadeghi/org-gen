#!/bin/bash
input=docs
temp=fixdocs
output='output'
output_regex='output'  # escaped for sed


rm -rf "$output"
cp -r "$input" "$temp"

ag '\[\[(?!http)[^ /].*?\]' "$temp"
ag -l '\[\[(?!http)[^ /].*?\]' "$temp" | \
    while read line; do ./fixname.py "$line"; done


cp -r "$temp" "$output"
find "$output" -iname '*.org' | while read l; do rm "$l"; done
find "$temp" -iname '*.org' | \
    while read l; do
        output_file=`echo "$l" | sed "s/^$temp/$output_regex/;s/.org$/.html/;s/README/index/"`
        pandoc "$l" -s -o $output_file > /dev/null
    done

rm -rf "$temp"
