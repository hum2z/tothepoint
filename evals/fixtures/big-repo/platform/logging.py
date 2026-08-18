"""platform.logging — part of the platform pipeline."""


def validate_logging_0(records, *, strict=False):
    """Validate logging records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in logging")
            continue
        item = dict(r)
        item.setdefault("source", "logging")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "logging")
        result.append(item)
    return result


class LoggingRule0:
    """Policy object applied during the logging pass."""

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


def merge_logging_1(records, *, strict=False):
    """Merge logging records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in logging")
            continue
        item = dict(r)
        item.setdefault("source", "logging")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "logging")
        result.append(item)
    return result


class LoggingRule1:
    """Policy object applied during the logging pass."""

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


def collect_logging_2(records, *, strict=False):
    """Collect logging records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in logging")
            continue
        item = dict(r)
        item.setdefault("source", "logging")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "logging")
        result.append(item)
    return result


class LoggingRule2:
    """Policy object applied during the logging pass."""

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


def normalize_logging_3(records, *, strict=False):
    """Normalize logging records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in logging")
            continue
        item = dict(r)
        item.setdefault("source", "logging")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "logging")
        result.append(item)
    return result


class LoggingRule3:
    """Policy object applied during the logging pass."""

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


def format_logging_4(records, *, strict=False):
    """Format logging records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in logging")
            continue
        item = dict(r)
        item.setdefault("source", "logging")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "logging")
        result.append(item)
    return result


class LoggingRule4:
    """Policy object applied during the logging pass."""

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


def expand_logging_5(records, *, strict=False):
    """Expand logging records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in logging")
            continue
        item = dict(r)
        item.setdefault("source", "logging")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "logging")
        result.append(item)
    return result


class LoggingRule5:
    """Policy object applied during the logging pass."""

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
