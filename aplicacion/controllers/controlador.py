from aplicacion import app
from flask import Flask, render_template, render_template, request, redirect, session

@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def procesando():
    session['nombre']=request.form['nombre']
    session['ubicacion']=request.form['ubicacion']
    session['lenguaje']=request.form['lenguaje']
    session['comentario']=request.form['comentario']
    session['terminos']=request.form['terminos']
    session['genero']= request.form['genero']
    print(session)

    #Esto es porque el checkbox solo da "on" como información, entonces para traspasarla a la tabla de manera mas coherente
    if session['terminos']== 'on':
        session['terminos']= 'Sí'

    return redirect('/')

@app.route('/result')
def resultado():
    return render_template('resultado.html')

@app.route('/volver',methods=['POST'])
def volver():
    return redirect('/')