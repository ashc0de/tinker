import os
import sqlite3

os.system('cls')

path='C:\\Users\\ak\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\5ghecb60.default-beta\\places.sqlite'

#print(path + '\n')

db_connection = sqlite3.connect(path)

cursor = db_connection.cursor()

command_dict ={

        1 : "select name from sqlite_schema where type='table'",
        2 : "select name from PRAGMA_TABLE_INFO('moz_places')",
        3 : "select url from moz_places",
        4 : "select name from PRAGMA_TABLE_INFO('moz_bookmarks')",
        5 : "select title from moz_bookmarks where fk is not NULL",
        6 : "select moz_bookmarks.title,moz_places.url from moz_bookmarks INNER JOIN moz_places ON moz_bookmarks.fk=moz_places.id",


        }


returned = cursor.execute(command_dict[6])

for sno,item in enumerate(returned):
    print(f'{sno+1}, {item[0]},\n{item[1]}\n')

print("\n")

db_connection.close()




