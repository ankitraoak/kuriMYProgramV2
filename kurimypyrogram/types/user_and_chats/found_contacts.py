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

from typing import Optional

import kurimypyrogram
from kurimypyrogram import raw
from kurimypyrogram import utils
from kurimypyrogram import types
from ..object import Object


class FoundContacts(Object):
    """Chats found by name substring and auxiliary data.

    Parameters:
        my_results (List of :obj:`~kurimypyrogram.types.Chat`, *optional*):
            Personalized results.

        global_results (List of :obj:`~kurimypyrogram.types.Chat`, *optional*):
            List of found chats in global search.
    """

    def __init__(
        self,
        *,
        client: "kurimypyrogram.Client" = None,
        my_results: Optional["types.Chat"] = None,
        global_results: Optional["types.Chat"] = None
    ):
        super().__init__(client)

        self.my_results = my_results
        self.global_results = global_results

    @staticmethod
    def _parse(client, found: "raw.types.contacts.Found") -> "FoundContacts":
        users = {u.id: u for u in found.users}
        chats = {c.id: c for c in found.chats}

        my_results = []
        global_results = []

        for result in found.my_results:
            peer_id = utils.get_raw_peer_id(result)
            peer = users.get(peer_id) or chats.get(peer_id)

            my_results.append(types.Chat._parse_chat(client, peer))

        for result in found.results:
            peer_id = utils.get_raw_peer_id(result)
            peer = users.get(peer_id) or chats.get(peer_id)

            global_results.append(types.Chat._parse_chat(client, peer))

        return FoundContacts(
            my_results=types.List(my_results) or None,
            global_results=types.List(global_results) or None,
            client=client
        )
