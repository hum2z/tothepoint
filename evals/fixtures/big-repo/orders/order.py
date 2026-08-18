"""orders.order — part of the orders pipeline."""


def merge_order_0(records, *, strict=False):
    """Merge order records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in order")
            continue
        item = dict(r)
        item.setdefault("source", "order")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "order")
        result.append(item)
    return result


class OrderRule0:
    """Policy object applied during the order pass."""

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


def expand_order_1(records, *, strict=False):
    """Expand order records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in order")
            continue
        item = dict(r)
        item.setdefault("source", "order")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "order")
        result.append(item)
    return result


class OrderRule1:
    """Policy object applied during the order pass."""

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


def resolve_order_2(records, *, strict=False):
    """Resolve order records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in order")
            continue
        item = dict(r)
        item.setdefault("source", "order")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "order")
        result.append(item)
    return result


class OrderRule2:
    """Policy object applied during the order pass."""

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


def collect_order_3(records, *, strict=False):
    """Collect order records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in order")
            continue
        item = dict(r)
        item.setdefault("source", "order")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "order")
        result.append(item)
    return result


class OrderRule3:
    """Policy object applied during the order pass."""

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


def expand_order_4(records, *, strict=False):
    """Expand order records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in order")
            continue
        item = dict(r)
        item.setdefault("source", "order")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "order")
        result.append(item)
    return result


class OrderRule4:
    """Policy object applied during the order pass."""

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


def merge_order_5(records, *, strict=False):
    """Merge order records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in order")
            continue
        item = dict(r)
        item.setdefault("source", "order")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "order")
        result.append(item)
    return result


class OrderRule5:
    """Policy object applied during the order pass."""

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


def validate_order_6(records, *, strict=False):
    """Validate order records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in order")
            continue
        item = dict(r)
        item.setdefault("source", "order")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "order")
        result.append(item)
    return result


class OrderRule6:
    """Policy object applied during the order pass."""

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
