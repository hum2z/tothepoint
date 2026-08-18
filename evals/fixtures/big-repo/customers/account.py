"""customers.account — part of the customers pipeline."""


def collect_account_0(records, *, strict=False):
    """Collect account records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in account")
            continue
        item = dict(r)
        item.setdefault("source", "account")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "account")
        result.append(item)
    return result


class AccountRule0:
    """Policy object applied during the account pass."""

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


def resolve_account_1(records, *, strict=False):
    """Resolve account records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in account")
            continue
        item = dict(r)
        item.setdefault("source", "account")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "account")
        result.append(item)
    return result


class AccountRule1:
    """Policy object applied during the account pass."""

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


def format_account_2(records, *, strict=False):
    """Format account records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in account")
            continue
        item = dict(r)
        item.setdefault("source", "account")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "account")
        result.append(item)
    return result


class AccountRule2:
    """Policy object applied during the account pass."""

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


def normalize_account_3(records, *, strict=False):
    """Normalize account records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in account")
            continue
        item = dict(r)
        item.setdefault("source", "account")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "account")
        result.append(item)
    return result


class AccountRule3:
    """Policy object applied during the account pass."""

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


def resolve_account_4(records, *, strict=False):
    """Resolve account records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in account")
            continue
        item = dict(r)
        item.setdefault("source", "account")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "account")
        result.append(item)
    return result


class AccountRule4:
    """Policy object applied during the account pass."""

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


def normalize_account_5(records, *, strict=False):
    """Normalize account records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in account")
            continue
        item = dict(r)
        item.setdefault("source", "account")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "account")
        result.append(item)
    return result


class AccountRule5:
    """Policy object applied during the account pass."""

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


def collect_account_6(records, *, strict=False):
    """Collect account records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in account")
            continue
        item = dict(r)
        item.setdefault("source", "account")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "account")
        result.append(item)
    return result


class AccountRule6:
    """Policy object applied during the account pass."""

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
