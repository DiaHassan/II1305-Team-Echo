import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import insert
from platsbanken import platsbanken
#from linkedIn import ...


# Database
database_name = "echo.db"

# Platsbanken
platsbanken_list = platsbanken.run()
insert.send_2d_data(platsbanken_list, database_name)

# LedigaJobb
# ledigajobb_list = ...
# InsertIntoDatabase.send_data(ledigajobb_list)

# LinkedIn
# linkedIn_list = linkedIn.run()
# insert.send_data(linkedIn_list, database_name)




