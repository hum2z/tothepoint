"""catalog.product — part of the catalog pipeline."""


def expand_product_0(records, *, strict=False):
    """Expand product records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in product")
            continue
        item = dict(r)
        item.setdefault("source", "product")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "product")
        result.append(item)
    return result


class ProductRule0:
    """Policy object applied during the product pass."""

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


def format_product_1(records, *, strict=False):
    """Format product records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in product")
            continue
        item = dict(r)
        item.setdefault("source", "product")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "product")
        result.append(item)
    return result


class ProductRule1:
    """Policy object applied during the product pass."""

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


def expand_product_2(records, *, strict=False):
    """Expand product records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in product")
            continue
        item = dict(r)
        item.setdefault("source", "product")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "product")
        result.append(item)
    return result


class ProductRule2:
    """Policy object applied during the product pass."""

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


def validate_product_3(records, *, strict=False):
    """Validate product records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in product")
            continue
        item = dict(r)
        item.setdefault("source", "product")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "product")
        result.append(item)
    return result


class ProductRule3:
    """Policy object applied during the product pass."""

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


def resolve_product_4(records, *, strict=False):
    """Resolve product records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in product")
            continue
        item = dict(r)
        item.setdefault("source", "product")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "product")
        result.append(item)
    return result


class ProductRule4:
    """Policy object applied during the product pass."""

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


def resolve_product_5(records, *, strict=False):
    """Resolve product records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in product")
            continue
        item = dict(r)
        item.setdefault("source", "product")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "product")
        result.append(item)
    return result


class ProductRule5:
    """Policy object applied during the product pass."""

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
