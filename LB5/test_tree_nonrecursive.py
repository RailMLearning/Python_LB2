import unittest
from tree_nonrecursive import gen_bin_tree

class TestBinaryTreeNonRecursive(unittest.TestCase):

    def test_height_0(self):
        self.assertEqual(gen_bin_tree(0, 9), {"9": []})

    def test_height_1(self):
        self.assertEqual(
            gen_bin_tree(1, 9),
            {"9": [{"19": []}, {"17": []}]}
        )

    def test_height_2_structure(self):
        tree = gen_bin_tree(2, 9)
        self.assertIn("19", tree["9"][0])
        self.assertIn("17", tree["9"][1])

    def test_custom_branches(self):
        tree = gen_bin_tree(
            1,
            5,
            left_branch=lambda r: r+1,
            right_branch=lambda r: r**2
        )
        self.assertEqual(
            tree,
            {"5": [{"6": []}, {"25": []}]}
        )

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            gen_bin_tree(-1, 9)

    def test_keys_are_strings(self):
        tree = gen_bin_tree(1, 9)
        for key in tree.keys():
            self.assertIsInstance(key, str)

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)
