"""reporting.cohort — part of the reporting pipeline."""


def format_cohort_0(records, *, strict=False):
    """Format cohort records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in cohort")
            continue
        item = dict(r)
        item.setdefault("source", "cohort")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "cohort")
        result.append(item)
    return result


class CohortRule0:
    """Policy object applied during the cohort pass."""

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


def build_cohort_1(records, *, strict=False):
    """Build cohort records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in cohort")
            continue
        item = dict(r)
        item.setdefault("source", "cohort")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "cohort")
        result.append(item)
    return result


class CohortRule1:
    """Policy object applied during the cohort pass."""

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


def format_cohort_2(records, *, strict=False):
    """Format cohort records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in cohort")
            continue
        item = dict(r)
        item.setdefault("source", "cohort")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "cohort")
        result.append(item)
    return result


class CohortRule2:
    """Policy object applied during the cohort pass."""

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


def build_cohort_3(records, *, strict=False):
    """Build cohort records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in cohort")
            continue
        item = dict(r)
        item.setdefault("source", "cohort")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "cohort")
        result.append(item)
    return result


class CohortRule3:
    """Policy object applied during the cohort pass."""

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


def build_cohort_4(records, *, strict=False):
    """Build cohort records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in cohort")
            continue
        item = dict(r)
        item.setdefault("source", "cohort")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "cohort")
        result.append(item)
    return result


class CohortRule4:
    """Policy object applied during the cohort pass."""

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
