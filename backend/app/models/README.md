# Models

This is where all your database code goes. While I have just `database.py`, it is okay
to separate your code out if necessary (espeically if you find you are getting lots of merge conflicts). This
code should be the layer between the api routes and database operations/actions.

For this solution, you may use either SQLite3 (this may require other slight code modifications) or the SQLAlchemy
ORM. For simplicity, I'd personally go with SQLALchemy, but I leave this design decision to you.