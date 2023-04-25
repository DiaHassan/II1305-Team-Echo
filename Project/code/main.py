import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# from db import insert
# from ledigajobb import ledigajobb
# from platsbanken import platsbanken
from linkedIn import linkedIn


# Database
# database_name = "echo.db"

# Platsbanken
# platsbanken_list = platsbanken.run()
# insert.send_2d_list(platsbanken_list, database_name)

# LedigaJobb
# ledigajobb_list = ledigajobb.run()
# insert.send_2d_list(ledigajobb_list, database_name)

# LinkedIn
linkedIn_list = linkedIn.run()
# insert.send_2d_list(linkedIn_list, database_name)
