from solutions.day_120_serialize_deserialize_binary_tree import serialize, deserialize, TreeNode

def test_serialize_deserialize():
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    serialized = serialize(root)
    assert serialized == "1,2,3,null,null,4,5"
    restored = deserialize(serialized)
    assert restored.val == 1
    assert restored.left.val == 2
    assert restored.right.val == 3

def test_serialize_single():
    root = TreeNode(42)
    serialized = serialize(root)
    assert serialized == "42"
    restored = deserialize(serialized)
    assert restored.val == 42
    assert restored.left is None

def test_serialize_empty():
    assert serialize(None) == ""
    assert deserialize("") is None

def test_serialize_left_skewed():
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), None), None), None)
    serialized = serialize(root)
    restored = deserialize(serialized)
    assert restored.val == 1
    assert restored.left.val == 2
    assert restored.left.left.val == 3
    assert restored.left.left.left.val == 4