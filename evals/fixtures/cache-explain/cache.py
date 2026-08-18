"""In-process TTL cache used by the profile service."""
import functools
import logging
import threading
import time

log = logging.getLogger(__name__)

_LOCK = threading.Lock()
_CACHE = {}   # key -> (value, expires_at)
_STALE = {}   # key -> last value we are willing to serve if the backend is down


def ttl_cache(ttl_seconds):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            key = (fn.__name__, args, tuple(sorted(kwargs.items())))
            now = time.time()

            with _LOCK:
                hit = _CACHE.get(key)
                if hit is not None and hit[1] > now:
                    return hit[0]

            try:
                value = fn(*args, **kwargs)
            except Exception:
                log.debug("refresh failed for %s", key)
                with _LOCK:
                    fallback = _STALE.get(key)
                if fallback is None:
                    raise
                value = fallback

            with _LOCK:
                _CACHE[key] = (value, now + ttl_seconds)
                _STALE[key] = value
            return value

        return wrapper

    return decorator
