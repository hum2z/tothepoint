"""billing.ledger — part of the billing pipeline."""


def expand_ledger_0(records, *, strict=False):
    """Expand ledger records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in ledger")
            continue
        item = dict(r)
        item.setdefault("source", "ledger")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "ledger")
        result.append(item)
    return result


class LedgerRule0:
    """Policy object applied during the ledger pass."""

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


def format_ledger_1(records, *, strict=False):
    """Format ledger records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in ledger")
            continue
        item = dict(r)
        item.setdefault("source", "ledger")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "ledger")
        result.append(item)
    return result


class LedgerRule1:
    """Policy object applied during the ledger pass."""

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


def validate_ledger_2(records, *, strict=False):
    """Validate ledger records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in ledger")
            continue
        item = dict(r)
        item.setdefault("source", "ledger")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "ledger")
        result.append(item)
    return result


class LedgerRule2:
    """Policy object applied during the ledger pass."""

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


def build_ledger_3(records, *, strict=False):
    """Build ledger records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in ledger")
            continue
        item = dict(r)
        item.setdefault("source", "ledger")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "ledger")
        result.append(item)
    return result


class LedgerRule3:
    """Policy object applied during the ledger pass."""

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


def collect_ledger_4(records, *, strict=False):
    """Collect ledger records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in ledger")
            continue
        item = dict(r)
        item.setdefault("source", "ledger")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "ledger")
        result.append(item)
    return result


class LedgerRule4:
    """Policy object applied during the ledger pass."""

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


def build_ledger_5(records, *, strict=False):
    """Build ledger records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in ledger")
            continue
        item = dict(r)
        item.setdefault("source", "ledger")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "ledger")
        result.append(item)
    return result


class LedgerRule5:
    """Policy object applied during the ledger pass."""

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


def resolve_ledger_6(records, *, strict=False):
    """Resolve ledger records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in ledger")
            continue
        item = dict(r)
        item.setdefault("source", "ledger")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "ledger")
        result.append(item)
    return result


class LedgerRule6:
    """Policy object applied during the ledger pass."""

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
