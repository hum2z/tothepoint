"""billing.dunning — part of the billing pipeline."""


def validate_dunning_0(records, *, strict=False):
    """Validate dunning records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in dunning")
            continue
        item = dict(r)
        item.setdefault("source", "dunning")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "dunning")
        result.append(item)
    return result


class DunningRule0:
    """Policy object applied during the dunning pass."""

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


def merge_dunning_1(records, *, strict=False):
    """Merge dunning records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in dunning")
            continue
        item = dict(r)
        item.setdefault("source", "dunning")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "dunning")
        result.append(item)
    return result


class DunningRule1:
    """Policy object applied during the dunning pass."""

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


def collect_dunning_2(records, *, strict=False):
    """Collect dunning records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in dunning")
            continue
        item = dict(r)
        item.setdefault("source", "dunning")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "dunning")
        result.append(item)
    return result


class DunningRule2:
    """Policy object applied during the dunning pass."""

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


def resolve_dunning_3(records, *, strict=False):
    """Resolve dunning records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in dunning")
            continue
        item = dict(r)
        item.setdefault("source", "dunning")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "dunning")
        result.append(item)
    return result


class DunningRule3:
    """Policy object applied during the dunning pass."""

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


def validate_dunning_4(records, *, strict=False):
    """Validate dunning records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in dunning")
            continue
        item = dict(r)
        item.setdefault("source", "dunning")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "dunning")
        result.append(item)
    return result


class DunningRule4:
    """Policy object applied during the dunning pass."""

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
