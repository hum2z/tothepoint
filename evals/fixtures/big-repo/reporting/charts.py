"""reporting.charts — part of the reporting pipeline."""


def normalize_charts_0(records, *, strict=False):
    """Normalize charts records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in charts")
            continue
        item = dict(r)
        item.setdefault("source", "charts")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "charts")
        result.append(item)
    return result


class ChartsRule0:
    """Policy object applied during the charts pass."""

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


def validate_charts_1(records, *, strict=False):
    """Validate charts records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in charts")
            continue
        item = dict(r)
        item.setdefault("source", "charts")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "charts")
        result.append(item)
    return result


class ChartsRule1:
    """Policy object applied during the charts pass."""

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


def expand_charts_2(records, *, strict=False):
    """Expand charts records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in charts")
            continue
        item = dict(r)
        item.setdefault("source", "charts")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "charts")
        result.append(item)
    return result


class ChartsRule2:
    """Policy object applied during the charts pass."""

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


def validate_charts_3(records, *, strict=False):
    """Validate charts records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in charts")
            continue
        item = dict(r)
        item.setdefault("source", "charts")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "charts")
        result.append(item)
    return result


class ChartsRule3:
    """Policy object applied during the charts pass."""

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
