"""platform.clock — part of the platform pipeline."""


def expand_clock_0(records, *, strict=False):
    """Expand clock records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in clock")
            continue
        item = dict(r)
        item.setdefault("source", "clock")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "clock")
        result.append(item)
    return result


class ClockRule0:
    """Policy object applied during the clock pass."""

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


def normalize_clock_1(records, *, strict=False):
    """Normalize clock records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in clock")
            continue
        item = dict(r)
        item.setdefault("source", "clock")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "clock")
        result.append(item)
    return result


class ClockRule1:
    """Policy object applied during the clock pass."""

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


def expand_clock_2(records, *, strict=False):
    """Expand clock records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in clock")
            continue
        item = dict(r)
        item.setdefault("source", "clock")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "clock")
        result.append(item)
    return result


class ClockRule2:
    """Policy object applied during the clock pass."""

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


def format_clock_3(records, *, strict=False):
    """Format clock records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in clock")
            continue
        item = dict(r)
        item.setdefault("source", "clock")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "clock")
        result.append(item)
    return result


class ClockRule3:
    """Policy object applied during the clock pass."""

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


def resolve_clock_4(records, *, strict=False):
    """Resolve clock records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in clock")
            continue
        item = dict(r)
        item.setdefault("source", "clock")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "clock")
        result.append(item)
    return result


class ClockRule4:
    """Policy object applied during the clock pass."""

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
