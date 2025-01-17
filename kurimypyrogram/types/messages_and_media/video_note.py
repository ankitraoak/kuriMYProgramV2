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

from datetime import datetime
from typing import List

import kurimypyrogram
from kurimypyrogram import raw, utils
from kurimypyrogram import types
from kurimypyrogram.file_id import FileId, FileType, FileUniqueId, FileUniqueType
from ..object import Object


class VideoNote(Object):
    """A video note.

    Parameters:
        file_id (``str``):
            Identifier for this file, which can be used to download or reuse the file.

        file_unique_id (``str``):
            Unique identifier for this file, which is supposed to be the same over time and for different accounts.
            Can't be used to download or reuse the file.

        length (``int``):
            Video width and height as defined by sender.

        duration (``int``):
            Duration of the video in seconds as defined by sender.

        mime_type (``str``, *optional*):
            MIME type of the file as defined by sender.

        file_size (``int``, *optional*):
            File size.

        date (:py:obj:`~datetime.datetime`, *optional*):
            Date the video note was sent.

        ttl_seconds (``int``, *optional*):
            Time-to-live seconds, for one-time media.

        thumbs (List of :obj:`~kurimypyrogram.types.Thumbnail`, *optional*):
            Video thumbnails.
    """

    def __init__(
        self,
        *,
        client: "kurimypyrogram.Client" = None,
        file_id: str,
        file_unique_id: str,
        length: int,
        duration: int,
        thumbs: List["types.Thumbnail"] = None,
        mime_type: str = None,
        file_size: int = None,
        date: datetime = None,
        ttl_seconds: int = None
    ):
        super().__init__(client)

        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.mime_type = mime_type
        self.file_size = file_size
        self.date = date
        self.ttl_seconds = ttl_seconds
        self.length = length
        self.duration = duration
        self.thumbs = thumbs

    @staticmethod
    def _parse(
        client,
        video_note: "raw.types.Document",
        video_attributes: "raw.types.DocumentAttributeVideo",
        ttl_seconds: int = None
    ) -> "VideoNote":
        return VideoNote(
            file_id=FileId(
                file_type=FileType.VIDEO_NOTE,
                dc_id=video_note.dc_id,
                media_id=video_note.id,
                access_hash=video_note.access_hash,
                file_reference=video_note.file_reference
            ).encode(),
            file_unique_id=FileUniqueId(
                file_unique_type=FileUniqueType.DOCUMENT,
                media_id=video_note.id
            ).encode(),
            length=video_attributes.w,
            duration=video_attributes.duration,
            file_size=video_note.size,
            mime_type=video_note.mime_type,
            date=utils.timestamp_to_datetime(video_note.date),
            ttl_seconds=ttl_seconds,
            thumbs=types.Thumbnail._parse(client, video_note),
            client=client
        )
