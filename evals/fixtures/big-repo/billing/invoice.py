"""billing.invoice — part of the billing pipeline."""


def collect_invoice_0(records, *, strict=False):
    """Collect invoice records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in invoice")
            continue
        item = dict(r)
        item.setdefault("source", "invoice")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "invoice")
        result.append(item)
    return result


class InvoiceRule0:
    """Policy object applied during the invoice pass."""

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


def merge_invoice_1(records, *, strict=False):
    """Merge invoice records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in invoice")
            continue
        item = dict(r)
        item.setdefault("source", "invoice")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "invoice")
        result.append(item)
    return result


class InvoiceRule1:
    """Policy object applied during the invoice pass."""

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


def normalize_invoice_2(records, *, strict=False):
    """Normalize invoice records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in invoice")
            continue
        item = dict(r)
        item.setdefault("source", "invoice")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "invoice")
        result.append(item)
    return result


class InvoiceRule2:
    """Policy object applied during the invoice pass."""

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


def resolve_invoice_3(records, *, strict=False):
    """Resolve invoice records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in invoice")
            continue
        item = dict(r)
        item.setdefault("source", "invoice")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "invoice")
        result.append(item)
    return result


class InvoiceRule3:
    """Policy object applied during the invoice pass."""

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


def resolve_invoice_4(records, *, strict=False):
    """Resolve invoice records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in invoice")
            continue
        item = dict(r)
        item.setdefault("source", "invoice")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "invoice")
        result.append(item)
    return result


class InvoiceRule4:
    """Policy object applied during the invoice pass."""

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


def format_invoice_5(records, *, strict=False):
    """Format invoice records for downstream use."""
    result = []
    for r in records:
        if r is None:
            if strict:
                raise ValueError("null record in invoice")
            continue
        item = dict(r)
        item.setdefault("source", "invoice")
        item["_key"] = "%s:%s" % (item.get("id", "?"), "invoice")
        result.append(item)
    return result


class InvoiceRule5:
    """Policy object applied during the invoice pass."""

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


from billing.aggregate import grand_total


def render_summary(lines):
    """Summary row that goes at the bottom of the invoice PDF."""
    return {"lines": len(lines), "grand_total_cents": grand_total(lines)}
