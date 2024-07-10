kibana_endpoint=kibana
elasticsearch_endpoint=elasticsearch

until curl -sS "http://${elasticsearch_endpoint}:9200/_cat/health?h=status" | grep -q "green\|yellow"; do
  sleep 1
done

curl -X PUT "http://${elasticsearch_endpoint}:9200/logstash" -H "Content-Type: application/json"

until curl -f -LI "${kibana_endpoint}:5601"; do
  sleep 1
done

curl -X POST "${kibana_endpoint}:5601/api/index_patterns/index_pattern" -H 'kbn-xsrf: true' -H 'Content-Type: application/json' -d'
{
  "index_pattern": {
     "title": "logstash"
  }
}
'
