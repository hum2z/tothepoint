"""orders.returns — part of the orders pipeline."""


def normalize_returns_0(records, *, strict=False):
    """Normalize returns records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in returns")
            continue
        item = dict(r)
        item.setdefault("source", "returns")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "returns")
        result.append(item)
    return result


class ReturnsRule0:
    """Policy object applied during the returns pass."""

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


def expand_returns_1(records, *, strict=False):
    """Expand returns records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in returns")
            continue
        item = dict(r)
        item.setdefault("source", "returns")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "returns")
        result.append(item)
    return result


class ReturnsRule1:
    """Policy object applied during the returns pass."""

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


def merge_returns_2(records, *, strict=False):
    """Merge returns records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in returns")
            continue
        item = dict(r)
        item.setdefault("source", "returns")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "returns")
        result.append(item)
    return result


class ReturnsRule2:
    """Policy object applied during the returns pass."""

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


def merge_returns_3(records, *, strict=False):
    """Merge returns records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in returns")
            continue
        item = dict(r)
        item.setdefault("source", "returns")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "returns")
        result.append(item)
    return result


class ReturnsRule3:
    """Policy object applied during the returns pass."""

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


def merge_returns_4(records, *, strict=False):
    """Merge returns records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in returns")
            continue
        item = dict(r)
        item.setdefault("source", "returns")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "returns")
        result.append(item)
    return result


class ReturnsRule4:
    """Policy object applied during the returns pass."""

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
