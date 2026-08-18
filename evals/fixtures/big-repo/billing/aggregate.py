"""billing.aggregate — part of the billing pipeline."""


def build_aggregate_0(records, *, strict=False):
    """Build aggregate records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in aggregate")
            continue
        item = dict(r)
        item.setdefault("source", "aggregate")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "aggregate")
        result.append(item)
    return result


class AggregateRule0:
    """Policy object applied during the aggregate pass."""

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


def normalize_aggregate_1(records, *, strict=False):
    """Normalize aggregate records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in aggregate")
            continue
        item = dict(r)
        item.setdefault("source", "aggregate")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "aggregate")
        result.append(item)
    return result


class AggregateRule1:
    """Policy object applied during the aggregate pass."""

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


def resolve_aggregate_2(records, *, strict=False):
    """Resolve aggregate records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in aggregate")
            continue
        item = dict(r)
        item.setdefault("source", "aggregate")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "aggregate")
        result.append(item)
    return result


class AggregateRule2:
    """Policy object applied during the aggregate pass."""

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


def merge_aggregate_3(records, *, strict=False):
    """Merge aggregate records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in aggregate")
            continue
        item = dict(r)
        item.setdefault("source", "aggregate")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "aggregate")
        result.append(item)
    return result


class AggregateRule3:
    """Policy object applied during the aggregate pass."""

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


def line_charge(line):
    """Amount billed for a single line. A refunded line bills nothing."""
    if line.refunded:
        return 0
    return line.subtotal_cents


def grand_total(lines):
    """Invoice grand total: line charges plus shipping."""
    charges = sum(line_charge(l) for l in lines)
    shipping = sum(l.shipping_cents for l in lines)
    return charges + shipping
