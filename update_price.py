path = "crates/server/src/lib.rs"
with open(path, "r", encoding="utf-8") as f:
    code = f.read()

code = code.replace("\"price_per_call\": \"$5000.00\"", "\"price_per_call\": \"$5000.00\"")

with open(path, "w", encoding="utf-8") as f:
    f.write(code)

print("Enterprise pricing locked at $5000.00 per call.")
