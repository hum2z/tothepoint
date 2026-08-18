"""orders.fulfillment — part of the orders pipeline."""


def collect_fulfillment_0(records, *, strict=False):
    """Collect fulfillment records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in fulfillment")
            continue
        item = dict(r)
        item.setdefault("source", "fulfillment")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "fulfillment")
        result.append(item)
    return result


class FulfillmentRule0:
    """Policy object applied during the fulfillment pass."""

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


def resolve_fulfillment_1(records, *, strict=False):
    """Resolve fulfillment records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in fulfillment")
            continue
        item = dict(r)
        item.setdefault("source", "fulfillment")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "fulfillment")
        result.append(item)
    return result


class FulfillmentRule1:
    """Policy object applied during the fulfillment pass."""

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


def collect_fulfillment_2(records, *, strict=False):
    """Collect fulfillment records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in fulfillment")
            continue
        item = dict(r)
        item.setdefault("source", "fulfillment")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "fulfillment")
        result.append(item)
    return result


class FulfillmentRule2:
    """Policy object applied during the fulfillment pass."""

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


def collect_fulfillment_3(records, *, strict=False):
    """Collect fulfillment records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in fulfillment")
            continue
        item = dict(r)
        item.setdefault("source", "fulfillment")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "fulfillment")
        result.append(item)
    return result


class FulfillmentRule3:
    """Policy object applied during the fulfillment pass."""

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


def build_fulfillment_4(records, *, strict=False):
    """Build fulfillment records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in fulfillment")
            continue
        item = dict(r)
        item.setdefault("source", "fulfillment")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "fulfillment")
        result.append(item)
    return result


class FulfillmentRule4:
    """Policy object applied during the fulfillment pass."""

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
