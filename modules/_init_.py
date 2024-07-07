#!/usr/bin/python3
"""Initialization method for models package. It initializes the storage."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
