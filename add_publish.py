"""
This script prepends the dg-garden = true property
to the front of each .md file in the working directory

Written by ChatGPT https://chatgpt.com/c/66e4ca97-1f58-8013-81b0-171686804711

Zachary Keyes 9/13/2024
"""

import os

# Define the front matter to add
front_matter = """---
dg-publish: true
---
"""

# Loop through all files in the current directory
for filename in os.listdir():
    # Only process .md files
    if filename.endswith('.md'):
        with open(filename, 'r+') as file:
            content = file.read()
            # Add the front matter if it isn't already present
            if "dg-publish: true" not in content:
                # Go back to the beginning of the file and prepend the front matter
                file.seek(0)
                file.write(front_matter + content)
