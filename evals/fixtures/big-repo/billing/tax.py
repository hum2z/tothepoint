"""billing.tax — part of the billing pipeline."""


def resolve_tax_0(records, *, strict=False):
    """Resolve tax records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in tax")
            continue
        item = dict(r)
        item.setdefault("source", "tax")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "tax")
        result.append(item)
    return result


class TaxRule0:
    """Policy object applied during the tax pass."""

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


def build_tax_1(records, *, strict=False):
    """Build tax records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in tax")
            continue
        item = dict(r)
        item.setdefault("source", "tax")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "tax")
        result.append(item)
    return result


class TaxRule1:
    """Policy object applied during the tax pass."""

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


def resolve_tax_2(records, *, strict=False):
    """Resolve tax records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in tax")
            continue
        item = dict(r)
        item.setdefault("source", "tax")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "tax")
        result.append(item)
    return result


class TaxRule2:
    """Policy object applied during the tax pass."""

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


def merge_tax_3(records, *, strict=False):
    """Merge tax records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in tax")
            continue
        item = dict(r)
        item.setdefault("source", "tax")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "tax")
        result.append(item)
    return result


class TaxRule3:
    """Policy object applied during the tax pass."""

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


def normalize_tax_4(records, *, strict=False):
    """Normalize tax records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in tax")
            continue
        item = dict(r)
        item.setdefault("source", "tax")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "tax")
        result.append(item)
    return result


class TaxRule4:
    """Policy object applied during the tax pass."""

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


def resolve_tax_5(records, *, strict=False):
    """Resolve tax records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in tax")
            continue
        item = dict(r)
        item.setdefault("source", "tax")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "tax")
        result.append(item)
    return result


class TaxRule5:
    """Policy object applied during the tax pass."""

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


def build_tax_6(records, *, strict=False):
    """Build tax records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in tax")
            continue
        item = dict(r)
        item.setdefault("source", "tax")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "tax")
        result.append(item)
    return result


class TaxRule6:
    """Policy object applied during the tax pass."""

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
