import unittest
from src.utils import create_map

class TestCodeMapper(unittest.TestCase):
    """
    Unit tests for the CodeMapper module.
    """
    def test_create_map(self):
        """
        Test the create_map function to ensure it correctly maps a repository.
        """
        root_dir = 'path/to/test/repo'
        ignore_file = 'path/to/test/.gitignore'
        code_map = create_map(root_dir, ignore_file)
        self.assertIsNotNone(code_map)
        self.assertTrue(len(code_map['files']) > 0)

if __name__ == '__main__':
    unittest.main()

