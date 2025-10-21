import re
from flask import Flask, render_template, request, redirect, url_for, session, flash
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
    
def validar_contraseña(contraseña):
    #!Valida la contraseña con unos parámetros
    errores = []
    if len(contraseña) <8:
        errores.append("Debe tener al menos 8 caracteres.")
    if not re.search(r"[A-Z]", contraseña):
        errores.append("Debe contener al menos una letra mayúscula.")
    if not re.search(r"[0-9]", contraseña):
        errores.append("Debe contener al menos un número")
    if not re.search(r"[\W_]", contraseña):
        errores.append("Debe contener al menos un caracter especial")
    return errores

@app.route('/registro', methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        #*Confirmar contraseña
        confirmar_contraseña = request.form['confirmar_contraseña']
        #Verificar si coinciden, si no coinciden recarga la página pero sin perder la información ingresada
        if contraseña != confirmar_contraseña:
            return render_template('registro.html',
                                   mensaje_error="Las contraseñas no coinciden.",
                                   nombre = nombre,
                                   correo = correo)
        errores_pass = validar_contraseña(contraseña)
        if errores_pass:
        #Si hay errores se recarga y muestra el error
            return render_template('registro.html', 
                                   mensaje_error_pass=errores_pass,
                                   nombre=nombre, 
                                   correo=correo)
        #Verificar correo duplicado
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE correo=%s", (correo,))
        if cursor.fetchone():
            return render_template('registro.html',
                                   mensaje_error="El correo ya está registrado.",
                                   nombre = nombre,
                                   correo = correo)
        
        hash_contraseña = generate_password_hash(contraseña)   
        cursor.execute("INSERT INTO usuarios (nombre, correo, contraseña) VALUES (%s, %s, %s)", 
                   (nombre, correo, hash_contraseña))
        conexion.commit()
        
        flash('Te has registrado exitosamente! Ahora puedes iniciar sesión.','success')
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
        passwordnew = request.form['contraseña']
        confirmar = request.form['confirmar']

        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE correo=%s", (correo,))
        usuario = cursor.fetchone()

        if passwordnew != confirmar:
            return render_template('recuperar.html',
                                   mensaje_error="Las contraseñas no coinciden.",
                                   correo = correo,)
        
        errores_pass = validar_contraseña(passwordnew)
        if errores_pass:
            return render_template('recuperar.html',
                                   mensaje_error="Las contraseñas no coinciden.",
                                   correo = correo)

        hash_nueva_contraseña = generate_password_hash(passwordnew)
        cursor.execute("UPDATE usuarios SET contraseña = %s WHERE correo = %s", (hash_nueva_contraseña, correo))
        conexion.commit()

        flash('Has cambiado tu contraseña exitosamente, ahora puedes iniciar sesión.','success')
        return redirect('/')
    return render_template('recuperar.html')

@app.route('/catalogo', methods=['GET'])
def catalogo():
    #cursor = conexion.cursor()
    #cursor.execute("SELECT nombre_columna_imagen FROM categoria WHERE nombre='Luffy'",)
    #if cursor.fetchone():
        #return render_template


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