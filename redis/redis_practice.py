import redis
import json

r = redis.Redis(host='192.168.20.241', port=31082, db=0)
r.set('titties', 'ass')
r.get('titties')
r.delete('titties')

dict_with_many_data_types = {"hello": {"world": ["test_data"]}}
json_str = json.dumps(dict_with_many_data_types)
r.set("dict_data", json_str)
result = r.get("dict_data")
result = json.loads(result)
print(type(result))
print(result)