from models.engine import file_storage

"""CNT - dictionary = { Class Name (string) : Class Type }"""

CNT = file_storage.FileStorage.CNT
storage = file_storage.FileStorage()
storage.reload()
