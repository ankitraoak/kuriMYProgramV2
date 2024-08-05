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

from .account import Account
from .advanced import Advanced
from .auth import Auth
from .business import Business
from .bots import Bots
from .chats import Chats
from .contacts import Contacts
from .decorators import Decorators
from .invite_links import InviteLinks
from .messages import Messages
from .password import Password
from .payments import Payments
from .phone import Phone
from .premium import Premium
from .users import Users
from .stories import Stories
from .utilities import Utilities


class Methods(
    Account,
    Advanced,
    Auth,
    Business,
    Bots,
    Contacts,
    Password,
    Payments,
    Phone,
    Premium,
    Chats,
    Users,
    Stories,
    Messages,
    Decorators,
    Utilities,
    InviteLinks,
):
    pass
