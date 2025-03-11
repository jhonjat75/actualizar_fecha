import os
import datetime
import subprocess

def actualizar_fecha():
    repo_path = "/Users/jhonjairotorres/dev/projects/actualizador_fecha"
    file_path = os.path.join(repo_path, "fecha.txt")
    
    # Obtener la fecha actual en el formato requerido
    fecha_actual = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Escribir la fecha en el archivo
    with open(file_path, "w") as file:
        file.write(fecha_actual + "\n")
    
    # Ejecutar comandos Git
    try:
        subprocess.run(["git", "-C", repo_path, "add", "fecha.txt"], check=True)
        subprocess.run(["git", "-C", repo_path, "commit", "-m", f"Actualizacin de fecha: {fecha_actual}"], check=True)
        subprocess.run(["git", "-C", repo_path, "push", "origin", "main"], check=True)
        print("Fecha actualizada y cambios enviados a Git.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar comandos Git: {e}")

if __name__ == "__main__":
    actualizar_fecha()

