curl -s -X POST http://127.0.0.1:8082/api/devicesets/0/scanner \
  -H "Content-Type: application/json" \
  -d '{"action": "stop"}' && echo "Milestone status submitted successfully."
