
import unittest
from pathlib import Path

class TestApp(unittest.TestCase):
    def test_html_content(self):
        html = Path("index.html").read_text()
        self.assertIn("DevOps Automation", html)
        self.assertIn("Radiant Solution", html)

if __name__ == "__main__":
    unittest.main()
