import unittest
from lab6_tree import build_tree_recursive, build_tree_iterative

class TestBinaryTree(unittest.TestCase):

    def test_height_0(self):
        self.assertEqual(build_tree_recursive(9, 0), {"9": []})
        self.assertEqual(build_tree_iterative(9, 0), {"9": []})

    def test_height_1(self):
        expected = {"9": [{"19": []}, {"17": []}]}
        self.assertEqual(build_tree_recursive(9, 1), expected)
        self.assertEqual(build_tree_iterative(9, 1), expected)

    def test_height_2(self):
        expected = {
            "9": [
                {"19": [{"39": []}, {"37": []}]},
                {"17": [{"35": []}, {"33": []}]}
            ]
        }
        self.assertEqual(build_tree_recursive(9, 2), expected)
        self.assertEqual(build_tree_iterative(9, 2), expected)

    def test_height_3(self):
        tree_rec = build_tree_recursive(2, 3)
        tree_iter = build_tree_iterative(2, 3)
        self.assertIsInstance(tree_rec, dict)
        self.assertIsInstance(tree_iter, dict)
        self.assertEqual(tree_rec, tree_iter)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            build_tree_recursive(9, -1)
        with self.assertRaises(ValueError):
            build_tree_iterative(9, -1)

    def test_custom_functions(self):
        l = lambda x: x + 1
        r = lambda x: x ** 2
        expected = {"5": [{"6": []}, {"25": []}]}
        self.assertEqual(build_tree_recursive(5, 1, l, r), expected)
        self.assertEqual(build_tree_iterative(5, 1, l, r), expected)

    def test_custom_complex_functions(self):
        l = lambda x: x * 2 + 3
        r = lambda x: x * x + 1
        tree_rec = build_tree_recursive(3, 2, l, r)
        tree_iter = build_tree_iterative(3, 2, l, r)
        self.assertEqual(tree_rec, tree_iter)
        # Проверяем левый лист корня
        self.assertIn(str(l(3)), tree_rec["3"][0])
        # Проверяем правый лист корня
        self.assertIn(str(r(3)), tree_rec["3"][1])

    def test_large_root(self):
        root = 1000
        height = 2
        tree_rec = build_tree_recursive(root, height)
        tree_iter = build_tree_iterative(root, height)
        self.assertEqual(tree_rec, tree_iter)
        # Проверяем, что левый и правый потомки вычислены верно
        self.assertEqual(list(tree_rec["1000"][0].keys())[0], str(2001))
        self.assertEqual(list(tree_rec["1000"][1].keys())[0], str(1999))

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)
