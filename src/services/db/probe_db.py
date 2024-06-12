

from services.db.database import DB
#from users_db import DB


def init_db():
    db = DB("./src/services/db/users.db")
    db.insert_user("admin", "admin")

    print(db.get_users())
    #db.close()
    




