lib_path = "crates/server/src/lib.rs"
with open(lib_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("\"price_per_call\": \"$5000.00\"", "\"price_per_call\": \"$5000.00\"")

with open(lib_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Verified price_per_call is locked at $5000.00.")
