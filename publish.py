"""
Publish to GitHub
"""

import os
import sys


def create(name):
    c = ["git init",
         "git add .",
         'git commit -m "first commit"',
         f"git remote add origin https://github.com/TomDeneire/{name}.git",
         "git push -u origin master"]
    for x in c:
        os.system(x)


def commit():
    print("Type your commit message (c: to create first, or q: to quit): ")
    message = input()

    if message == "c:":
        print("Type your respository name: ")
        name = input()
        create(name)
        with open(".gitignore", 'w') as gitignore:
            gitignore.write("publish.py")
        commit()

    if message == "q:":
        sys.exit(0)
    else:
        c = ['git add .', f'git commit . -m "{message}"', 'git push']
        for x in c:
            os.system(x)


if __name__ == "__main__":
    commit()
