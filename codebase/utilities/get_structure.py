def explore_structure(obj, level=0, name="root"):
    import numpy as np
    indent = "  " * level
    t = type(obj).__name__

    if isinstance(obj, dict):
        print(f"{indent}{name}: 📘 dict ({len(obj)} keys)")
        for k, v in obj.items():
            explore_structure(v, level + 1, name=f"key '{k}'")

    elif isinstance(obj, list):
        print(f"{indent}{name}: 📗 list ({len(obj)} items)")
        if obj:
            explore_structure(obj[0], level + 1, name="item 0")

    elif isinstance(obj, tuple):
        print(f"{indent}{name}: 📙 tuple ({len(obj)} items)")
        for i, v in enumerate(obj):
            explore_structure(v, level + 1, name=f"item {i}")

    elif isinstance(obj, np.ndarray):
        print(f"{indent}{name}: 📊 ndarray shape={obj.shape} dtype={obj.dtype}")

    else:
        print(f"{indent}{name}: 🔹 {t}")
