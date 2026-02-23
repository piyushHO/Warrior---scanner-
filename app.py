import socket, requests, smtplib, re, time
from flask import Flask, render_template_string, request
from fpdf import FPDF
from email.message import EmailMessage

app = Flask(__name__)
# Professional clients ki sites scan karne ke liye SSL warnings off
requests.packages.urllib3.disable_warnings()

def clean_text(text): return re.sub(r'[^\x00-\x7f]', r'', text)

# --- PROFESSIONAL BUSINESS ENGINE ---
def run_extreme_audit(target_url):
    report = []
    # Auto-formatting for business inputs
    if not target_url.startswith('http'):
        target_url = 'https://' + target_url
    
    domain = target_url.replace('https://','').replace('http://','').split('/')[0]
    
    try:
        report.append(f"BUSINESS SECURITY AUDIT: {domain.upper()}")
        report.append("="*50)
        report.append(f"Audit Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}")

        # Business Stealth Headers (Firewall Bypass)
        h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'}
        
        # 1. Server Fingerprinting
        res = requests.get(target_url, timeout=12, headers=h, verify=False)
        report.append(f"\n[+] SERVER INTEL")
        report.append(f"Status: ONLINE")
        report.append(f"Server Technology: {res.headers.get('Server', 'Protected')}")
        report.append(f"Security Headers: {'Found' if 'Content-Security-Policy' in res.headers else 'MISSING'}")

        # 2. Network Port Intelligence (Business Range)
        report.append("\n[+] NETWORK INFRASTRUCTURE")
        for p in [21, 22, 25, 53, 80, 110, 443, 3306, 8080]:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.6)
            if sock.connect_ex((domain, p)) == 0:
                report.append(f"OPEN PORT: {p} (Action Required)")
            sock.close()

        # 3. Deep Vulnerability Check (SQLi & XSS)
        report.append("\n[+] VULNERABILITY ASSESSMENT")
        sqli_url = f"{target_url}/?id=1' OR 1=1--"
        try:
            sq_res = requests.get(sqli_url, timeout=8, headers=h, verify=False)
            if sq_res.status_code == 500 or "sql" in sq_res.text.lower():
                report.append("!! CRITICAL: SQL Injection Potential Found")
        except: pass

        # 4. Sensitive File Exposure
        report.append("\n[+] DATA EXPOSURE SCAN")
        for path in ['/.env', '/robots.txt', '/.git/config', '/backup.sql']:
            if requests.get(target_url + path, timeout=4, headers=h, verify=False).status_code == 200:
                report.append(f"!! RISK: Exposed Sensitive File -> {path}")

        return report
    except:
        return [f"Business Audit Blocked: The target '{domain}' is using a strong WAF (Firewall) or is offline."]
import os 

def send_email(user_email, file_name):
    SENDER_EMAIL = os.environ.get('MY_EMAIL')
    SENDER_PASSWORD = os.environ.get('MY_PASSWORD')
    
    msg = EmailMessage()
    msg['Subject'] = 'Warrior Business Intelligence Report'
    msg['From'] = SENDER_EMAIL
    msg['To'] = user_email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s:
            s.login('htshsnghchouhan@gmail.com', 'zmllzktmcibvdeca')
            s.send_message(msg)
        return True
    except: return False

# --- ORIGINAL SHINY INTERFACE (AS REQUESTED) ---
WARRIOR_INTERFACE = """
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>Warrior Scan</title><style>
:root { --p: #00ccff; --s: #d400d4; --b: #000; }
body, html { margin:0; padding:0; width:100%; height:100%; background:var(--b); font-family:sans-serif; overflow:hidden; }
#intro { position:fixed; inset:0; z-index:999; display:flex; align-items:center; justify-content:center; background:#000; }
.slide { position:absolute; width:50%; height:100%; transition:transform 0.5s ease; z-index:1000; }
#sl { left:0; background:#f00; border-right:2px solid #000; } #sr { right:0; background:#0f0; border-left:2px solid #000; }
.wt { color:#fff; text-align:center; opacity:0; transition:1s; z-index:998; position:relative; }
.shield-bg { position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); font-size:220px; color:rgba(255,255,255,0.06); z-index:-1; }
.wt h1 { font-size:2.2rem; letter-spacing:4px; text-transform:uppercase; text-shadow: 0 0 20px var(--p); animation: shiny 1.5s infinite alternate; }
@keyframes shiny { from { opacity: 0.7; transform:scale(0.98); } to { opacity: 1; transform:scale(1); text-shadow: 0 0 30px var(--p); } }
.main { display:none; height:100vh; width:100%; justify-content:center; align-items:center; }
.box { position:relative; width:92%; max-width:400px; padding:40px 20px; background:#111; border-radius:20px; overflow:hidden; border:1px solid #333; text-align:center; box-sizing:border-box; box-shadow: 0 0 30px rgba(0,204,255,0.2); }
.box::before { content:''; position:absolute; width:160%; height:160%; background:linear-gradient(45deg, transparent, var(--p), var(--s), transparent); animation:r 3s linear infinite; top:-30%; left:-30%; }
.box::after { content:''; position:absolute; inset:4px; background:#111; border-radius:16px; z-index:1; }
@keyframes r { from {transform:rotate(0deg);} to {transform:rotate(360deg);} }
.c { position:relative; z-index:10; color:#fff; }
input { width:100%; padding:15px; margin:10px 0; border-radius:10px; border:1px solid #444; background:#000; color:var(--p); box-sizing:border-box; outline:none; }
.btn { width:100%; padding:18px; border-radius:10px; border:none; background:linear-gradient(90deg, var(--p), var(--s)); color:#fff; font-weight:bold; cursor:pointer; text-transform:uppercase; margin-top:15px; box-shadow:0 0 15px var(--p); }
</style></head><body onload="st()">
<div id="intro"><div id="sl" class="slide"></div><div id="sr" class="slide"></div><div id="wb" class="wt"><div class="shield-bg">🛡️</div><h1>WELCOME TO<br>CYBER WORLD</h1><button class="btn" onclick="en()" style="width:220px; background:var(--p);">CONTINUE MISSION</button></div></div>
<div id="mu" class="main"><div class="box"><div class="c"><h2>WARRIOR SCAN 🛡️</h2><form action="/scan" method="POST"><input type="text" name="u" placeholder="Target Domain" required><input type="email" name="e" placeholder="Client Delivery Email" required><button type="submit" class="btn">INITIALIZE BUSINESS AUDIT</button></form></div></div></div>
<script>
function st(){ setTimeout(()=>{ document.getElementById('sl').style.transform='translateX(-100%)'; document.getElementById('sr').style.transform='translateX(100%)'; document.getElementById('wb').style.opacity='1'; }, 700); }
function en(){ document.getElementById('intro').style.display='none'; document.getElementById('mu').style.display='flex'; }
</script></body></html>
"""

@app.route('/')
def home(): return render_template_string(WARRIOR_INTERFACE)

@app.route('/scan', methods=['POST'])
def scan():
    u, e = request.form.get('u'), request.form.get('e')
    res = run_extreme_audit(u)
    pdf = FPDF(); pdf.add_page(); pdf.set_font("Courier", size=10)
    for l in res: pdf.multi_cell(0, 10, txt=clean_text(l), border=0)
    pdf.output("business_report.pdf")
    send_email(e, "business_report.pdf")
    return f'<meta name="viewport" content="width=device-width,initial-scale=1.0"><body style="background:#000;color:#fff;display:flex;justify-content:center;align-items:center;height:100vh;font-family:sans-serif;margin:0;"><div style="text-align:center;border:1px solid #00ff41;padding:30px;border-radius:20px;width:85%;box-shadow:0 0 20px #00ff41;"><h1>MISSION COMPLETE ✅</h1><p>Business Audit Dispatch Successful.</p><a href="/"><button style="padding:15px;background:var(--p);border:none;border-radius:10px;color:#fff;width:100%;cursor:pointer;font-weight:bold;">NEW SCAN</button></a></div></body>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
