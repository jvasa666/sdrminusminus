lib_path = "crates/server/src/lib.rs"
with open(lib_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("\"price_per_call\": \"$5000.00\"", "\"price_per_call\": \"$0.05\"")

with open(lib_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Restored price_per_call to $0.05.")
