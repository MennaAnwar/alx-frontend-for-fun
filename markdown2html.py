#!/usr/bin/python3

"""
Markdown script using python.
"""

import sys
import os
import markdown2

def convert_markdown_to_html(input_file, output_file):
    try:
        with open(input_file, 'r') as markdown_file:
            markdown_content = markdown_file.read()
            html_content = markdown2.markdown(markdown_content)
            with open(output_file, 'w') as html_file:
                html_file.write(html_content)
    except FileNotFoundError:
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

if len(sys.argv) != 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(input_file):
    sys.stderr.write(f"Missing {input_file}\n")
    sys.exit(1)

convert_markdown_to_html(input_file, output_file)
sys.exit(0)
