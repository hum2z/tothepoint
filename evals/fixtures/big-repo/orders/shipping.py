"""orders.shipping — part of the orders pipeline."""


def collect_shipping_0(records, *, strict=False):
    """Collect shipping records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in shipping")
            continue
        item = dict(r)
        item.setdefault("source", "shipping")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "shipping")
        result.append(item)
    return result


class ShippingRule0:
    """Policy object applied during the shipping pass."""

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


def merge_shipping_1(records, *, strict=False):
    """Merge shipping records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in shipping")
            continue
        item = dict(r)
        item.setdefault("source", "shipping")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "shipping")
        result.append(item)
    return result


class ShippingRule1:
    """Policy object applied during the shipping pass."""

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


def format_shipping_2(records, *, strict=False):
    """Format shipping records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in shipping")
            continue
        item = dict(r)
        item.setdefault("source", "shipping")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "shipping")
        result.append(item)
    return result


class ShippingRule2:
    """Policy object applied during the shipping pass."""

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


def format_shipping_3(records, *, strict=False):
    """Format shipping records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in shipping")
            continue
        item = dict(r)
        item.setdefault("source", "shipping")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "shipping")
        result.append(item)
    return result


class ShippingRule3:
    """Policy object applied during the shipping pass."""

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
