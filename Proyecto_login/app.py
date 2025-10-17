from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf.csrf import CSRFProtect
import psycopg2
from models.usuario import Usuario
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = '00000'

#Seguridad csrf
csrf = CSRFProtect(app)
#Login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

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
    contraseña_formulario = request.form['contraseña']

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE correo=%s", (correo,))
    datos = cursor.fetchone()

    if datos:
        usuario = Usuario(datos[0], datos[1], datos[2], datos[3])
        if check_password_hash(usuario.get_contraseña(), contraseña_formulario):
            login_user(usuario)
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
        #Genera el hash

        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE correo=%s", (correo,))
        if cursor.fetchone():
            return render_template('registro.html', mensaje="El correo ya está registrado")
        
        hash_contraseña = generate_password_hash(contraseña)   
        cursor.execute("INSERT INTO usuarios (nombre, correo, contraseña) VALUES (%s, %s, %s)", 
                   (nombre, correo, hash_contraseña))
        conexion.commit()
        return redirect('/')

    return render_template('registro.html')

@app.route('/inicio')
@login_required
def pagina_inicio():
    return render_template('inicio.html', nombre=current_user.get_nombre())
    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.route('/recuperar', methods=['GET', 'POST'])
def recuperar():
    if request.method == 'POST':
        correo = request.form['correo']

        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE correo=%s", (correo,))
        usuario = cursor.fetchone()

        if usuario:
            mensaje = f"Se ha enviado un enlace de recuperación al {correo}."
        else: 
            mensaje = "No existe una cuenta con ese correo."
        return render_template('recuperar.html', mensaje=mensaje)
    return render_template('recuperar.html')

@login_manager.user_loader
def load_user(user_id):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
    datos = cursor.fetchone()
    if datos:
        return Usuario(datos[0], datos[1], datos[2], datos[3])
    return None

if __name__ == '__main__':
    app.run(debug=True)