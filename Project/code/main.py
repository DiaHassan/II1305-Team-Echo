from platsbanken import platsbanken
from linkedIn import linkedIn
from db import insert
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import insert


database_name = "echo.db"

# Platsbanken
platsbanken_list = platsbanken.run()
insert.insert_data(platsbanken_list, database_name)

# LedigaJobb
# ledigajobb_list = ...
# InsertIntoDatabase.insert_data(ledigajobb_list)

# LinkedIn
linkedIn_list = linkedIn.run()
insert.insert_data(linkedIn_list, database_name)




