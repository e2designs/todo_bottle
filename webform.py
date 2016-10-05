#!/usr/bin/env python

import os
import web

def make_text(string):
    return string

urls = ('/', 'dropdown')
render = web.template.render('templates/')

app = web.application(urls, globals())

class dropdown():

    def __init__(self):
        self.userid = os.getenv('AUTHENTICATE_UID')
        self.my_form = web.form.Form(
                  web.form.Dropdown('author', args=[], description='author'),
                  web.form.Dropdown('modid', args=[], description='Test Module id')
                  )
        self.my_form.author.args = ['None Selected', 'eevans', 'jenkins', 'userx']

    def GET(self):
        form = self.my_form()
        return render.dropdown(form, "Please select a user.", self.userid)

    def POST(self):
        form = self.my_form()
        form.validates()
        s = form.author.value
        if s == 'eevans':
            form.modid.args = ['None Selected', 'Eric1', 'Eric2']
        elif s == 'jenkins':
            form.modid.args = ['None Selected', 'jenkins1', 'jenkins2']
        elif s == 'userx':
            form.modid.args = ['None Selected', 'weaponx', 'wolverine']
        else:
            form.modid.args = ['None Selected', 'alltests']
        return render.dropdown(form, "User {0} selected".format(s), self.userid)

if __name__ == '__main__':
    app.run()

