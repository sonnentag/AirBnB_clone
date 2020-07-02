#!/usr/bin/env python3
""" module specific init """

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
