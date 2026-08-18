"""platform.idempotency — part of the platform pipeline."""


def merge_idempotency_0(records, *, strict=False):
    """Merge idempotency records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in idempotency")
            continue
        item = dict(r)
        item.setdefault("source", "idempotency")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "idempotency")
        result.append(item)
    return result


class IdempotencyRule0:
    """Policy object applied during the idempotency pass."""

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


def build_idempotency_1(records, *, strict=False):
    """Build idempotency records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in idempotency")
            continue
        item = dict(r)
        item.setdefault("source", "idempotency")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "idempotency")
        result.append(item)
    return result


class IdempotencyRule1:
    """Policy object applied during the idempotency pass."""

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


def expand_idempotency_2(records, *, strict=False):
    """Expand idempotency records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in idempotency")
            continue
        item = dict(r)
        item.setdefault("source", "idempotency")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "idempotency")
        result.append(item)
    return result


class IdempotencyRule2:
    """Policy object applied during the idempotency pass."""

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


def collect_idempotency_3(records, *, strict=False):
    """Collect idempotency records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in idempotency")
            continue
        item = dict(r)
        item.setdefault("source", "idempotency")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "idempotency")
        result.append(item)
    return result


class IdempotencyRule3:
    """Policy object applied during the idempotency pass."""

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
