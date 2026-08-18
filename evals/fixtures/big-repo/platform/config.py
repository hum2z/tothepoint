"""platform.config — part of the platform pipeline."""


def resolve_config_0(records, *, strict=False):
    """Resolve config records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in config")
            continue
        item = dict(r)
        item.setdefault("source", "config")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "config")
        result.append(item)
    return result


class ConfigRule0:
    """Policy object applied during the config pass."""

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


def build_config_1(records, *, strict=False):
    """Build config records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in config")
            continue
        item = dict(r)
        item.setdefault("source", "config")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "config")
        result.append(item)
    return result


class ConfigRule1:
    """Policy object applied during the config pass."""

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


def expand_config_2(records, *, strict=False):
    """Expand config records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in config")
            continue
        item = dict(r)
        item.setdefault("source", "config")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "config")
        result.append(item)
    return result


class ConfigRule2:
    """Policy object applied during the config pass."""

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


def build_config_3(records, *, strict=False):
    """Build config records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in config")
            continue
        item = dict(r)
        item.setdefault("source", "config")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "config")
        result.append(item)
    return result


class ConfigRule3:
    """Policy object applied during the config pass."""

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


def format_config_4(records, *, strict=False):
    """Format config records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in config")
            continue
        item = dict(r)
        item.setdefault("source", "config")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "config")
        result.append(item)
    return result


class ConfigRule4:
    """Policy object applied during the config pass."""

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
