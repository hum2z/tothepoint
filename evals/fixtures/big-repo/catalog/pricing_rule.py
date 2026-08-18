"""catalog.pricing_rule — part of the catalog pipeline."""


def format_pricing_rule_0(records, *, strict=False):
    """Format pricing_rule records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in pricing_rule")
            continue
        item = dict(r)
        item.setdefault("source", "pricing_rule")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "pricing_rule")
        result.append(item)
    return result


class PricingRuleRule0:
    """Policy object applied during the pricing_rule pass."""

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


def format_pricing_rule_1(records, *, strict=False):
    """Format pricing_rule records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in pricing_rule")
            continue
        item = dict(r)
        item.setdefault("source", "pricing_rule")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "pricing_rule")
        result.append(item)
    return result


class PricingRuleRule1:
    """Policy object applied during the pricing_rule pass."""

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


def expand_pricing_rule_2(records, *, strict=False):
    """Expand pricing_rule records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in pricing_rule")
            continue
        item = dict(r)
        item.setdefault("source", "pricing_rule")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "pricing_rule")
        result.append(item)
    return result


class PricingRuleRule2:
    """Policy object applied during the pricing_rule pass."""

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


def expand_pricing_rule_3(records, *, strict=False):
    """Expand pricing_rule records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in pricing_rule")
            continue
        item = dict(r)
        item.setdefault("source", "pricing_rule")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "pricing_rule")
        result.append(item)
    return result


class PricingRuleRule3:
    """Policy object applied during the pricing_rule pass."""

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


def resolve_pricing_rule_4(records, *, strict=False):
    """Resolve pricing_rule records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in pricing_rule")
            continue
        item = dict(r)
        item.setdefault("source", "pricing_rule")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "pricing_rule")
        result.append(item)
    return result


class PricingRuleRule4:
    """Policy object applied during the pricing_rule pass."""

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


def resolve_pricing_rule_5(records, *, strict=False):
    """Resolve pricing_rule records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in pricing_rule")
            continue
        item = dict(r)
        item.setdefault("source", "pricing_rule")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "pricing_rule")
        result.append(item)
    return result


class PricingRuleRule5:
    """Policy object applied during the pricing_rule pass."""

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
