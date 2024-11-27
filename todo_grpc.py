from services.todo import run


async def main():
    await run()  # Передаем сессию в функцию run


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
