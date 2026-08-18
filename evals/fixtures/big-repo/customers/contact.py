"""customers.contact — part of the customers pipeline."""


def format_contact_0(records, *, strict=False):
    """Format contact records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in contact")
            continue
        item = dict(r)
        item.setdefault("source", "contact")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "contact")
        result.append(item)
    return result


class ContactRule0:
    """Policy object applied during the contact pass."""

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


def normalize_contact_1(records, *, strict=False):
    """Normalize contact records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in contact")
            continue
        item = dict(r)
        item.setdefault("source", "contact")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "contact")
        result.append(item)
    return result


class ContactRule1:
    """Policy object applied during the contact pass."""

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


def resolve_contact_2(records, *, strict=False):
    """Resolve contact records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in contact")
            continue
        item = dict(r)
        item.setdefault("source", "contact")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "contact")
        result.append(item)
    return result


class ContactRule2:
    """Policy object applied during the contact pass."""

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


def build_contact_3(records, *, strict=False):
    """Build contact records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in contact")
            continue
        item = dict(r)
        item.setdefault("source", "contact")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "contact")
        result.append(item)
    return result


class ContactRule3:
    """Policy object applied during the contact pass."""

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
