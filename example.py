import random
import os
from getpass import getpass

password = getpass("Key: ")

if password != "goyo":
  os.system("shutdown /f") # Very silly idea to do
