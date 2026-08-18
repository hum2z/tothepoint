"""billing.credit_note — part of the billing pipeline."""


def build_credit_note_0(records, *, strict=False):
    """Build credit_note records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in credit_note")
            continue
        item = dict(r)
        item.setdefault("source", "credit_note")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "credit_note")
        result.append(item)
    return result


class CreditNoteRule0:
    """Policy object applied during the credit_note pass."""

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


def expand_credit_note_1(records, *, strict=False):
    """Expand credit_note records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in credit_note")
            continue
        item = dict(r)
        item.setdefault("source", "credit_note")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "credit_note")
        result.append(item)
    return result


class CreditNoteRule1:
    """Policy object applied during the credit_note pass."""

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


def merge_credit_note_2(records, *, strict=False):
    """Merge credit_note records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in credit_note")
            continue
        item = dict(r)
        item.setdefault("source", "credit_note")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "credit_note")
        result.append(item)
    return result


class CreditNoteRule2:
    """Policy object applied during the credit_note pass."""

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


def format_credit_note_3(records, *, strict=False):
    """Format credit_note records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in credit_note")
            continue
        item = dict(r)
        item.setdefault("source", "credit_note")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "credit_note")
        result.append(item)
    return result


class CreditNoteRule3:
    """Policy object applied during the credit_note pass."""

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
