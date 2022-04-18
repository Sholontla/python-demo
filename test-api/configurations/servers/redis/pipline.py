
import redis

client = redis.Redis(host = "localhost", port = 6379)

pipline = client.pipeline(transaction = False)
pipline.sadd('mydict',f"{{'firstelement': 'value'}}")
pipline.sadd('mydict','secondelement')
pipline.sadd('mydict','thirdelement')
pipline.sadd('mydict','fourthelement')
pipline.sadd('mydict','fifthelement')
print(pipline.smembers('mydict'))
print(pipline.execute())


with client.pipeline() as mypipe:
	print(mypipe.scard('mydict'))