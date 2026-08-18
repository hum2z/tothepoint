"""catalog.inventory — part of the catalog pipeline."""


def format_inventory_0(records, *, strict=False):
    """Format inventory records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in inventory")
            continue
        item = dict(r)
        item.setdefault("source", "inventory")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "inventory")
        result.append(item)
    return result


class InventoryRule0:
    """Policy object applied during the inventory pass."""

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


def normalize_inventory_1(records, *, strict=False):
    """Normalize inventory records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in inventory")
            continue
        item = dict(r)
        item.setdefault("source", "inventory")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "inventory")
        result.append(item)
    return result


class InventoryRule1:
    """Policy object applied during the inventory pass."""

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


def expand_inventory_2(records, *, strict=False):
    """Expand inventory records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in inventory")
            continue
        item = dict(r)
        item.setdefault("source", "inventory")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "inventory")
        result.append(item)
    return result


class InventoryRule2:
    """Policy object applied during the inventory pass."""

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


def format_inventory_3(records, *, strict=False):
    """Format inventory records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in inventory")
            continue
        item = dict(r)
        item.setdefault("source", "inventory")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "inventory")
        result.append(item)
    return result


class InventoryRule3:
    """Policy object applied during the inventory pass."""

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


def collect_inventory_4(records, *, strict=False):
    """Collect inventory records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in inventory")
            continue
        item = dict(r)
        item.setdefault("source", "inventory")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "inventory")
        result.append(item)
    return result


class InventoryRule4:
    """Policy object applied during the inventory pass."""

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


def resolve_inventory_5(records, *, strict=False):
    """Resolve inventory records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in inventory")
            continue
        item = dict(r)
        item.setdefault("source", "inventory")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "inventory")
        result.append(item)
    return result


class InventoryRule5:
    """Policy object applied during the inventory pass."""

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


def expand_inventory_6(records, *, strict=False):
    """Expand inventory records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in inventory")
            continue
        item = dict(r)
        item.setdefault("source", "inventory")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "inventory")
        result.append(item)
    return result


class InventoryRule6:
    """Policy object applied during the inventory pass."""

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
