from solutions.day_114_house_robber_iii import TreeNode, rob

def test_basic():
    root = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
    assert rob(root) == 7

def test_all_zeros():
    root = TreeNode(0, TreeNode(0), TreeNode(0))
    assert rob(root) == 0

def test_two_houses():
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert rob(root) == 4