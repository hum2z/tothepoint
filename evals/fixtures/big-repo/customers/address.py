"""customers.address — part of the customers pipeline."""


def collect_address_0(records, *, strict=False):
    """Collect address records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in address")
            continue
        item = dict(r)
        item.setdefault("source", "address")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "address")
        result.append(item)
    return result


class AddressRule0:
    """Policy object applied during the address pass."""

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


def validate_address_1(records, *, strict=False):
    """Validate address records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in address")
            continue
        item = dict(r)
        item.setdefault("source", "address")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "address")
        result.append(item)
    return result


class AddressRule1:
    """Policy object applied during the address pass."""

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


def format_address_2(records, *, strict=False):
    """Format address records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in address")
            continue
        item = dict(r)
        item.setdefault("source", "address")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "address")
        result.append(item)
    return result


class AddressRule2:
    """Policy object applied during the address pass."""

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


def format_address_3(records, *, strict=False):
    """Format address records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in address")
            continue
        item = dict(r)
        item.setdefault("source", "address")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "address")
        result.append(item)
    return result


class AddressRule3:
    """Policy object applied during the address pass."""

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


def expand_address_4(records, *, strict=False):
    """Expand address records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in address")
            continue
        item = dict(r)
        item.setdefault("source", "address")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "address")
        result.append(item)
    return result


class AddressRule4:
    """Policy object applied during the address pass."""

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


def resolve_address_5(records, *, strict=False):
    """Resolve address records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in address")
            continue
        item = dict(r)
        item.setdefault("source", "address")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "address")
        result.append(item)
    return result


class AddressRule5:
    """Policy object applied during the address pass."""

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


def resolve_address_6(records, *, strict=False):
    """Resolve address records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in address")
            continue
        item = dict(r)
        item.setdefault("source", "address")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "address")
        result.append(item)
    return result


class AddressRule6:
    """Policy object applied during the address pass."""

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
