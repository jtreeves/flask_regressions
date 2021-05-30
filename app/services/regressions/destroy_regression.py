from app import db
from .find_regression import find_regression

def destroy_regression(user_id, source):
    try:
        found_regression = find_regression(user_id, source)
        
        db.session.delete(found_regression)
        db.session.commit()
        
        return 'Data set deleted', 204
    
    except Exception:
        return 'Data set not found', 404