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

from .add_contact import AddContact
from .delete_contacts import DeleteContacts
from .get_contacts import GetContacts
from .get_contacts_count import GetContactsCount
from .import_contacts import ImportContacts
from .search_contacts import SearchContacts


class Contacts(
    GetContacts,
    DeleteContacts,
    ImportContacts,
    GetContactsCount,
    AddContact,
    SearchContacts
):
    pass
