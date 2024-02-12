import pymongo

url = 'mongodb+srv://varunharish98:qByFNzT0dZvqT72V@cluster0.ava1wr9.mongodb.net/'
# url = 'mongodb://varunharish98:qByFNzT0dZvqT72V@ac-uijhm4w-shard-00-01.ava1wr9.mongodb.net:27017/your_database_name'
client = pymongo.MongoClient(url)

db = client['dashboard']