import os
import sqlite3
import time
import base64

def gen_guid():
    guid_length=12
    byte_length=int(guid_length / 4 * 3)
    gen_bytes=os.urandom(byte_length)
    guid=base64.b64encode(gen_bytes)
    #print(f'GUID : {guid}, Length: {len(guid)}')
    return guid

def add_new_bookmark(path, url):

    guid=gen_guid()

    db_connection = sqlite3.connect(path)

    cursor = db_connection.cursor()

    split_list = url.split("/")
    prefix = split_list[0]+'//'
    host = split_list[2]

    # add entry to moz_origins

    command = 'INSERT INTO moz_origins (prefix, host, frecency) VALUES (?,?,?)' 

    cursor.execute(
            command, 
            (
                prefix,
                host,
                0
            )
        )
    
    # add entry in moz_places

    #reverse host and add dot at the end
    rev_host=host[::-1] + '.'

    command = 'INSERT INTO moz_places (url, rev_host, visit_count, typed, frecency, guid, foreign_count, origin_id) VALUES (?,?,?,?,?,?,?,?)'

    origin_id = cursor.execute(f"SELECT id FROM moz_origins WHERE host='{host}'").fetchall()[0][0]


    cursor.execute(
            command,
            (
                url,
                rev_host,
                0,
                0,
                -1,
                guid,
                1,
                origin_id
            )
        )

    #add entry in moz_bookmarks

    command = 'INSERT INTO moz_bookmarks (type, fk, parent, position, title, dateAdded, lastModified, guid, syncStatus ) VALUES (?,?,?,?,?,?,?,?,?)'
    parent, position = 0, 0

    fk = cursor.execute(f"SELECT id FROM moz_places WHERE url='{url}'").fetchall()[0][0]
    parent = cursor.execute('SELECT parent FROM moz_bookmarks ORDER BY position DESC LIMIT 1').fetchall()[0][0]
    position = cursor.execute('SELECT position FROM moz_bookmarks ORDER BY position DESC LIMIT 1').fetchall()[0][0] + 1


    cursor.execute(
            command,
            (
                1,
                fk,
                parent,
                position,
                url,
                int(time.time()*(10**6)),
                int(time.time()*(10**6)),
                guid,
                1
            )
        )


    db_connection.commit()

    db_connection.close()

if __name__ == '__main__':

    os.system('cls')

    #path='C:\\Users\\ak\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\5ghecb60.default-beta\\places.sqlite'
    path='places.sqlite'

    url = 'https://pythonforundergradengineers.com/'

    add_new_bookmark(path, url)
