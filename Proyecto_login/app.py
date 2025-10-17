from flask import Flask, render_template, request, redirect, session
import psycopg2
from models.usuario import Usuario

app = Flask(__name__)
app.secret_key = '00000'

conexion = psycopg2.connect(
    host='localhost',
    database='commerce',
    user='postgres',
    password=''
)

@app.route('/')
def inicio():
    return render_template('login.html')

@app.route('/login', methods =['POST'])
def login():
    correo = request.form['correo']
    contraseña = request.form['contraseña']

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE correo=%s", (correo,))
    datos = cursor.fetchone()

    if datos:
        usuario = Usuario(datos[0], datos[1], datos[2], datos[3])
        if usuario.verificar_contraseña(contraseña):
            session['usuario_id'] = usuario.get_id()
            session['usuario_nombre'] = usuario.get_nombre()
            return redirect('/inicio')
        else:
            return render_template('login.html', mensaje="Contraseña incorrecta")
    else:
        return render_template('login.html', mensaje="Usuario no encontrado")
    
@app.route('/registro', methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contraseña = request.form['contraseña']

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, correo, contraseña) VALUES (%s, %s, %s)",
                       (nombre, correo, contraseña))
        conexion.commit()
        return redirect('/')
    return render_template('registro.html')

@app.route('/inicio')
def pagina_inicio():
    if 'usuario_id' in session:
        nombre = session['usuario_nombre']
        return render_template('inicio.html', nombre = nombre)
    else:
        return redirect('/')
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)