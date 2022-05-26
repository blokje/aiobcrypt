"""Async implementation of bcrypt"""

import asyncio
import functools
import os
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, TypeVar

import bcrypt
from typing_extensions import ParamSpec

P = ParamSpec("P")
R = TypeVar("R")

pool = ThreadPoolExecutor(
    max_workers=os.cpu_count() or 1,
    thread_name_prefix="aiobcrypt",
)


def aio(fn: Callable[P, R]) -> Callable[P, "asyncio.Future[R]"]:
    @functools.wraps(fn)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> "asyncio.Future[R]":
        loop = asyncio.get_running_loop()
        return loop.run_in_executor(
            pool, functools.partial(fn, *args, **kwargs)
        )

    return wrapper


gensalt = aio(bcrypt.gensalt)
hashpw = aio(bcrypt.hashpw)
checkpw = aio(bcrypt.checkpw)
kdf = aio(bcrypt.kdf)


async def hashpw_with_salt(password: bytes) -> bytes:
    salt = await gensalt()
    return await hashpw(password, salt)


__all__ = ["gensalt", "hashpw", "checkpw", "kdf", "hashpw_with_salt"]
