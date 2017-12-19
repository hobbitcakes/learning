import sqlite3

conn = sqlite3.connect('demo.db')

c = conn.cursor()

c.execute('''CREATE TABLE users (username text, email text)''')

c.execute("INSERT INTO users VALUES ('me', 'me@mydomain.com')")

conn.commit()

username, email = 'me', 'me@mydomain.com'

c.execute("INSERT INTO users VALUES (?, ?)", (username, email) )

userlist = [
	('paul', 'paul@gmail.com'), 
	('donny', 'donny@gmail.com'),
]

c.executemany("INSERT INTO users VALUES (?, ?)", userlist)
conn.commit()

username = 'me'

c.execute('SELECT email FROM users WHERE username = ?', (username,))
print c.fetchone()


lookup = ('me',)
