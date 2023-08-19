import redis

if __name__ == "__main__":
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)

    key = r.hset(
        "11111111",
        mapping = {
            "111": "value of 111",
            "222": "value of 222",
            "333": "value of 333",
        }
    )
    print("Get key 111 for CID 11111111", r.hget("11111111", "111"))
    print("Get key 111, 222 for CID 11111111", r.hmget("11111111", ["111", "222"]))

    print("Updating value for key 111")
    r.hset("11111111", mapping = {
        "111": "Updated value of 111"
    })
    print("Get key 111 for CID 11111111", r.hget("11111111", "111"))
    print("Get all values for CID 11111111", r.hgetall("11111111"))
    
    r.close()

