import redis.asyncio as redis

redis = redis.Redis(host="localhost", port=6379, decode_responses=True)


async def get_books_cache():
    return await redis.get("books")

async def set_books_cache(data: str):
    await redis.set("books", data, ex=60)
