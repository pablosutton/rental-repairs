from flask import render_template, redirect, send_file, session, send_from_directory
from app import app
from app.forms import LandlordForm
from mailmerge import MailMerge
from pathlib import Path
from datetime import date
from random import randint
import hashlib
import os


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    session.pop('file_name', None)
    form = LandlordForm()
    if form.validate_on_submit():
        template = "NoticeTemplate.docx"
        document = MailMerge(template)
        document.merge(
            LandlordName = form.lln.data,
            LandlordAddressLine1 = form.lla.data,
            LandlordSuburb = form.llsu.data,
            LandlordState = form.llst.data,
            LandlordPostCode = str(form.llpc.data),
        )
        n = str(date.today())+str(randint(1,10000))
        bn = n.encode()
        m = hashlib.sha256()
        m.update(bn)
        y = m.hexdigest()
        file_name = "{}.docx".format(y)
        dir = os.getcwd()
        path = Path (dir+'/app/notices')
        os.chdir(path)
        document.write(file_name)
        session['file_name'] = file_name
        return redirect('/download')
    return render_template('home.html', title='Home', form=form)

@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/download_file')
def download_file():
        dir = os.getcwd()
        path = Path ('{}/{}'.format(dir, session['file_name']))
        return send_file(path, as_attachment=True)
