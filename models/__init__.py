#!/usr/bin/python3
"""import storage library"""
from models.engine.file_storage import FileStorage

"""storage instance"""
storage = FileStorage()
storage.reload()
