from functools import wraps
from flask_login import current_user

def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.rulechildren[0].rule not in roles:
                return "No access",403
            return f(*args, **kwargs)
        return wrapped
    return wrapper