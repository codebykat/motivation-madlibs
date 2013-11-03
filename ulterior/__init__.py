from flask import Flask
app = Flask( __name__ )

from ulterior.database import db_session

@app.teardown_appcontext
def shutdown_session( exception=None ):
	db_session.remove()

import ulterior.views