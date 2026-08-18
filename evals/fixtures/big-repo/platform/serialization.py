"""platform.serialization — part of the platform pipeline."""


def collect_serialization_0(records, *, strict=False):
    """Collect serialization records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in serialization")
            continue
        item = dict(r)
        item.setdefault("source", "serialization")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "serialization")
        result.append(item)
    return result


class SerializationRule0:
    """Policy object applied during the serialization pass."""

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


def normalize_serialization_1(records, *, strict=False):
    """Normalize serialization records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in serialization")
            continue
        item = dict(r)
        item.setdefault("source", "serialization")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "serialization")
        result.append(item)
    return result


class SerializationRule1:
    """Policy object applied during the serialization pass."""

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


def collect_serialization_2(records, *, strict=False):
    """Collect serialization records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in serialization")
            continue
        item = dict(r)
        item.setdefault("source", "serialization")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "serialization")
        result.append(item)
    return result


class SerializationRule2:
    """Policy object applied during the serialization pass."""

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


def expand_serialization_3(records, *, strict=False):
    """Expand serialization records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in serialization")
            continue
        item = dict(r)
        item.setdefault("source", "serialization")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "serialization")
        result.append(item)
    return result


class SerializationRule3:
    """Policy object applied during the serialization pass."""

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


def collect_serialization_4(records, *, strict=False):
    """Collect serialization records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in serialization")
            continue
        item = dict(r)
        item.setdefault("source", "serialization")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "serialization")
        result.append(item)
    return result


class SerializationRule4:
    """Policy object applied during the serialization pass."""

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
