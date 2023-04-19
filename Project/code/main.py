from platsbanken import platsbanken
from db import insert


# Platsbanken
platsbanken_list = platsbanken.run()
insert.insert_data(platsbanken_list)

# LedigaJobb
# ledigajobb_list = ...
# InsertIntoDatabase.insert_data(ledigajobb_list)

# LinkedIn
# linkedIn_list = ...
# InsertIntoDatabase.insert_data(linkedIn_list)




