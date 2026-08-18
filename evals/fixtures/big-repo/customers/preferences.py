"""customers.preferences — part of the customers pipeline."""


def validate_preferences_0(records, *, strict=False):
    """Validate preferences records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in preferences")
            continue
        item = dict(r)
        item.setdefault("source", "preferences")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "preferences")
        result.append(item)
    return result


class PreferencesRule0:
    """Policy object applied during the preferences pass."""

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


def expand_preferences_1(records, *, strict=False):
    """Expand preferences records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in preferences")
            continue
        item = dict(r)
        item.setdefault("source", "preferences")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "preferences")
        result.append(item)
    return result


class PreferencesRule1:
    """Policy object applied during the preferences pass."""

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


def collect_preferences_2(records, *, strict=False):
    """Collect preferences records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in preferences")
            continue
        item = dict(r)
        item.setdefault("source", "preferences")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "preferences")
        result.append(item)
    return result


class PreferencesRule2:
    """Policy object applied during the preferences pass."""

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


def normalize_preferences_3(records, *, strict=False):
    """Normalize preferences records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in preferences")
            continue
        item = dict(r)
        item.setdefault("source", "preferences")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "preferences")
        result.append(item)
    return result


class PreferencesRule3:
    """Policy object applied during the preferences pass."""

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


def build_preferences_4(records, *, strict=False):
    """Build preferences records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in preferences")
            continue
        item = dict(r)
        item.setdefault("source", "preferences")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "preferences")
        result.append(item)
    return result


class PreferencesRule4:
    """Policy object applied during the preferences pass."""

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


def format_preferences_5(records, *, strict=False):
    """Format preferences records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in preferences")
            continue
        item = dict(r)
        item.setdefault("source", "preferences")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "preferences")
        result.append(item)
    return result


class PreferencesRule5:
    """Policy object applied during the preferences pass."""

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
