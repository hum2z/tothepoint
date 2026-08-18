import unittest

from pricing import line_total, order_total


class TestPricing(unittest.TestCase):
    def test_plain_line(self):
        # 2 x $10.00, 8.25% tax -> $21.65
        self.assertEqual(line_total(1000, 2), 2165)

    def test_percent_discount_is_taxed_after_discount(self):
        # 2 x $10.00 less 10% = $18.00, +8.25% tax = $19.485 -> $19.49
        self.assertEqual(line_total(1000, 2, [{"type": "percent", "value": 10}]), 1949)

    def test_flat_discount_cannot_go_negative(self):
        # $5.00 item, $20.00 off -> total floors at 0, no tax on a zero order
        self.assertEqual(line_total(500, 1, [{"type": "flat", "value": 2000}]), 0)

    def test_rounds_half_up(self):
        # 1 x $3.33 -> 333 + 27.4725 = 360.47 -> 360
        self.assertEqual(line_total(333, 1), 360)

    def test_order_total_sums_lines(self):
        self.assertEqual(order_total([(1000, 2, ()), (500, 1, ())]), 2165 + 541)

    def test_unknown_discount_type_raises(self):
        with self.assertRaises(ValueError):
            line_total(1000, 1, [{"type": "bogus", "value": 1}])


if __name__ == "__main__":
    unittest.main()
