node -e '
const fs = require("fs");
let code = fs.readFileSync("server.js", "utf8");
code = code.replace(/\$5000\.00/g, "$0.05");
code = code.replace(/"price_per_call"\s*:\s*"[^"]+"/g, \x27"price_per_call": "$5000.00"\x27);
fs.writeFileSync("server.js", code);
'
pkill -f node
node server.js &
sleep 1
curl -s http://localhost:3000/verify && echo
