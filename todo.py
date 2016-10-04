#!/usr/bin/env python

import sqlite3
from bottle import Bottle, route, run, debug, template, request

app = Bottle()

@app.route('/todo')
@app.route('/')
def todo_list():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = cursor.fetchall()
    output = template('make_table', rows=result)
    return output

@app.route('/new', method='GET')
def new_item():
    if request.GET.save:
        new = request.GET.task.strip()
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute("INSERT into todo (task,status) VALUES (?,?)", (new, 1))
        new_id = cursor.lastrowid
        conn.commit()
        cursor.close()
        return_html ='<p>The new task was inserted into the database, the ID is %s</p>' % new_id + \
                '\n<form action="/" method="GET">' + \
                '   <input value="Return" type="submit">' + \
                '</form>'
        return return_html

    else:
        return template('new_task.tpl')

@app.route('/edit/<idnum:int>', method='GET')
def edit_item(idnum):
    print 'idnum = {0}'.format(idnum)
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()

    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()
        
        if status == 'open':
            status = 1
        else:
            status = 0

        cursor.execute("Update todo set task = ?, status = ? WHERE id = ?", (edit, status, idnum))

        conn.commit()
        cursor.close()
        return_html = '<p>The item number %s was successfully updated</p>' % idnum + \
                '\n<form action="/" method="GET">' + \
                '   <input value="Return" type="submit">' + \
                '</form>'
        return return_html

    else:
        cursor.execute("SELECT task FROM todo WHERE id = {0}".format(int(idnum)))
        cur_data = cursor.fetchone()

        return template('edit_task', old=cur_data, idnum=idnum)
        
@app.error(403)
def error403(code):
    return 'URL is not correct'

@app.error(404)
def error404(code):
    return 'This is not the page you are looking for'

@app.error(500)
def error500(code):
    return 'Unable to process your request at this time.'

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8080, debug=True, reloader=True)
