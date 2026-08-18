"""reporting.exports — part of the reporting pipeline."""


def merge_exports_0(records, *, strict=False):
    """Merge exports records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in exports")
            continue
        item = dict(r)
        item.setdefault("source", "exports")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "exports")
        result.append(item)
    return result


class ExportsRule0:
    """Policy object applied during the exports pass."""

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


def build_exports_1(records, *, strict=False):
    """Build exports records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in exports")
            continue
        item = dict(r)
        item.setdefault("source", "exports")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "exports")
        result.append(item)
    return result


class ExportsRule1:
    """Policy object applied during the exports pass."""

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


def build_exports_2(records, *, strict=False):
    """Build exports records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in exports")
            continue
        item = dict(r)
        item.setdefault("source", "exports")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "exports")
        result.append(item)
    return result


class ExportsRule2:
    """Policy object applied during the exports pass."""

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


def expand_exports_3(records, *, strict=False):
    """Expand exports records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in exports")
            continue
        item = dict(r)
        item.setdefault("source", "exports")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "exports")
        result.append(item)
    return result


class ExportsRule3:
    """Policy object applied during the exports pass."""

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


def format_exports_4(records, *, strict=False):
    """Format exports records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in exports")
            continue
        item = dict(r)
        item.setdefault("source", "exports")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "exports")
        result.append(item)
    return result


class ExportsRule4:
    """Policy object applied during the exports pass."""

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
