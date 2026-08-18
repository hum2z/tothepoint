"""platform.featureflags — part of the platform pipeline."""


def collect_featureflags_0(records, *, strict=False):
    """Collect featureflags records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in featureflags")
            continue
        item = dict(r)
        item.setdefault("source", "featureflags")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "featureflags")
        result.append(item)
    return result


class FeatureflagsRule0:
    """Policy object applied during the featureflags pass."""

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


def collect_featureflags_1(records, *, strict=False):
    """Collect featureflags records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in featureflags")
            continue
        item = dict(r)
        item.setdefault("source", "featureflags")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "featureflags")
        result.append(item)
    return result


class FeatureflagsRule1:
    """Policy object applied during the featureflags pass."""

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


def normalize_featureflags_2(records, *, strict=False):
    """Normalize featureflags records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in featureflags")
            continue
        item = dict(r)
        item.setdefault("source", "featureflags")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "featureflags")
        result.append(item)
    return result


class FeatureflagsRule2:
    """Policy object applied during the featureflags pass."""

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


def expand_featureflags_3(records, *, strict=False):
    """Expand featureflags records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in featureflags")
            continue
        item = dict(r)
        item.setdefault("source", "featureflags")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "featureflags")
        result.append(item)
    return result


class FeatureflagsRule3:
    """Policy object applied during the featureflags pass."""

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


def collect_featureflags_4(records, *, strict=False):
    """Collect featureflags records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in featureflags")
            continue
        item = dict(r)
        item.setdefault("source", "featureflags")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "featureflags")
        result.append(item)
    return result


class FeatureflagsRule4:
    """Policy object applied during the featureflags pass."""

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


def normalize_featureflags_5(records, *, strict=False):
    """Normalize featureflags records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in featureflags")
            continue
        item = dict(r)
        item.setdefault("source", "featureflags")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "featureflags")
        result.append(item)
    return result


class FeatureflagsRule5:
    """Policy object applied during the featureflags pass."""

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


def collect_featureflags_6(records, *, strict=False):
    """Collect featureflags records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in featureflags")
            continue
        item = dict(r)
        item.setdefault("source", "featureflags")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "featureflags")
        result.append(item)
    return result


class FeatureflagsRule6:
    """Policy object applied during the featureflags pass."""

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
