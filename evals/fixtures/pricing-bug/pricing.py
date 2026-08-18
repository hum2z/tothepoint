"""Order pricing. All money is in integer cents."""

TAX_RATE = 0.0825


def _apply_discounts(subtotal_cents, discounts):
    """Apply discounts in order. `percent` is 0-100, `flat` is in cents."""
    total = subtotal_cents
    for d in discounts:
        if d["type"] == "percent":
            total = total * (1 - d["value"] / 100.0)
        elif d["type"] == "flat":
            total = total - d["value"]
        else:
            raise ValueError("unknown discount type: %s" % d["type"])
    return total


def line_total(unit_price_cents, qty, discounts=()):
    """Total for one line item, after discounts and tax."""
    subtotal = unit_price_cents * qty
    tax = subtotal * TAX_RATE
    discounted = _apply_discounts(subtotal, discounts)
    return int(discounted + tax)


def order_total(lines):
    """`lines` is a list of (unit_price_cents, qty, discounts)."""
    return sum(line_total(*line) for line in lines)
