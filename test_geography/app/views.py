from . import app
from flask import Flask, request, render_template

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/play')
def play():
    return render_template("play.html")


@app.route('/petr')
def petr():
    return render_template("petr.html")


@app.route('/NYSENASDAQ')
def nysenasdaq():
    return render_template("nysenasdaq.html")


@app.route('/monday')
def monday():
    return render_template("monday.html")


@app.route('/kiev')
def kiev():
    return render_template("kiev.html")


@app.route('/1986')
def chernobyl():
    return render_template("1986.html")


@app.route('/obninsk')
def obninsk():
    return render_template("obninsk.html")


@app.route('/guangzhou')
def guangzhou():
    return render_template("guangzhou.html")


@app.route('/usa')
def theusa():
    return render_template("usa.html")


@app.route('/berlin')
def berlin():
    return render_template("berlin.html")


@app.route('/nordstream2')
def nordstream2():
    return render_template("nordstream2.html")


@app.route('/sabetta')
def sabetta():
    return render_template("sabetta.html")


@app.route('/yangzi')
def yangzi():
    return render_template('yangzi.html')


@app.route('/2009')
def sasuges():
    return render_template('2009.html')


@app.route('/japan')
def japan():
    return render_template('japan.html')


@app.route('/sanmarino')
def sanmarino():
    return render_template('sanmarino.html')


@app.route('/ningbozhoushan')
def ningbozhoushan():
    return render_template('ningbozhoushan.html')


@app.route('/republicofkorea')
def korea():
    return render_template('republicofkorea.html')


@app.route('/diamonds')
def diamonds():
    return render_template('diamonds.html')


@app.route('/CH4')
def ch4():
    return render_template('CH4.html')


@app.route('/commonwealthofaustralia')
def commonwealthofaustralia():
    return render_template('commonwealthofaustralia.html')
