import json
s=open('video.html').read().replace('__ICONS__', open('icons.json').read())
open('built.html','w').write(s)
