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

from typing import Union

import kurimypyrogram
from kurimypyrogram import raw
from kurimypyrogram import enums

class UpdateColor:
    async def update_color(
        self: "kurimypyrogram.Client",
        chat_id: Union[int, str],
        color: Union["enums.ReplyColor", "enums.ProfileColor"],
        background_emoji_id: int = None
    ) -> bool:
        """Update color

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            color (:obj:`~kurimypyrogram.enums.ReplyColor` | :obj:`~kurimypyrogram.enums.ProfileColor`):
                Color type.
                Pass :obj:`~kurimypyrogram.enums.ReplyColor` to set reply color or
                :obj:`~kurimypyrogram.enums.ProfileColor` to set profile color.

            background_emoji_id (``int``, *optional*):
                Unique identifier of the custom emoji.

        Returns:
            ``bool``: On success, in case the passed-in session is authorized, True is returned.

        Example:
            .. code-block:: python

                await app.update_color(chat_id, enums.ReplyColor.RED)
        """
        peer = await self.resolve_peer(chat_id)

        if isinstance(peer, raw.types.InputPeerSelf):
            r = await self.invoke(
                raw.functions.account.UpdateColor(
                    for_profile=isinstance(color, enums.ProfileColor),
                    color=color.value,
                    background_emoji_id=background_emoji_id
                )
            )
        else:
            r = await self.invoke(
                raw.functions.channels.UpdateColor(
                    channel=peer,
                    for_profile=isinstance(color, enums.ProfileColor),
                    color=color.value,
                    background_emoji_id=background_emoji_id
                )
            )

        return bool(r)
