import unittest
import os


def analyze_text(filename):
    """Calculate the number of lines and characters in a file

    Args:
        filename: The name of the file to analyze.

    Raises:
        IOError: If 'filename' does not exist or can't be read.

    Returns:
        A tuple where the first element is the number of lines in
        the file and the second element is the number of characters.
    """
    lines = 0
    characters = 0
    with open(filename, "r") as f:
        for line in f:
            lines += 1
            characters += len(line)
    return lines, characters


class TextAnalysisTests(unittest.TestCase):
    """Tests for the 'analyze_text()' function"""

    def setUp(self):
        """Fixture that creates a file for the text method to use"""
        self.filename = "Lorem_Ipsum.txt"
        with open(self.filename, "wt") as f:
            f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas ultricies ultricies venenatis.\n"
                    "Aliquam pulvinar, nunc id aliquet faucibus, elit libero tincidunt ante, sed malesuada tellus orci\n"
                    "et est. Nullam id libero in est varius faucibus at id enim. Pellentesque bibendum rutrum neque at\n"
                    "iaculis. Donec consectetur volutpat fringilla. Integer pretium velit in nunc sagittis, nec\n"
                    "pellentesque odio placerat. Cras varius tortor lacus, dapibus rhoncus urna luctus eget. Aliquam\n"
                    "gravida justo velit, vel cursus nulla accumsan quis. Fusce nec nisl sapien. Pellentesque sem mi,\n"
                    "sodales et magna id, semper tincidunt justo. Phasellus non quam viverra, sagittis turpis at,\n"
                    "sollicitudin ex. Curabitur lacinia mauris at varius placerat. Phasellus tincidunt nisl sit amet\n"
                    "condimentum elementum. Sed ante turpis, placerat vulputate congue ac, efficitur at elit. Quisque\n"
                    "posuere sollicitudin lorem id ultrices. Aliquam pharetra iaculis nunc, id rhoncus urna elementum\n"
                    "sit amet.\n")

    def tearDown(self):
        """Fixture that deletes the files used by the test methods"""
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        """Basic smoke test: does the function run"""
        analyze_text(self.filename)

    def test_line_count(self):
        """Check that the line count is correct"""
        self.assertEqual(analyze_text(self.filename)[0], 11)

    def test_character_count(self):
        """Check that the character count is correct."""
        self.assertEqual(analyze_text(self.filename)[1], 970)

    def test_no_such_file(self):
        """Check the proper exception is thrown for a missing file"""
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_deletion(self):
        """Check that the function doesn't delete the input file"""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))


if __name__ == '__main__':
    unittest.main()
