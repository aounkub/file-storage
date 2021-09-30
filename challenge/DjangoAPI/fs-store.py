import sys, os, pathlib, random, string
from pathlib import Path
import sqlite3
import datetime

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

parent = pathlib.Path(__file__).parent.resolve()
path = "%s/media/"%(parent)

def main():
    args = sys.argv
    # args[0] = this file name | args[1] = command | args[2] = file name
    if args[1]:
        if args[1] == "upload-file":
            if 4 >= len(args):
                upload(args[2])
            else:
                    print("Please input file name for upload")
        elif args[1] == "delete-file" and args[2]:
            if 4 >= len(args):
                delete(args[2])
            else:
                print("Please input file name for delete")
        elif args[1] == "list-file":
            list()
        else:
            print("error")

def list():
    files_list = os.listdir(path)
    count = 1
    print("File List")
    for file in files_list:
        print(count, file)
        count+=1

def upload(fileName):
    file = os.path.basename(fileName)
    filePath = path+fileName
    if Path(filePath).is_file():
        letters = string.ascii_letters
        randomLetter = ''.join(random.choice(letters) for i in range(10))
        index = fileName.find('.txt')
        fileName = fileName[:index] + randomLetter + fileName[index:]
        filePath = path+fileName
    with open(file, 'rb+') as fd:
        q = fd.read()
        fd.close()
    uploadedFile = open(filePath, 'wb')
    uploadedFile.write(q)
    date = datetime.datetime.now()
    sql = "INSERT INTO FileStorageApp_filestorage (FileName, UpdateDate) VALUES ('%s', '%s')"% (fileName, date.strftime("%Y-%m-%d"))
    cur.execute(sql)
    con.commit()
    uploadedFile.close()


def delete(fileName):
    delete_file = path+fileName
    id = 0
    res = cur.execute("SELECT FileId FROM FileStorageApp_filestorage WHERE FileName = '%s'"% fileName)
    for row in res:
        id = row[0]
    if(Path(delete_file).is_file()):
        if id:
            sql = "DELETE FROM FileStorageApp_filestorage WHERE FileId = ?"
            cur.execute(sql, (id,))
        con.commit()
        os.remove(delete_file)
        print("deleted")
    else:
        print("%s is not in the folder"% fileName)

if __name__ == "__main__":
    main()