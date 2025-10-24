

from core.CacheRepositories.JsonCacheRepository import JsonCacheRepository
from core.ApiRepositories.HttpApiRepository import HttpApiRepository

CACH_REPOSITORY=JsonCacheRepository(path="./data.json")
API_REPOSITORY=HttpApiRepository("localhost",8000)
