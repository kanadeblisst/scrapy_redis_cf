import redis

redis_url = "redis://127.0.0.1:6379"
server = redis.StrictRedis.from_url(redis_url, decode_responses=True)

bf = server.cf()
# redis key
key = "test"
expansion = 2 
# 去重数据量 2**18
capacity = 18
bucket_size =2
if not server.exists(key):
    print(bf.create(key, capacity, expansion=expansion, bucket_size=bucket_size))

for i in range(10):
    print(i, bf.addnx(key, f"http://www.httpbin.org/get?a={i}"))
for i in range(20):
    print(i, bf.addnx(key, f"http://www.httpbin.org/get?a={i}"))
for i in range(10):
    print(i, bf.exists(key, f"http://www.httpbin.org/get?a={i}"))
