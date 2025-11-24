def apply_metadata_filter(results, metadata_filter):
    if not metadata_filter:
        return results.get("matches", [])

    filtered = []
    for m in results.get("matches", []):
        meta = m.get("metadata", {}) or {}
        ok = True
        for k, v in metadata_filter.items():
            if isinstance(v, dict):
                continue
            if meta.get(k) != v:
                ok = False
                break
        if ok:
            filtered.append(m)
    return filtered




