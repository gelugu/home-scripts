import sys, os, subprocess, shlex
from src.Colors import cyan

script_description = """
This script looking for unsynced local git repositories

usage:
  check-git [parameter]

params:
  - help - print help message
  - list - print unsynced repositories
"""

def list_unsynced():
  is_only_path = "--only-path" in sys.argv or "-p" in sys.argv
  print("Scanning file system")
  for root, dirs, _ in os.walk(os.environ["HOME"]):
    if ".git" in dirs:
      path = os.path.abspath(root)
      changes = []
      with subprocess.Popen(
        shlex.split(f"git -C {path} status"),
        stdout=subprocess.PIPE
      ) as proc:
        is_print = False
        for l in [b.decode("utf-8") for b in proc.stdout.readlines()]:
          if "Changes not staged for commit" in l: is_print = True
          if "Untracked files" in l: is_print = True
          if is_print == True and l == "\n": is_print = False
          if is_print: changes.append(l.replace("\n", ""))
      if len(changes) > 0:
        cyan(f"\n{path}")
        if not is_only_path: [print(c) for c in changes]

def help():
  print(script_description)


# handle params

params = {
  "help": help,
  "list": list_unsynced
}

if (len(sys.argv) > 1):
  if (sys.argv[1] not in params.keys()):
    print("Unknown parameter")
    exit(1)
  else:
    params[sys.argv[1]]()
else: list_unsynced()
