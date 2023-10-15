#!/usr/bin/env python3

"""
init file.
run storage.reloaad
"""

from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
