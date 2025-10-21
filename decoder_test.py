from decoder import decoder
import unittest


class TestDecoderFunctions(unittest.TestCase):

    # ---------------- ENCODE TESTS ----------------

    # Basic tests
    def test_encode_basic_1(self):
        expected = "Khoor"
        actual = decoder("Hello", "1")
        self.assertEqual(actual, expected)

    def test_encode_basic_2(self):
        expected = "Dolfh"
        actual = decoder("Alice", "1")
        self.assertEqual(actual, expected)

    # Challenge tests (punctuation, spaces, mixed case)
    def test_encode_challenge_1(self):
        expected = "Khoor, Zruog!"
        actual = decoder("Hello, World!", "1")
        self.assertEqual(actual, expected)

    def test_encode_challenge_2(self):
        expected = "Wkh txlfn ira zdj."
        actual = decoder("The quick fox wag.", "1")
        self.assertEqual(actual, expected)

    def test_encode_challenge_3(self):
        expected = "Abc XyZ"
        actual = decoder("Xyz UvW", "1")
        self.assertEqual(actual, expected)

    # Boundary tests (letters near 'z', empty string, all uppercase)
    def test_encode_boundary_1(self):
        expected = "def"
        actual = decoder("abc", "1")
        self.assertEqual(actual, expected)

    def test_encode_boundary_2(self):
        expected = "ZAB"
        actual = decoder("WXY", "1")
        self.assertEqual(actual, expected)

    def test_encode_boundary_3(self):
        expected = ""
        actual = decoder("", "1")
        self.assertEqual(actual, expected)

    # ---------------- DECODE TESTS ----------------

    # Basic tests
    def test_decode_basic_1(self):
        expected = "Hello"
        actual = decoder("Khoor", "2")
        self.assertEqual(actual, expected)

    def test_decode_basic_2(self):
        expected = "Alice"
        actual = decoder("Dolfh", "2")
        self.assertEqual(actual, expected)

    # Challenge tests
    def test_decode_challenge_1(self):
        expected = "Hello, World!"
        actual = decoder("Khoor, Zruog!", "2")
        self.assertEqual(actual, expected)

    def test_decode_challenge_2(self):
        expected = "The quick fox wag."
        actual = decoder("Wkh txlfn ira zdj.", "2")
        self.assertEqual(actual, expected)

    def test_decode_challenge_3(self):
        expected = "Xyz UvW"
        actual = decoder("Abc XyZ", "2")
        self.assertEqual(actual, expected)

    # Boundary tests
    def test_decode_boundary_1(self):
        expected = "abc"
        actual = decoder("def", "2")
        self.assertEqual(actual, expected)

    def test_decode_boundary_2(self):
        expected = "WXY"
        actual = decoder("ZAB", "2")
        self.assertEqual(actual, expected)

    def test_decode_boundary_3(self):
        expected = ""
        actual = decoder("", "2")
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
