#  kurimypyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of kurimypyrogram.
#
#  kurimypyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  kurimypyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with kurimypyrogram.  If not, see <http://www.gnu.org/licenses/>.

from typing import List, Union, Iterable

import kurimypyrogram
from kurimypyrogram import raw
from kurimypyrogram import types


class PinStories:
    async def pin_stories(
        self: "kurimypyrogram.Client",
        chat_id: Union[int, str],
        stories_ids: Union[int, Iterable[int]],
        pinned: bool = False,
    ) -> List[int]:
        """Pin one or more stories in a chat by using stories identifiers.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".

            stories_ids (``int`` | Iterable of ``int``, *optional*):
                List of unique identifiers of the target stories.

            pinned (``bool``):
                If set to ``True``, the stories will be pinned.

        Returns:
            List of ``int``: List of pinned stories IDs

        Example:
            .. code-block:: python

                # Pin a single story
                await app.pin_stories(chat_id, 123456789, True)

        """
        is_iterable = not isinstance(stories_ids, int)
        stories_ids = list(stories_ids) if is_iterable else [stories_ids]

        r = await self.invoke(
            raw.functions.stories.TogglePinned(
                peer=await self.resolve_peer(chat_id),
                id=stories_ids,
                pinned=pinned
            )
        )

        return types.List(r)
