import unittest
from hashmap import HashMap


class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.hashmap = HashMap(size=10)

    def test_insert_and_get(self):
        self.hashmap.insert("keyivan", "valueivan")
        self.assertEqual(self.hashmap.get("keyivan"), "valueivan")

    def test_delete_key_value(self):
        self.hashmap.insert("key", "value")
        self.hashmap.remove("key")
        self.assertNotEqual(self.hashmap.get("key"), "")

    def test_update_value(self):
        self.hashmap.insert('key1', 'value1')
        self.hashmap.insert('key1', 'updated_value')
        self.assertEqual(self.hashmap.get('key1'), 'updated_value')
