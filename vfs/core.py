import json
import os
from vfs.models import Directory, File

class VirtualFileSystem:
  def __init__(self):
    self.root = Directory("/")
    self.current_dir = self.root

  #Новые методы сериализации
  def _node_to_dict(self, node) -> dict:
    """Рекурсивно превращает дерево объектов в словарь"""
    data = {
      "name": node.name,
      "is_directory": node.is_directory,
      "created_at": node.created_at,
    }
    if node.is_directory:
      data["children"] = {
        name: self._node_to_dict(child)
        for name, child in node.children.items()
      }
    else:
      data["content"] = node.content
    return data

def _dict_to_node(self, data: dict):
  """Рекурсивно воссоздает дерево объектов из словаря"""
  if data["is_directory"]:
    dir_node = Directory(data["name"])
    dir_node.created_at = data.get("created_at", dir_node.created_at)
    for child_name, child_data in data.get("children", {}).items():
      child_node = self._dict_to_node(child_data)
      dir_node.add_child(child_node)
    return dir_node
  else:
    file_node = File(data["name"], data.get("content", ""))
    file_node.created_at = data.get("created_at", file_node.created_at)
    return file_node

def save_to_file(self, filepath: str = "state.json") -> None:
  """Сохраняет состояние системы в JSON-файл"""
  data = self._node_to_dict(self.root)
  with open(filepath, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

def load_from_file(self, filepath: str = "state.json") -> bool:
  """Загружает состояние системы из JSON-файла"""
  if not os.path.exists(filepath):
    return False
  with open(filepath, "r", encoding="utf-8") as f:
    data = json.load(f)
  self.root = self._dict_to_node(data)
  self.current_dir = self.root
  return True
  

