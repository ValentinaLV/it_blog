from app import app
from app import db

from posts.blueprint import posts_

import view

app.register_blueprint(posts_, url_prefix='/blog')

if __name__ == '__main__':
    app.run()









