import asyncio
import httpx
import pytest

from main import app
from database.connection import Settings
from models.events import Event
from models.users import User


@pytest.fixture(scope="session")  # 루프 세션 픽스처
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


async def init_db():
    test_settings = Settings()
    test_settings.DATABASE_URL = (
        "mongodb://localhost:27017/testdb"  # testdb 라는 새로운 DB 사용
    )

    await test_settings.initialize_database()


@pytest.fixture(scope="session")  # 기본 클라이언트 픽스처
async def default_client():
    await init_db()
    async with httpx.AsyncClient(app=app, base_url="http://app") as client:
        yield client
        # 리소스 정리
        await Event.find_all().delete()
        await User.find_all().delete()
