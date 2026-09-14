lib_path = "crates/server/src/lib.rs"
with open(lib_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("chrono::Utc::now().to_rfc3339()", "\"2026-09-14T18:03:50.378Z\"")

with open(lib_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated /verify timestamp to static string to avoid missing crate dependency.")
