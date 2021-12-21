from __future__ import annotations

import asyncio
import socket
from typing import Any, Mapping, Optional

import aiohttp
import async_timeout

from aioherepy.aiohere_api import AioHEREApi


class RoutingApi(AioHEREApi):
    """An asynchronous Python client into the HERE Routing API."""

    def __init__(
        self,
        api_key: str,
        request_timeout: int = 10,
        session: aiohttp.ClientSession | None = None) -> None:
        """Returns a RoutingApi instance.
        Args:
          api_key (str):
            API key taken from HERE Developer Portal.
          request_timeout (int):
            Timeout limit for requests.
          session (Optional[aiohttp.ClientSession]):
            aiohttp client session.
        """

        super(RoutingApi, self).__init__(
            api_key=api_key,
            api_url="https://router.hereapi.com/v8/routes",
            request_timeout=request_timeout,
            session=session
        )
