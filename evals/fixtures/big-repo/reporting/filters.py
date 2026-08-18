"""reporting.filters — part of the reporting pipeline."""


def format_filters_0(records, *, strict=False):
    """Format filters records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in filters")
            continue
        item = dict(r)
        item.setdefault("source", "filters")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "filters")
        result.append(item)
    return result


class FiltersRule0:
    """Policy object applied during the filters pass."""

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


def expand_filters_1(records, *, strict=False):
    """Expand filters records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in filters")
            continue
        item = dict(r)
        item.setdefault("source", "filters")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "filters")
        result.append(item)
    return result


class FiltersRule1:
    """Policy object applied during the filters pass."""

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


def format_filters_2(records, *, strict=False):
    """Format filters records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in filters")
            continue
        item = dict(r)
        item.setdefault("source", "filters")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "filters")
        result.append(item)
    return result


class FiltersRule2:
    """Policy object applied during the filters pass."""

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


def format_filters_3(records, *, strict=False):
    """Format filters records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in filters")
            continue
        item = dict(r)
        item.setdefault("source", "filters")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "filters")
        result.append(item)
    return result


class FiltersRule3:
    """Policy object applied during the filters pass."""

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


def resolve_filters_4(records, *, strict=False):
    """Resolve filters records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in filters")
            continue
        item = dict(r)
        item.setdefault("source", "filters")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "filters")
        result.append(item)
    return result


class FiltersRule4:
    """Policy object applied during the filters pass."""

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
