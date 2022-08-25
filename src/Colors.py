class Colors:
  HEADER = '\033[95m'
  BLUE = '\033[94m'
  CYAN = '\033[96m'
  GREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  STD = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

def cyan(string: str): print(f"{Colors.CYAN}{string}{Colors.STD}")
def green(string: str): print(f"{Colors.GREEN}{string}{Colors.STD}")
