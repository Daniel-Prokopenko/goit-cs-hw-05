import asyncio
from aiopath import AsyncPath
from aioshutil import copyfile
import logging


# logger settings
logging.basicConfig(
    filename="task1/log.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
)


async def read_folder(source, output):
    try:
        if await source.is_dir():
            async for path in source.iterdir():
                if await path.is_dir():
                    await read_folder(path, output)
                else:
                    await copy_file(path, output)
        else:
            await copy_file(source, output)
    except Exception as e:
        logging.error(f"Error processing {source}: {e}")


async def copy_file(file, output):
    try:
        form = file.suffix.lstrip(".")  # file format
        dst = output / form
        await dst.mkdir(
            parents=True, exist_ok=True
        )  # make a dir that will contain files with certain format
        await copyfile(file, dst / file.name)
        logging.info(f"Copied {file} to {dst}")
    except Exception as e:
        logging.error(f"Error copying {file} to {dst}: {e}")


async def main():
    try:
        source = AsyncPath(input("Enter a source folder ===>  "))
        output = AsyncPath(input("Enter an output folder ===>  "))
        await read_folder(source, output)
    except Exception as e:
        logging.error(f"Error in main function: {e}")


if __name__ == "__main__":
    asyncio.run(main())
