import unittest

from billing.invoice import render_summary
from orders.line_item import LineItem
from orders.refund import mark_refunded


class TestInvoiceSummary(unittest.TestCase):
    def test_plain_order(self):
        lines = [LineItem("a", 1000, 500), LineItem("b", 2000, 300)]
        self.assertEqual(render_summary(lines)["grand_total_cents"], 3800)

    def test_refunded_line_is_not_billed_at_all(self):
        # b is refunded: neither its subtotal nor its shipping should be billed.
        lines = [LineItem("a", 1000, 500), mark_refunded(LineItem("b", 2000, 300))]
        self.assertEqual(render_summary(lines)["grand_total_cents"], 1500)

    def test_all_refunded(self):
        lines = [mark_refunded(LineItem("a", 1000, 500))]
        self.assertEqual(render_summary(lines)["grand_total_cents"], 0)


if __name__ == "__main__":
    unittest.main()
