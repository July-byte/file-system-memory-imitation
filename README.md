# PyVFS - In-Memory Virtual File System

An interactive in-memory Virtual File System

## Key Features:
- **Three Data Structure**: File and Directory hierarchy built using Object-Oriented Programming (OOP)
- **CLI Navigation**: Unix-like console interface ('cd', 'ls', 'mkdir', 'touch', 'cat', 'rm', 'find', 'pwd')
- **State Persistence**: Save and restore the entire filesystem tree to/from a JSON file
- **Recursive Search**: Quick path resolution for files and directories
- **Unit Tested**: Covered with Python's native 'unittests' framework

  ## Quick Start
  1. clone the repository:
  '''bash git clone [https://github.com/July-byte/py-vfs.git] (https://github.com/July-byte/py-vfs.git)
     cd py-vfs
  2. run the program:
     python main.py
  3. run tests:
  4. python -m unittest discover tests

  ## Usage example
  === PyVFS: Virtual File System in Memory ===
  vfs:/$ mkdir projects
  vfs:/$ cd projects
  vfs:/projects$ touch app.py "print('Hello World')"
  vfs:/projects$ ls
  [FILE] app.py (20 bytes)
  vfs:/projects$ cat app.py
  print('Hello World')
  vfs:/projects$ cd ..
  vfs:/$ find app.py
  /projects/app.py
