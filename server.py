""" server.py """

from flask_todomvc.factory import create_app
try:
    app = create_app()
except:
    pass
app.run(port=8000)
