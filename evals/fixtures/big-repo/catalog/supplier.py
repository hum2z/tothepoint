"""catalog.supplier — part of the catalog pipeline."""


def build_supplier_0(records, *, strict=False):
    """Build supplier records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in supplier")
            continue
        item = dict(r)
        item.setdefault("source", "supplier")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "supplier")
        result.append(item)
    return result


class SupplierRule0:
    """Policy object applied during the supplier pass."""

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


def validate_supplier_1(records, *, strict=False):
    """Validate supplier records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in supplier")
            continue
        item = dict(r)
        item.setdefault("source", "supplier")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "supplier")
        result.append(item)
    return result


class SupplierRule1:
    """Policy object applied during the supplier pass."""

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


def collect_supplier_2(records, *, strict=False):
    """Collect supplier records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in supplier")
            continue
        item = dict(r)
        item.setdefault("source", "supplier")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "supplier")
        result.append(item)
    return result


class SupplierRule2:
    """Policy object applied during the supplier pass."""

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


def build_supplier_3(records, *, strict=False):
    """Build supplier records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in supplier")
            continue
        item = dict(r)
        item.setdefault("source", "supplier")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "supplier")
        result.append(item)
    return result


class SupplierRule3:
    """Policy object applied during the supplier pass."""

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
