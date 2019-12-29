https://bootsnipp.com/snippets/A36DP

flask db init -> create directory migration

# before commit if you change smth in db
# when you change db model (create file .py with migrations info)
flask db migrate

# do it after pull from git
# when you use db (migrations will implement in current db)
flask db upgrade