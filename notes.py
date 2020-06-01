import sys
import os

python = ".py"
ruby = ".rb"
node = ".js"
text = ".txt"
html = ".html"
css = ".css"

extensions = {
    "python": python,
    "py": python,
    ".py": python,
    "ruby": ruby,
    "rb": ruby,
    ".rb": ruby,
    "node": node,
    "javascript": node,
    ".js": node,
    "js": node,
    "text": text,
    "txt": text,
    ".txt": text,
    "html": html,
    ".html": html,
    "css": css,
    ".css": css,
}

def create():
    extension = str(sys.argv[2])
    try:
        extension = extensions[extension]
    except Exception:
        print("Invalid extension")
        print("Setting extension to Text File (.txt)")
        extension = ".txt"

    fileName = str(sys.argv[1]) + extension
    open(fileName, "a").close()
    os.system("notepad " + fileName)

if __name__ == "__main__":
    create()