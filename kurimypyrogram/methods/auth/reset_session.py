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

import kurimypyrogram
from kurimypyrogram import raw


class ResetSession:
    async def reset_session(
        self: "kurimypyrogram.Client",
        id: int
    ) -> bool:
        """Log out an active authorized session by its hash.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            ``bool``: On success, in case the session is destroyed, True is returned. Otherwise, False is returned.

        """
        r = await self.invoke(
            raw.functions.account.ResetAuthorization(hash=id)
        )

        return r
