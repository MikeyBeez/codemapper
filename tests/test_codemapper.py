import unittest
import tempfile
import os
from codemapper.utils import create_map

class TestCodeMapper(unittest.TestCase):
    """
    Unit tests for the CodeMapper module.
    """
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        
        # Create a mock .gitignore file
        self.ignore_file = os.path.join(self.test_dir, '.gitignore')
        with open(self.ignore_file, 'w') as f:
            f.write("*.pyc\n__pycache__\n")
        
        # Create a mock Python file
        test_file = os.path.join(self.test_dir, 'test_file.py')
        with open(test_file, 'w') as f:
            f.write("def test_function():\n    pass\n")

    def tearDown(self):
        # Clean up the temporary directory
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)

    def test_create_map(self):
        """
        Test the create_map function to ensure it correctly maps a repository.
        """
        code_map = create_map(self.test_dir, self.ignore_file)
        self.assertIsNotNone(code_map)
        self.assertTrue(len(code_map['files']) > 0)
        
        # Check if the test file is in the map
        test_file_found = any(file_info['path'].endswith('test_file.py') for file_info in code_map['files'])
        self.assertTrue(test_file_found, "Test file not found in the code map")

if __name__ == '__main__':
    unittest.main()
