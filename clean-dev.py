from distutils.filelist import findall
import os, sys, re
from src.Colors import cyan

script_description = """
This script looking for temporary development files and remove it

usage:
  clean-dev [parameter]

params:
  - help - print help message
  - list - print dev resources
  - clean - clean all dev resources
"""

def list_node_modules():
  except_roots = [
    r".*/Library/Caches/.*"
  ]
  print("Scanning file system")
  for root, dirs, _ in os.walk(os.environ["HOME"]):
    is_continue = False
    for e in except_roots:
      # print(re.findall(e, root))
      if len(re.findall(e, root)) > 0:
        is_continue: True
        break
    if is_continue: continue

    if "node_modules" in dirs:
      path = os.path.abspath(root)
      cyan(f"\n{path}")

def clean_all():
  print("Not released yet.")

def help():
  print(script_description)


# handle params

params = {
  "help": help,
  "list": list_node_modules,
  "clean": clean_all
}

if (len(sys.argv) > 1):
  if (sys.argv[1] not in params.keys()):
    print("Unknown parameter")
    exit(1)
  else:
    params[sys.argv[1]]()
else: list_node_modules()

