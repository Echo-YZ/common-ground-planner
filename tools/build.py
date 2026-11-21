import sys
code = sys.argv[1] if len(sys.argv) > 1 else ''
out = sys.argv[2] if len(sys.argv) > 2 else 'index.html'
hosts = sys.argv[3] if len(sys.argv) > 3 else None
t = open('tools/template.html').read()
for w in (400, 700, 800):
    t = t.replace(f'/*FONT{w}*/', open(f'tools/font{w}.b64').read().strip())
t = t.replace("goatcounter: '',", f"goatcounter: '{code}',")
if hosts:
    t = t.replace("hosts: ['echo-yz.github.io']", f"hosts: {hosts}")
open(out, 'w').write(t)
print('built', out, len(t))
