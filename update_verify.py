import os

needles = ("verify", "price_per_call", "Router::new", ".route(")
skip_dirs = {".git", "target", "node_modules"}

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in skip_dirs]

    for filename in files:
        if not filename.endswith(".rs"):
            continue

        path = os.path.join(root, filename)
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except OSError as exc:
            print(f"Skipped {path}: {exc}")
            continue

        matches = [needle for needle in needles if needle in content]
        if matches:
            print(f"Found {', '.join(matches)} in: {path}")
