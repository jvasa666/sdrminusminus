target/debug/sdrmm --bind 0.0.0.0:8080 &
sleep 2
curl -s http://localhost:8080/api/v1/devices || curl -s http://localhost:8080/
