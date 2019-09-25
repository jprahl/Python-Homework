import sqlite3

conn = sqlite3.connect('emaildb.sqlite') #creates one if DNE?
cur = conn.cursor() #"handle or variable"

cur.execute('DROP TABLE IF EXISTS Counts') #Keeps from blowing up if table exists

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
#Set up table to build a list of the domains of email addresses
#Later will use reading from an existing file
#Pretend its a dictionary
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    #if "@" not in line: continue
    if not line.startswith('From: '): continue
    pieces = line.split('@')
    org = pieces[1]
        #org = re.findall("(@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", line)
    #if "@" in pieces:
        #org = "@" + pieces.split("@")[1]  #why didn't this work?
      #plucks part for email
    #emailparts = email.split('@')
    #org = emailparts[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))  #begin dictionary
    # ? is a placeholder, to avoid SQL injection (find out more)
    # more of an issue in online applications (not this one)
    # (email,) is a one-touple
    #Doesn't really retrieving the data- cursor sets up for a record set
    row = cur.fetchone() #grab the first one and give it back
    # in row (the information we "get" from the database)
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))

# https://www.sqlite.org/lang_select.html
conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
