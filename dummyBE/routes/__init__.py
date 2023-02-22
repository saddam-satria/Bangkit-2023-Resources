# from routes.students import studentRoute
from routes.test import testRoute

def routing(app):
    # app.include_router(studentRoute)
    app.include_router(testRoute)