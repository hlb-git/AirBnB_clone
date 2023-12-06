from models.engine import file_storage

"""CNC - dictionary = { Class Name (string) : Class Type }"""

    CNC = file_storage.FileStorage.CNC
    storage = file_storage.FileStorage()
    storage.reload()
