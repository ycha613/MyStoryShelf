from flask import session

def get_username():
    try:
        username = session["user_name"]
    except:
        username = None
    return username