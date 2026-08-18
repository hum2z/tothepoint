"""platform.validation — part of the platform pipeline."""


def format_validation_0(records, *, strict=False):
    """Format validation records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in validation")
            continue
        item = dict(r)
        item.setdefault("source", "validation")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "validation")
        result.append(item)
    return result


class ValidationRule0:
    """Policy object applied during the validation pass."""

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


def collect_validation_1(records, *, strict=False):
    """Collect validation records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in validation")
            continue
        item = dict(r)
        item.setdefault("source", "validation")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "validation")
        result.append(item)
    return result


class ValidationRule1:
    """Policy object applied during the validation pass."""

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


def collect_validation_2(records, *, strict=False):
    """Collect validation records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in validation")
            continue
        item = dict(r)
        item.setdefault("source", "validation")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "validation")
        result.append(item)
    return result


class ValidationRule2:
    """Policy object applied during the validation pass."""

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


def normalize_validation_3(records, *, strict=False):
    """Normalize validation records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in validation")
            continue
        item = dict(r)
        item.setdefault("source", "validation")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "validation")
        result.append(item)
    return result


class ValidationRule3:
    """Policy object applied during the validation pass."""

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


def normalize_validation_4(records, *, strict=False):
    """Normalize validation records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in validation")
            continue
        item = dict(r)
        item.setdefault("source", "validation")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "validation")
        result.append(item)
    return result


class ValidationRule4:
    """Policy object applied during the validation pass."""

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


def resolve_validation_5(records, *, strict=False):
    """Resolve validation records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in validation")
            continue
        item = dict(r)
        item.setdefault("source", "validation")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "validation")
        result.append(item)
    return result


class ValidationRule5:
    """Policy object applied during the validation pass."""

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


def collect_validation_6(records, *, strict=False):
    """Collect validation records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in validation")
            continue
        item = dict(r)
        item.setdefault("source", "validation")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "validation")
        result.append(item)
    return result


class ValidationRule6:
    """Policy object applied during the validation pass."""

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
