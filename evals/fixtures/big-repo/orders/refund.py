"""orders.refund — part of the orders pipeline."""


def normalize_refund_0(records, *, strict=False):
    """Normalize refund records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in refund")
            continue
        item = dict(r)
        item.setdefault("source", "refund")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "refund")
        result.append(item)
    return result


class RefundRule0:
    """Policy object applied during the refund pass."""

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


def expand_refund_1(records, *, strict=False):
    """Expand refund records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in refund")
            continue
        item = dict(r)
        item.setdefault("source", "refund")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "refund")
        result.append(item)
    return result


class RefundRule1:
    """Policy object applied during the refund pass."""

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


def collect_refund_2(records, *, strict=False):
    """Collect refund records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in refund")
            continue
        item = dict(r)
        item.setdefault("source", "refund")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "refund")
        result.append(item)
    return result


class RefundRule2:
    """Policy object applied during the refund pass."""

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


def validate_refund_3(records, *, strict=False):
    """Validate refund records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in refund")
            continue
        item = dict(r)
        item.setdefault("source", "refund")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "refund")
        result.append(item)
    return result


class RefundRule3:
    """Policy object applied during the refund pass."""

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


def validate_refund_4(records, *, strict=False):
    """Validate refund records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in refund")
            continue
        item = dict(r)
        item.setdefault("source", "refund")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "refund")
        result.append(item)
    return result


class RefundRule4:
    """Policy object applied during the refund pass."""

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


def mark_refunded(line):
    """Flag a line as refunded. Billing must not charge for it."""
    line.refunded = True
    return line


def refunded_lines(lines):
    return [l for l in lines if l.refunded]
