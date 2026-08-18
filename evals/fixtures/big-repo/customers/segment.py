"""customers.segment — part of the customers pipeline."""


def expand_segment_0(records, *, strict=False):
    """Expand segment records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in segment")
            continue
        item = dict(r)
        item.setdefault("source", "segment")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "segment")
        result.append(item)
    return result


class SegmentRule0:
    """Policy object applied during the segment pass."""

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


def expand_segment_1(records, *, strict=False):
    """Expand segment records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in segment")
            continue
        item = dict(r)
        item.setdefault("source", "segment")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "segment")
        result.append(item)
    return result


class SegmentRule1:
    """Policy object applied during the segment pass."""

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


def expand_segment_2(records, *, strict=False):
    """Expand segment records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in segment")
            continue
        item = dict(r)
        item.setdefault("source", "segment")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "segment")
        result.append(item)
    return result


class SegmentRule2:
    """Policy object applied during the segment pass."""

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


def validate_segment_3(records, *, strict=False):
    """Validate segment records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in segment")
            continue
        item = dict(r)
        item.setdefault("source", "segment")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "segment")
        result.append(item)
    return result


class SegmentRule3:
    """Policy object applied during the segment pass."""

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


def resolve_segment_4(records, *, strict=False):
    """Resolve segment records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in segment")
            continue
        item = dict(r)
        item.setdefault("source", "segment")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "segment")
        result.append(item)
    return result


class SegmentRule4:
    """Policy object applied during the segment pass."""

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


def collect_segment_5(records, *, strict=False):
    """Collect segment records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in segment")
            continue
        item = dict(r)
        item.setdefault("source", "segment")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "segment")
        result.append(item)
    return result


class SegmentRule5:
    """Policy object applied during the segment pass."""

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


def resolve_segment_6(records, *, strict=False):
    """Resolve segment records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in segment")
            continue
        item = dict(r)
        item.setdefault("source", "segment")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "segment")
        result.append(item)
    return result


class SegmentRule6:
    """Policy object applied during the segment pass."""

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
