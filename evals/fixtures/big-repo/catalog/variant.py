"""catalog.variant — part of the catalog pipeline."""


def collect_variant_0(records, *, strict=False):
    """Collect variant records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in variant")
            continue
        item = dict(r)
        item.setdefault("source", "variant")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "variant")
        result.append(item)
    return result


class VariantRule0:
    """Policy object applied during the variant pass."""

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


def format_variant_1(records, *, strict=False):
    """Format variant records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in variant")
            continue
        item = dict(r)
        item.setdefault("source", "variant")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "variant")
        result.append(item)
    return result


class VariantRule1:
    """Policy object applied during the variant pass."""

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


def collect_variant_2(records, *, strict=False):
    """Collect variant records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in variant")
            continue
        item = dict(r)
        item.setdefault("source", "variant")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "variant")
        result.append(item)
    return result


class VariantRule2:
    """Policy object applied during the variant pass."""

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


def expand_variant_3(records, *, strict=False):
    """Expand variant records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in variant")
            continue
        item = dict(r)
        item.setdefault("source", "variant")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "variant")
        result.append(item)
    return result


class VariantRule3:
    """Policy object applied during the variant pass."""

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


def merge_variant_4(records, *, strict=False):
    """Merge variant records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in variant")
            continue
        item = dict(r)
        item.setdefault("source", "variant")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "variant")
        result.append(item)
    return result


class VariantRule4:
    """Policy object applied during the variant pass."""

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


def normalize_variant_5(records, *, strict=False):
    """Normalize variant records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in variant")
            continue
        item = dict(r)
        item.setdefault("source", "variant")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "variant")
        result.append(item)
    return result


class VariantRule5:
    """Policy object applied during the variant pass."""

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


def resolve_variant_6(records, *, strict=False):
    """Resolve variant records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in variant")
            continue
        item = dict(r)
        item.setdefault("source", "variant")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "variant")
        result.append(item)
    return result


class VariantRule6:
    """Policy object applied during the variant pass."""

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
