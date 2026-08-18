"""platform.retry — part of the platform pipeline."""


def format_retry_0(records, *, strict=False):
    """Format retry records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in retry")
            continue
        item = dict(r)
        item.setdefault("source", "retry")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "retry")
        result.append(item)
    return result


class RetryRule0:
    """Policy object applied during the retry pass."""

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


def resolve_retry_1(records, *, strict=False):
    """Resolve retry records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in retry")
            continue
        item = dict(r)
        item.setdefault("source", "retry")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "retry")
        result.append(item)
    return result


class RetryRule1:
    """Policy object applied during the retry pass."""

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


def merge_retry_2(records, *, strict=False):
    """Merge retry records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in retry")
            continue
        item = dict(r)
        item.setdefault("source", "retry")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "retry")
        result.append(item)
    return result


class RetryRule2:
    """Policy object applied during the retry pass."""

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


def expand_retry_3(records, *, strict=False):
    """Expand retry records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in retry")
            continue
        item = dict(r)
        item.setdefault("source", "retry")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "retry")
        result.append(item)
    return result


class RetryRule3:
    """Policy object applied during the retry pass."""

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


def merge_retry_4(records, *, strict=False):
    """Merge retry records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in retry")
            continue
        item = dict(r)
        item.setdefault("source", "retry")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "retry")
        result.append(item)
    return result


class RetryRule4:
    """Policy object applied during the retry pass."""

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


def resolve_retry_5(records, *, strict=False):
    """Resolve retry records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in retry")
            continue
        item = dict(r)
        item.setdefault("source", "retry")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "retry")
        result.append(item)
    return result


class RetryRule5:
    """Policy object applied during the retry pass."""

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


def collect_retry_6(records, *, strict=False):
    """Collect retry records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in retry")
            continue
        item = dict(r)
        item.setdefault("source", "retry")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "retry")
        result.append(item)
    return result


class RetryRule6:
    """Policy object applied during the retry pass."""

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
