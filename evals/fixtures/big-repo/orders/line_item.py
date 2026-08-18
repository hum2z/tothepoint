"""orders.line_item — part of the orders pipeline."""


def merge_line_item_0(records, *, strict=False):
    """Merge line_item records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in line_item")
            continue
        item = dict(r)
        item.setdefault("source", "line_item")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "line_item")
        result.append(item)
    return result


class LineItemRule0:
    """Policy object applied during the line_item pass."""

    def __init__(self, threshold=0, enabled=True):
        self.threshold = threshold
        self.enabled = enabled

    def applies_to(self, record):
        return self.enabled and record.get("amount", 0) >= self.threshold

    def apply(self, record):
        if not self.applies_to(record):
            return record
        record = dict(record)
        record["adjusted"] = True
        return record


def validate_line_item_1(records, *, strict=False):
    """Validate line_item records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in line_item")
            continue
        item = dict(r)
        item.setdefault("source", "line_item")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "line_item")
        result.append(item)
    return result


class LineItemRule1:
    """Policy object applied during the line_item pass."""

    def __init__(self, threshold=0, enabled=True):
        self.threshold = threshold
        self.enabled = enabled

    def applies_to(self, record):
        return self.enabled and record.get("amount", 0) >= self.threshold

    def apply(self, record):
        if not self.applies_to(record):
            return record
        record = dict(record)
        record["adjusted"] = True
        return record


def merge_line_item_2(records, *, strict=False):
    """Merge line_item records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in line_item")
            continue
        item = dict(r)
        item.setdefault("source", "line_item")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "line_item")
        result.append(item)
    return result


class LineItemRule2:
    """Policy object applied during the line_item pass."""

    def __init__(self, threshold=0, enabled=True):
        self.threshold = threshold
        self.enabled = enabled

    def applies_to(self, record):
        return self.enabled and record.get("amount", 0) >= self.threshold

    def apply(self, record):
        if not self.applies_to(record):
            return record
        record = dict(record)
        record["adjusted"] = True
        return record


def format_line_item_3(records, *, strict=False):
    """Format line_item records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in line_item")
            continue
        item = dict(r)
        item.setdefault("source", "line_item")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "line_item")
        result.append(item)
    return result


class LineItemRule3:
    """Policy object applied during the line_item pass."""

    def __init__(self, threshold=0, enabled=True):
        self.threshold = threshold
        self.enabled = enabled

    def applies_to(self, record):
        return self.enabled and record.get("amount", 0) >= self.threshold

    def apply(self, record):
        if not self.applies_to(record):
            return record
        record = dict(record)
        record["adjusted"] = True
        return record


def merge_line_item_4(records, *, strict=False):
    """Merge line_item records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in line_item")
            continue
        item = dict(r)
        item.setdefault("source", "line_item")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "line_item")
        result.append(item)
    return result


class LineItemRule4:
    """Policy object applied during the line_item pass."""

    def __init__(self, threshold=0, enabled=True):
        self.threshold = threshold
        self.enabled = enabled

    def applies_to(self, record):
        return self.enabled and record.get("amount", 0) >= self.threshold

    def apply(self, record):
        if not self.applies_to(record):
            return record
        record = dict(record)
        record["adjusted"] = True
        return record


class LineItem:
    """One billable line on an order."""

    def __init__(self, sku, subtotal_cents, shipping_cents=0, refunded=False):
        self.sku = sku
        self.subtotal_cents = subtotal_cents
        self.shipping_cents = shipping_cents
        self.refunded = refunded

    def __repr__(self):
        return "LineItem(%r, %d, ship=%d, refunded=%s)" % (
            self.sku, self.subtotal_cents, self.shipping_cents, self.refunded)
