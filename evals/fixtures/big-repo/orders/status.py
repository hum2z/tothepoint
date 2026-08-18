"""orders.status — part of the orders pipeline."""


def resolve_status_0(records, *, strict=False):
    """Resolve status records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in status")
            continue
        item = dict(r)
        item.setdefault("source", "status")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "status")
        result.append(item)
    return result


class StatusRule0:
    """Policy object applied during the status pass."""

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


def expand_status_1(records, *, strict=False):
    """Expand status records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in status")
            continue
        item = dict(r)
        item.setdefault("source", "status")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "status")
        result.append(item)
    return result


class StatusRule1:
    """Policy object applied during the status pass."""

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


def merge_status_2(records, *, strict=False):
    """Merge status records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in status")
            continue
        item = dict(r)
        item.setdefault("source", "status")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "status")
        result.append(item)
    return result


class StatusRule2:
    """Policy object applied during the status pass."""

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


def normalize_status_3(records, *, strict=False):
    """Normalize status records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in status")
            continue
        item = dict(r)
        item.setdefault("source", "status")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "status")
        result.append(item)
    return result


class StatusRule3:
    """Policy object applied during the status pass."""

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


def build_status_4(records, *, strict=False):
    """Build status records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in status")
            continue
        item = dict(r)
        item.setdefault("source", "status")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "status")
        result.append(item)
    return result


class StatusRule4:
    """Policy object applied during the status pass."""

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


def resolve_status_5(records, *, strict=False):
    """Resolve status records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in status")
            continue
        item = dict(r)
        item.setdefault("source", "status")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "status")
        result.append(item)
    return result


class StatusRule5:
    """Policy object applied during the status pass."""

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


def build_status_6(records, *, strict=False):
    """Build status records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in status")
            continue
        item = dict(r)
        item.setdefault("source", "status")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "status")
        result.append(item)
    return result


class StatusRule6:
    """Policy object applied during the status pass."""

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
