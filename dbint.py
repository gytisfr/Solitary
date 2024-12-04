#I genuinely hate this stupid stupid database thing
#Who let SQL Exist, it works like it was invented 300 years ago
#a woi jse ujgiugs igseiufhiifuwa ofahu

import sqlite3, os

os.chdir(os.getcwd())

class currin:
    def insert(userid, time):
        conn = sqlite3.connect("db")
        c = conn.cursor()
        
        c.execute(f"INSERT INTO currin VALUES('{userid}', '{time}')")
        
        conn.commit()
    
    def update(userid, time):
        conn = sqlite3.connect("db")
        c = conn.cursor()
        
        c.execute(f"UPDATE currin SET time = '{time}' WHERE userid = '{userid}'")

        conn.commit()

    def remove(userid):
        conn = sqlite3.connect("db")
        c = conn.cursor()
        
        c.execute(f"DELETE FROM currin WHERE userid = '{userid}'")
        
        conn.commit()
    
    def get(userid):
        conn = sqlite3.connect("db")
        c = conn.cursor()
        
        d = c.execute(f"SELECT * FROM currin WHERE userid = '{userid}'")
        
        return d.fetchall()[0][1] if d.fetchall() else False
    
    def fetch():
        conn = sqlite3.connect("db")
        c = conn.cursor()
        
        d = c.execute("SELECT * FROM currin")
        
        return d.fetchall()
        
    def check(userid):
        db = currin.fetch()
        userids = [el[0] for el in db]
        return (userid in userids)

class payload:
    def insert(userid):
        conn = sqlite3.connect("db")
        c = conn.cursor()
        
        c.execute(f"INSERT INTO payload VALUES('{userid}')")
        
        conn.commit()

    def remove(userid):
        conn = sqlite3.connect("db")
        c = conn.cursor()
        
        c.execute(f"DELETE FROM payload WHERE userid = '{userid}'")
        
        conn.commit()
    
    def fetch():
        conn = sqlite3.connect("db")
        c = conn.cursor()
        
        d = c.execute("SELECT * FROM payload")
        
        return d.fetchall()
        
    def check(userid):
        db = payload.fetch()
        userids = [el[0] for el in db]
        return (userid in userids)


#This is the only part of the entire project anyone helped me
#Thank you Tallis for knowing SQL, But where the hell is the rest of the team

def createdb():
    conn = sqlite3.connect("db")
    c = conn.cursor()
    
    c.execute("CREATE TABLE currin ([userid] TEXT PRIMARY KEY NOT NULL, [time] TEXT NOT NULL)")
    c.execute("CREATE TABLE payload ([userid] TEXT PRIMARY KEY NOT NULL)")
    
    conn.commit()




"""
{
    "users": {
        "123": "in 3 seconds",
        "456": "time object",
        "789": "time object"
    },
    "payload": {
    }
}
"""