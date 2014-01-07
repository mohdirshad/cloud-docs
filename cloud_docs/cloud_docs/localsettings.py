DBNAME="notesdb"
DBUSER="notes"
DBPASSWORD="notes123"
DBHOST="127.0.0.1"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DBNAME,                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': DBUSER,
        'PASSWORD': DBPASSWORD,
        'HOST': DBHOST,                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}