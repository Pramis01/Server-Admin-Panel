from flask import Flask, render_template_string
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    try:
        uptime = subprocess.check_output(['uptime', '-p']).decode().strip()
    except Exception:
        uptime = 'uptime not available'
    html = """
    <html>
      <head><title>Server Admin</title></head>
      <body style='font-family:sans-serif;background:#111;color:#eee;text-align:center'>
        <h1>Server Admin Panel</h1>
        <p>Uptime: {{ uptime }}</p>
        <p>Hvis du ser dette, funker Flask ✅</p>
      </body>
    </html>
    """
    return render_template_string(html, uptime=uptime)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


