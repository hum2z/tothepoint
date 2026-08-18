"""integrations.webhooks — part of the integrations pipeline."""


def build_webhooks_0(records, *, strict=False):
    """Build webhooks records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in webhooks")
            continue
        item = dict(r)
        item.setdefault("source", "webhooks")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "webhooks")
        result.append(item)
    return result


class WebhooksRule0:
    """Policy object applied during the webhooks pass."""

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


def validate_webhooks_1(records, *, strict=False):
    """Validate webhooks records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in webhooks")
            continue
        item = dict(r)
        item.setdefault("source", "webhooks")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "webhooks")
        result.append(item)
    return result


class WebhooksRule1:
    """Policy object applied during the webhooks pass."""

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


def build_webhooks_2(records, *, strict=False):
    """Build webhooks records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in webhooks")
            continue
        item = dict(r)
        item.setdefault("source", "webhooks")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "webhooks")
        result.append(item)
    return result


class WebhooksRule2:
    """Policy object applied during the webhooks pass."""

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


def expand_webhooks_3(records, *, strict=False):
    """Expand webhooks records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in webhooks")
            continue
        item = dict(r)
        item.setdefault("source", "webhooks")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "webhooks")
        result.append(item)
    return result


class WebhooksRule3:
    """Policy object applied during the webhooks pass."""

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


def collect_webhooks_4(records, *, strict=False):
    """Collect webhooks records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in webhooks")
            continue
        item = dict(r)
        item.setdefault("source", "webhooks")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "webhooks")
        result.append(item)
    return result


class WebhooksRule4:
    """Policy object applied during the webhooks pass."""

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


def merge_webhooks_5(records, *, strict=False):
    """Merge webhooks records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in webhooks")
            continue
        item = dict(r)
        item.setdefault("source", "webhooks")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "webhooks")
        result.append(item)
    return result


class WebhooksRule5:
    """Policy object applied during the webhooks pass."""

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


def resolve_webhooks_6(records, *, strict=False):
    """Resolve webhooks records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in webhooks")
            continue
        item = dict(r)
        item.setdefault("source", "webhooks")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "webhooks")
        result.append(item)
    return result


class WebhooksRule6:
    """Policy object applied during the webhooks pass."""

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
