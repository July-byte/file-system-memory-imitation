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

def
