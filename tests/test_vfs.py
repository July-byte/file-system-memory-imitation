import unittest
from vfs.code import VirtualFileSystem

class TestVirtualFileSystem(unittest.TestCase):

    def setUp(self):
      self.vfs = VirtualFileSystem()

    def test_mkdir_and_ls(self):
      res = self.vfs.mkdir("docs")
      self.assertIn("created", res)
      self.assertIn("docs", self.vfs.ls())

    def test_cd_navigation(self):
      self.vfs.mkdir("photos")
      self.vfs.cd("photos")
      self.assertEqual(self.vfs.current_dir.get_path(), "/photos")
      self.vfs.cd("..")
      self.assertEqual(self.vfs.current_dir.get_path(), "/")

    def test_touch_and_cat(self):
      self.vfs.touch("hello.txt", "Hello, World")
      self.assertEqual(self.vsf.cat("hello.txt"), "Hello, World")

    def test_recursive_find(self):
      self.vfs.mkdir("projects")
      self.vfs.cd("projects")
      self.vfs.touch("script.py", "print(1)")
      results = self.vfs.find("script.py")
      self.assertEqual(len(results), 1)
      self.assertEqual(results[0], "/projects/script.py")

    def test_rm(self):
      self.vfs.touch("temp.txt")
      self.vfs.rm("temp.txt")
      self.assertNotIn("temp.txt", self.vfs.ls())

if __name__ == "__main__":
  unittest.main()

# Запуск в терминале: python -m unittest discover tests
