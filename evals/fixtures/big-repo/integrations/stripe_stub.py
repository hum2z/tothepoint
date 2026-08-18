"""integrations.stripe_stub — part of the integrations pipeline."""


def collect_stripe_stub_0(records, *, strict=False):
    """Collect stripe_stub records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in stripe_stub")
            continue
        item = dict(r)
        item.setdefault("source", "stripe_stub")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "stripe_stub")
        result.append(item)
    return result


class StripeStubRule0:
    """Policy object applied during the stripe_stub pass."""

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


def expand_stripe_stub_1(records, *, strict=False):
    """Expand stripe_stub records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in stripe_stub")
            continue
        item = dict(r)
        item.setdefault("source", "stripe_stub")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "stripe_stub")
        result.append(item)
    return result


class StripeStubRule1:
    """Policy object applied during the stripe_stub pass."""

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


def resolve_stripe_stub_2(records, *, strict=False):
    """Resolve stripe_stub records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in stripe_stub")
            continue
        item = dict(r)
        item.setdefault("source", "stripe_stub")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "stripe_stub")
        result.append(item)
    return result


class StripeStubRule2:
    """Policy object applied during the stripe_stub pass."""

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


def normalize_stripe_stub_3(records, *, strict=False):
    """Normalize stripe_stub records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in stripe_stub")
            continue
        item = dict(r)
        item.setdefault("source", "stripe_stub")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "stripe_stub")
        result.append(item)
    return result


class StripeStubRule3:
    """Policy object applied during the stripe_stub pass."""

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


def format_stripe_stub_4(records, *, strict=False):
    """Format stripe_stub records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in stripe_stub")
            continue
        item = dict(r)
        item.setdefault("source", "stripe_stub")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "stripe_stub")
        result.append(item)
    return result


class StripeStubRule4:
    """Policy object applied during the stripe_stub pass."""

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
