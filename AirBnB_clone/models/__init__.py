#!/usr/bin/python3
"""
Initialization module for the models package.

This module initializes the FileStorage instance
and reloads any stored objects.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

