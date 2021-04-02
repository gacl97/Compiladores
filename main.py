from Syntatic.Syntatic import Syntatic
import sys

def main():
  if(len(sys.argv) <= 1):
    print("No path directory was passed in arguments.")
    return

  for i in range(1, len(sys.argv)):
    file_name = sys.argv[i]
    Syntatic(file_name)
    print("\n\n")

main()
