import sqlite3

def open_connection():
    connection = sqlite3.connect('filebase.db')
    query = '''
CREATE TABLE IF NOT EXISTS Files (
    id INTEGER,
    messageID INTEGER,
    label TEXT NOT NULL
);
    '''
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


def addFile(user_id, messageID, label):
    connection = sqlite3.connect('filebase.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Files (id, messageID, label) VALUES (?, ?, ?)', (user_id, messageID, label))
    connection.commit()
    connection.close()

def getFile(user_id, label):
    connection = sqlite3.connect('filebase.db')
    cursor = connection.cursor()
    cursor.execute('SELECT messageID FROM Files WHERE id = ? and label = ?', (user_id, label))
    messageID_result = cursor.fetchall()
    connection.close()
    return messageID_result

def removeFile(user_id, label):
    connection = sqlite3.connect('filebase.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM Files WHERE id = ? and label = ?', (user_id, label))
    connection.commit()
    connection.close()

def listOfFiles(user_id):
    connection = sqlite3.connect('filebase.db')
    cursor = connection.cursor()
    cursor.execute('SELECT label FROM Files WHERE id = ?', (user_id,))
    file_result = cursor.fetchall()
    return file_result

def getListOfFiles(user_id):
    list = listOfFiles(user_id)
    filesString = ''
    for file in list:
        fileString = file[0]
        filesString = filesString + '├── '+ fileString + '\n'
    ind = filesString.rindex('├')
    filesString = filesString[:ind] + '└' + filesString[ind + 1:]
    return filesString