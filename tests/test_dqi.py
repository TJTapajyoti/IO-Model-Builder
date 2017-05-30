import unittest
import iomb.dqi as dqi


class TestDqiMatrix(unittest.TestCase):

    def test_indices(self):
        m = dqi.DqiMatrix(3, 5)
        m[2, 4] = (1, 2, 3, 4, 5)
        self.assertEqual((1, 2, 3, 4, 5), m[2, 4])

    def test_rand(self):
        m = dqi.DqiMatrix.rand(5, 10)
        for row in range(0, m.rows):
            for col in range(0, m.cols):
                val = m[row, col]
                self.assertTrue(isinstance(val, list))
                self.assertEqual(5, len(val))
                for i in range(0, len(val)):
                    self.assertTrue(isinstance(val[i], int))

    def test_parse(self):
        t = """
        [ (1,2,4) (3,3,2) (4,2,2) ;
          (4,2,4) (none)  (5,2,5) ]
        """
        m = dqi.DqiMatrix.parse(t)
        # print(m)
        self.assertEqual([1, 2, 4], m[0, 0])
        self.assertEqual([3, 3, 2], m[0, 1])
        self.assertEqual([4, 2, 2], m[0, 2])
        self.assertEqual([4, 2, 4], m[1, 0])
        self.assertEqual(None, m[1, 1])
        self.assertEqual([5, 2, 5], m[1, 2])


class TestAggregation(unittest.TestCase):

    def test_weighted_avg(self):
        self.assertEqual(0, dqi.weighted_avg([], []))
        self.assertEqual(5, dqi.weighted_avg([5], [0.3]))
        self.assertEqual(3, dqi.weighted_avg([5, 3, 2], [0.3, 0.8, 0.1]))

    def test_aggregate_entries(self):
        entries = [[4, 1, 3], [2, 1, 5]]
        weights = [0.4,  0.7]
        agg_entry = dqi.aggregate_entries(entries, weights)
        self.assertEqual([3, 1, 4], agg_entry)

    def test_aggregate_columns(self):
        t = """
            [ (4,1,3) (2,1,5) ;
              (4,5,3) (1,5,1) ;
              (2,1,5) (3,1,4) ]
        """
        m = dqi.DqiMatrix.parse(t)
        base = [[0.4,  0.7],
                [0.1,  0.5],
                [0.9,  0.2]]
        r = m.aggregate_columns(base)
        self.assertEqual(3, r.rows)
        self.assertEqual(1, r.cols)
        self.assertEqual([3, 1, 4], r[0, 0])
        self.assertEqual([2, 5, 1], r[1, 0])
        self.assertEqual([2, 1, 5], r[2, 0])

if __name__ == '__main__':
    unittest.main()
