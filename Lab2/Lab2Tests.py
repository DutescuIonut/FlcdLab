import unittest
from Lab2 import HashTable,ConstantsSymbolTable,IdentifiersSymbolTable


class TestHashTable(unittest.TestCase):
    def test_insert_and_contains(self):
        table = HashTable(10)
        table.insert("key1", "value1")
        self.assertIn("key1", table)
        self.assertEqual(len(table), 1)

    def test_search(self):
        table = HashTable(10)
        table.insert("key1", "value1")
        value = table.search("key1")
        self.assertEqual(value, "value1")

    def test_remove(self):
        table = HashTable(10)
        table.insert("key1", "value1")
        table.remove("key1")
        self.assertNotIn("key1", table)
        self.assertEqual(len(table), 0)


class TestConstantsSymbolTable(unittest.TestCase):
    def test_insert_and_contains(self):
        table = ConstantsSymbolTable(10)
        table.insert("key1", "value1")
        self.assertIn("key1", table)
        self.assertEqual(len(table), 1)

    def test_search(self):
        table = ConstantsSymbolTable(10)
        table.insert("key1", "value1")
        value = table.search("key1")
        self.assertEqual(value, "value1")

    def test_remove(self):
        table = ConstantsSymbolTable(10)
        table.insert("key1", "value1")
        table.remove("key1")
        self.assertNotIn("key1", table)
        self.assertEqual(len(table), 0)


class TestIdentifiersSymbolTable(unittest.TestCase):
    def test_insert_and_contains(self):
        table = IdentifiersSymbolTable(10)
        table.insert("key1", "value1")
        self.assertIn("key1", table)
        self.assertEqual(len(table), 1)

    def test_search(self):
        table = IdentifiersSymbolTable(10)
        table.insert("key1", "value1")
        value = table.search("key1")
        self.assertEqual(value, "value1")

    def test_remove(self):
        table = IdentifiersSymbolTable(10)
        table.insert("key1", "value1")
        table.remove("key1")
        self.assertNotIn("key1", table)
        self.assertEqual(len(table), 0)


if __name__ == '__main__':
    unittest.main()