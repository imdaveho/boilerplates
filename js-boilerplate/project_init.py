import getpass
import argparse
from os import path
from string import Template

dirname = path.relpath(".", "..")
username = getpass.getuser()

parser = argparse.ArgumentParser("Initialize a boilerplate package.json")
parser.add_argument('-n', '--project_name', nargs="?", const=dirname, default=dirname)
parser.add_argument('-d', '--project_description', nargs="?", const="", default="")
parser.add_argument('-a', '--author', nargs="?", const=username, default=username)
parser.add_argument('-l', '--license', nargs="?", const="MIT", default="MIT")

args = vars(parser.parse_args())

try:
    filein = open('./package.json', 'r+')
    source = Template(filein.read())
    filein.seek(0)
except IOError:
    print("File does not exist\nCreating new package.json...\n")
    filein = open('./package.json', 'w')
    source = Template("""
    {
        "name": "${project_name}",
        "version": "0.0.1",
        "description": "${project_description}",
        "main": "index.js",
        "scripts": {
            "test": "echo \"Error: no test specified\" && exit 1"
        },
        "author": "${author}",
        "license": "${license}",
        "devDependencies": {
            "gulp": "^3.9.0",
            "jspm": "^0.16.19",
        },
        "dependencies": {}
    }""")

filein.write(source.substitute(args))
filein.truncate()
filein.close()
