import threading, subprocess

def poke():
    subprocess.call('python random_pokemon.py', shell=True)

def real():
    subprocess.call('python random_real_madrid_player.py', shell=True)

def swapi():
    subprocess.call('python swapi.py', shell=True)

threadPoke = threading.Thread(target=poke)
threadReal = threading.Thread(target=real)
threadSwapi = threading.Thread(target=swapi)

threadPoke.start()
threadReal.start()
threadSwapi.start()
