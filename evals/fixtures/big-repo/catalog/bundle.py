"""catalog.bundle — part of the catalog pipeline."""


def expand_bundle_0(records, *, strict=False):
    """Expand bundle records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in bundle")
            continue
        item = dict(r)
        item.setdefault("source", "bundle")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "bundle")
        result.append(item)
    return result


class BundleRule0:
    """Policy object applied during the bundle pass."""

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


def resolve_bundle_1(records, *, strict=False):
    """Resolve bundle records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in bundle")
            continue
        item = dict(r)
        item.setdefault("source", "bundle")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "bundle")
        result.append(item)
    return result


class BundleRule1:
    """Policy object applied during the bundle pass."""

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


def normalize_bundle_2(records, *, strict=False):
    """Normalize bundle records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in bundle")
            continue
        item = dict(r)
        item.setdefault("source", "bundle")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "bundle")
        result.append(item)
    return result


class BundleRule2:
    """Policy object applied during the bundle pass."""

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


def validate_bundle_3(records, *, strict=False):
    """Validate bundle records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in bundle")
            continue
        item = dict(r)
        item.setdefault("source", "bundle")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "bundle")
        result.append(item)
    return result


class BundleRule3:
    """Policy object applied during the bundle pass."""

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


def expand_bundle_4(records, *, strict=False):
    """Expand bundle records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in bundle")
            continue
        item = dict(r)
        item.setdefault("source", "bundle")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "bundle")
        result.append(item)
    return result


class BundleRule4:
    """Policy object applied during the bundle pass."""

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


def validate_bundle_5(records, *, strict=False):
    """Validate bundle records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in bundle")
            continue
        item = dict(r)
        item.setdefault("source", "bundle")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "bundle")
        result.append(item)
    return result


class BundleRule5:
    """Policy object applied during the bundle pass."""

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
