"""billing.proration — part of the billing pipeline."""


def resolve_proration_0(records, *, strict=False):
    """Resolve proration records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in proration")
            continue
        item = dict(r)
        item.setdefault("source", "proration")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "proration")
        result.append(item)
    return result


class ProrationRule0:
    """Policy object applied during the proration pass."""

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


def build_proration_1(records, *, strict=False):
    """Build proration records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in proration")
            continue
        item = dict(r)
        item.setdefault("source", "proration")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "proration")
        result.append(item)
    return result


class ProrationRule1:
    """Policy object applied during the proration pass."""

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


def format_proration_2(records, *, strict=False):
    """Format proration records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in proration")
            continue
        item = dict(r)
        item.setdefault("source", "proration")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "proration")
        result.append(item)
    return result


class ProrationRule2:
    """Policy object applied during the proration pass."""

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


def resolve_proration_3(records, *, strict=False):
    """Resolve proration records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in proration")
            continue
        item = dict(r)
        item.setdefault("source", "proration")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "proration")
        result.append(item)
    return result


class ProrationRule3:
    """Policy object applied during the proration pass."""

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


def resolve_proration_4(records, *, strict=False):
    """Resolve proration records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in proration")
            continue
        item = dict(r)
        item.setdefault("source", "proration")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "proration")
        result.append(item)
    return result


class ProrationRule4:
    """Policy object applied during the proration pass."""

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
