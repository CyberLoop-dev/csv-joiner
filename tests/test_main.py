import unittest
from main import join_rows


class JoinTests(unittest.TestCase):
    def setUp(self):
        self.left_fields = ["id", "name"]
        self.left = [{"id": "1", "name": "Ada"}, {"id": "2", "name": "Lin"}]
        self.right_fields = ["id", "total"]
        self.right = [{"id": "1", "total": "10"}, {"id": "1", "total": "20"}, {"id": "3", "total": "30"}]

    def test_left_join_preserves_duplicate_matches_and_unmatched_left(self):
        fields, rows = join_rows(self.left_fields, self.left, self.right_fields, self.right, "id", "left")
        self.assertEqual(len(rows), 3)
        self.assertEqual([row["right_total"] for row in rows], ["10", "20", ""])

    def test_full_join_includes_right_only_rows(self):
        _, rows = join_rows(self.left_fields, self.left, self.right_fields, self.right, "id", "full")
        self.assertEqual(len(rows), 4)
        self.assertEqual(rows[-1]["id"], "3")


if __name__ == "__main__":
    unittest.main()
