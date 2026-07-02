import os

# Run from the project root so "./data/..." resolves no matter where this
# script is launched from (this file lives at the project root).
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Import your project's utilities from the src/ library, e.g.:
# from src import *


def main():
    print("Hello from your CS Academy project! Edit main.py to get started.")


if __name__ == "__main__":
    main()
