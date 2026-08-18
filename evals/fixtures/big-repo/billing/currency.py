"""billing.currency — part of the billing pipeline."""


def merge_currency_0(records, *, strict=False):
    """Merge currency records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in currency")
            continue
        item = dict(r)
        item.setdefault("source", "currency")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "currency")
        result.append(item)
    return result


class CurrencyRule0:
    """Policy object applied during the currency pass."""

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


def normalize_currency_1(records, *, strict=False):
    """Normalize currency records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in currency")
            continue
        item = dict(r)
        item.setdefault("source", "currency")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "currency")
        result.append(item)
    return result


class CurrencyRule1:
    """Policy object applied during the currency pass."""

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


def build_currency_2(records, *, strict=False):
    """Build currency records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in currency")
            continue
        item = dict(r)
        item.setdefault("source", "currency")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "currency")
        result.append(item)
    return result


class CurrencyRule2:
    """Policy object applied during the currency pass."""

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


def normalize_currency_3(records, *, strict=False):
    """Normalize currency records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in currency")
            continue
        item = dict(r)
        item.setdefault("source", "currency")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "currency")
        result.append(item)
    return result


class CurrencyRule3:
    """Policy object applied during the currency pass."""

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
