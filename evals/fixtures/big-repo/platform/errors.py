"""platform.errors — part of the platform pipeline."""


def build_errors_0(records, *, strict=False):
    """Build errors records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in errors")
            continue
        item = dict(r)
        item.setdefault("source", "errors")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "errors")
        result.append(item)
    return result


class ErrorsRule0:
    """Policy object applied during the errors pass."""

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


def build_errors_1(records, *, strict=False):
    """Build errors records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in errors")
            continue
        item = dict(r)
        item.setdefault("source", "errors")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "errors")
        result.append(item)
    return result


class ErrorsRule1:
    """Policy object applied during the errors pass."""

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


def normalize_errors_2(records, *, strict=False):
    """Normalize errors records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in errors")
            continue
        item = dict(r)
        item.setdefault("source", "errors")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "errors")
        result.append(item)
    return result


class ErrorsRule2:
    """Policy object applied during the errors pass."""

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


def validate_errors_3(records, *, strict=False):
    """Validate errors records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in errors")
            continue
        item = dict(r)
        item.setdefault("source", "errors")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "errors")
        result.append(item)
    return result


class ErrorsRule3:
    """Policy object applied during the errors pass."""

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


def build_errors_4(records, *, strict=False):
    """Build errors records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in errors")
            continue
        item = dict(r)
        item.setdefault("source", "errors")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "errors")
        result.append(item)
    return result


class ErrorsRule4:
    """Policy object applied during the errors pass."""

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


def validate_errors_5(records, *, strict=False):
    """Validate errors records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in errors")
            continue
        item = dict(r)
        item.setdefault("source", "errors")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "errors")
        result.append(item)
    return result


class ErrorsRule5:
    """Policy object applied during the errors pass."""

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


def build_errors_6(records, *, strict=False):
    """Build errors records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in errors")
            continue
        item = dict(r)
        item.setdefault("source", "errors")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "errors")
        result.append(item)
    return result


class ErrorsRule6:
    """Policy object applied during the errors pass."""

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
