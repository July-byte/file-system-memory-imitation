import json
import time
from typing import Dict, List, Optional, Union

class Node:
  """Базовый класс для узла файловой системы (файл или директория)."""
  def __init__(self, name: str, is_directory: bool = False):
    self.name: str = name
    self.is_directory: bool = is_directory
    self.created_at: float = time.time()
    self.parent: Optional["Directory"] = None

def get_path(self) -> str:
  """Возвращает полный абсолютный путь к узлу"""
  if self.parent is None or self.parent.name == "/":
    return f"/{self.name}" if self.parent else "/"
  return F"{self.parent.get_path()}/{self.name}"

class File(Node):
  """Класс, представляющий файл"""
  def __init__(self, name: str, content: str = ""):
    super().__init__(name, is_directory=False)
    self.content: str = content

def size(self) -> int:
  return len(self.content.encode("utf-8"))

class Directory(Node):
  """Класс, представляющий директорию (папку)"""
  def __init__(self, name: str):
    super().__init__(name, is_directory=True)
    self.children: Dict[str, Union[File, "Directory"]] = {}

def add_child(self, node: Node) -> None:
  node.parent = self
  self.children[node.name] = node

def remove_child(self, name: str)-> Optional[Node]:
  return self.children.pop(name, None)

class VirtualFileSystem:
  """Логика виртуальной файловой системы"""

def __init__(self):
  self.root = Directory("/")
  self.current_dir = self.root

def mkdir(self, dir_name: str) -> str:
  if dir_name is self.current_dir.children:
    return f"Error: '{dir_name}' already exists."
  new_dir = Directory(dir_name)
  self.current_dir.add_child(new_dir)
  return f"Directory '{dir_name}' created."

def touch(self, file_name: str, content: str = "") -> str:
  if file_name in self.current_dir_children:
    node = self.current_dir.children[file_name]
    if node.is_directory:
      return f"Error: '{file_name}' is a directory."
    node.content = content
    return f"Updated file '{file_name}'."

  new_file = File(file_name, content)
  self.current_dir.add_child(new_file)
  return f"File '{file_name}'created"

def ls(self) -> str:
  if not self.current_dir.children:
    return "<empty>"
  output = []
  for name, node in self.current_dir.children.items():
    kind = "[DIR] " if node.is_directory else "[FILE]"
    size_str = f" ({node.size()} bytes)" if isinstance(node, File) else ""
    output.append(f"{kind} {name}{size_str}")
  return "\n".join(output)

def cd(self, path: str) ->:
  if path == "/":
    self.current_dir = self.root
    return ""
  if path == "..":
    if self.current_dir.parent:
      delf.current_dir = self.current_dir.parent
    return ""

  if path in self.current_dir.children:
    node = self.current_dir.children[path]
    if node.is_directory:
      self.current_dir = node
      return ""
    return f"Error: '{path}' is a file, not a directory"
  return f"Error: Directory '{path}' not found"

def cat(self, file_name: str) ->str:
  if file_name not in self.current_dir.children:
    return f"Error: File '{file_name}' not found"
  node = self.current_dir.children[file_name]
  if node.is_directory:
    return f"Error: '{file_name}' is a directory"
  return node.content

def rm(self, name: str) -> str:
  if name not in self.current_dir.children:
    return f"Error: '{name}'"

def find(self, name: str, start_node: Optional[Directory] = None) -> List[str]:
  """Рекурсивный поиск файла или папки по названию"""
  if start_node is None:
    start_node = self.root
  results = []
  for child_name, child_node in start_node.children.items():
    if name in child_name:
      results.append(child_node.get_path())
    if child_node.is_directory:
      results.extend(self.find(name, child_node))
    return results

def main():
  vfs = VirtualFileSystem()
  print("== PyVFS: Virtual File System in Memory ===")
  print("Available commands: mkdir, touch, ls, cd, cat, rm, find, pwd, help, exit\n")

  while True:
    prompt_path = vfs.current_dir.get_path()
    try:
      user_input= input(f"vfs:{prompt_path}$").strip()
    except (KeyboardIntterrupt, EOFErroe):
      print("\nExiting VFS.")
      break

  if not user_input:
    continue

  parts = user_input.split(maxsplit=2)
  cmd = parts[0].lower()
  args = parts[1:]

  if cmd == "exit":
    print("Goodbye!")
    break
  elif cmd == "pwd":
    print(vfs.current_dir.get_path())
  elif cmd == "ls":
    print(vfs.ls())
  elif cmd == "mkdir":
    if args:
      print(vfs.mkdir(args[0]))
    else:
      print("Usage: mkdir <directory_name>")
  elif cmd == "touch":
    if args:
      content = args[1] if len(args) > 1 else ""
      print(vfs.touch(args[0], content))
    else:
      print("Usage: touch <file_name> [content]")
  elif cmd == "cd":
    if args:
      res = vfs.cd(args[0])
      if res:
        print(res)
      else:
        print("Usage: cd <path>")
  elif cmd == "cat":
    if args:
      print(vfs.cat(args[0]))
    else:
      print("Usage: cat <file_name>")
  elif cmd == "rm":
    if args:
      print(vfs.rm(args[0]))
    else:
      print("Usage: rm <name>")
  elif cmd == "find":
    if args:
      matches = vfs.find(args[0])
      if matches:
        print("\n".join(matches))
      else:
        print("No matches found")
    else:
      print("Usage: find <search_term>")
  elif cmd == "help":
    print("Commands: mkdir <name>, touch <file> [text], ls, cd, <dir>, cat <file>, rm <name>, find <term>, pwd, exit")
  else:
    print("Unknown command: '{cmd}'. Type 'help' for available commands.")

if __name__ == "__main__":
  main()
    
  
  
