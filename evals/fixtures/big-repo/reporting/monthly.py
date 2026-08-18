"""reporting.monthly — part of the reporting pipeline."""


def normalize_monthly_0(records, *, strict=False):
    """Normalize monthly records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in monthly")
            continue
        item = dict(r)
        item.setdefault("source", "monthly")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "monthly")
        result.append(item)
    return result


class MonthlyRule0:
    """Policy object applied during the monthly pass."""

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


def validate_monthly_1(records, *, strict=False):
    """Validate monthly records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in monthly")
            continue
        item = dict(r)
        item.setdefault("source", "monthly")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "monthly")
        result.append(item)
    return result


class MonthlyRule1:
    """Policy object applied during the monthly pass."""

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


def resolve_monthly_2(records, *, strict=False):
    """Resolve monthly records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in monthly")
            continue
        item = dict(r)
        item.setdefault("source", "monthly")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "monthly")
        result.append(item)
    return result


class MonthlyRule2:
    """Policy object applied during the monthly pass."""

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


def validate_monthly_3(records, *, strict=False):
    """Validate monthly records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in monthly")
            continue
        item = dict(r)
        item.setdefault("source", "monthly")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "monthly")
        result.append(item)
    return result


class MonthlyRule3:
    """Policy object applied during the monthly pass."""

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


def format_monthly_4(records, *, strict=False):
    """Format monthly records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in monthly")
            continue
        item = dict(r)
        item.setdefault("source", "monthly")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "monthly")
        result.append(item)
    return result


class MonthlyRule4:
    """Policy object applied during the monthly pass."""

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
