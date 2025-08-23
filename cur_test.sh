curl -X 'POST' \
  'http://127.0.0.1:8000/hotels' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "New York"
}'
