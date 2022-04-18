import redis

client = redis.Redis(host = "localhost", port = 6379)

pipline = client.pipeline(transaction = True)
pipline.sadd('mylist','firstelement')
pipline.sadd('mylist','secondelement')
pipline.sadd('mylist','thirdelement')
pipline.sadd('mylist','fourthelement')
pipline.sadd('mylist','fifthelement')
print(pipline.smembers('mylist'))
print(pipline.execute())