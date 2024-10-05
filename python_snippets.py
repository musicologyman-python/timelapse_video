    print(f'{name:<85} {size:>12,}')
for name, size in files_and_sizes:
    print(f'{name:<80} {size:>12}')
    print(len(name))
    
from pathlib import Path
files = [p for p in Path.cwd().iterdir() if p.suffix == '.mp4']
files_and_sizes = [(p.name, p.stat().st_size) for p in files]
[len(p.name) for p in files]
max(len(p.name) for p in files)
import operator
files_and_sizes.sort(key=operator.itemgetter(1))
for name, size in files_and_sizes:
    print(f'{name:<80} {size:>12}')
    
for name, size in files_and_sizes:
    print(f'{name:<85} {size:>12,}')
for name, size in files_and_sizes:
    print(f'{name:<80} {size:>12}')
    print(len(name))
    
for name, size in files_and_sizes:
    print(f'{name:<80} {size:>15,}')
    
from pathlib import Path
files = [p for p in Path.cwd().iterdir() if p.suffix == '.mp4']
files_and_sizes = [(p.name, p.stat().st_size) for p in files]
[len(p.name) for p in files]
max(len(p.name) for p in files)
import operator
files_and_sizes.sort(key=operator.itemgetter(1))
for name, size in files_and_sizes:
    print(f'{name:<80} {size:>12}')
    
for name, size in files_and_sizes:
    print(f'{name:<85} {size:>12,}')
for name, size in files_and_sizes:
    print(f'{name:<80} {size:>12}')
    print(len(name))
    
for name, size in files_and_sizes:
    print(f'{name:<80} {size:>15,}')
from pathlib import Path
files = [p for p in Path.cwd().iterdir() if p.suffix == '.mp4']
files_and_sizes = [(p.name, p.stat().st_size) for p in files]
[len(p.name) for p in files]
max(len(p.name) for p in files)
import operator
files_and_sizes.sort(key=operator.itemgetter(1))
for name, size in files_and_sizes:
    print(f'{name:<80} {size:>12}')
    
for name, size in files_and_sizes:
    print(f'{name:<85} {size:>12,}')
for name, size in files_and_sizes:
    print(f'{name:<80} {size:>12}')
    print(len(name))
    
for name, size in files_and_sizes:
    print(f'{name.strip():<80} {size:>15,}')
from pathlib import Path
files = [p for p in Path.cwd().iterdir() if p.suffix == '.mp4']
files_and_sizes = [(p.name, p.stat().st_size) for p in files]
[len(p.name) for p in files]
max(len(p.name) for p in files)
import operator
files_and_sizes.sort(key=operator.itemgetter(1))
for name, size in files_and_sizes:
    print(f'{name:<80} {size:>12}')
    
for name, size in files_and_sizes:
    print(f'{name:<85} {size:>12,}')
for name, size in files_and_sizes:
    print(f'{name:<80} {size:>12}')
    print(len(name))
    
for name, size in files_and_sizes:
    print(f'{name:<80} {size:>15,n}')
from pathlib import Path
files = [p for p in Path.cwd().iterdir() if p.suffix == '.mp4']
files_and_sizes = [(p.name, p.stat().st_size) for p in files]
[len(p.name) for p in files]
max(len(p.name) for p in files)
import operator
files_and_sizes.sort(key=operator.itemgetter(1))
for name, size in files_and_sizes:
    print(f'{name:<80} {size:>12}')
    
for name, size in files_and_sizes:
    print(f'{name:<85} {size:>12,}')
for name, size in files_and_sizes:
    print(f'{name:<80} {size:>12}')
    print(len(name))
    
for name, size in files_and_sizes:
    print(f'{name:<80} {size:>15n}')
from pathlib import Path
files = [p for p in Path.cwd().iterdir() if p.suffix == '.mp4']
files_and_sizes = [(p.name, p.stat().st_size) for p in files]
[len(p.name) for p in files]
max(len(p.name) for p in files)
import operator
files_and_sizes.sort(key=operator.itemgetter(1))
for name, size in files_and_sizes:
    print(f'{name:<80} {size:>12}')
    
for name, size in files_and_sizes:
    print(f'{name:<85} {size:>12,}')
for name, size in files_and_sizes:
    print(f'{name:<80} {size:>12}')
    print(len(name))
    
for name, size in files_and_sizes:
    print(f'{name:@<80} {size:>15n}')
exit()
import yt_dlp
from pathlib import Path
lines = Path('~/Downloads/media/playlist').expanduser().read_text().splitlines()
from pprint import pprint
pprint(lines)
for line in lines:
    print(line[slice(0, line.index('?'))])
    
lines = [line[slice(0, line.index('?'))] for line in lines if len(line.strip()) > 0]
lines
urls = lines
help(yt_dlp.YoutubeDL)
with yt_dlp.YoutubeDL() as ydl:
from pathlib import Path
from pprint import pprint
import yt_dlp
lines = Path('~/Downloads/media/playlist').expanduser().read_text().splitlines()
    
urls = [line[slice(0, line.index('?'))] for line in lines if len(line.strip()) > 0]
with yt_dlp.YoutubeDL({}) as ydl:
    info = ydl.extact_info(urls[0], download=False)
exit()
from pathlib import Path
from pprint import pprint
import yt_dlp
lines = Path('~/Downloads/media/playlist').expanduser().read_text().splitlines()
    
urls = [line[slice(0, line.index('?'))] for line in lines if len(line.strip()) > 0]
with yt_dlp.YoutubeDL({}) as ydl:
    info = ydl.extract_info(urls[0], download=False)
info.keys()
info.get('format')
info.get('formats')
import json
type(info)
with open('info_01.json', mode='w') as fp:
    json.dump(info, fp, indent=2)
    
exit()
import random
some_numbers = [random.randint(0, 10) for _ in range(10)]
from pprint import pprint
pprint(some_numbers)
pprint(some_numbers[::-1])
exit()
from urllib.parse import *
import pyperclip
split_url = urlsplit(pyperclip.paste())
split_url
import urlib.parse as parse
import urllib.parse as parse
parse.parse_qs(split_url.query)
from pprint import pprint
pprint(parse.parse_qs(split_url.query))
parsed_query = parse.parse_qs(split_url.query)
split_url2 = parse.urlsplit(parsed_query['continue'])
split_url2 = parse.urlsplit(parsed_query['continue'][0])
split_url2
parsed_query_2 = parse.parse_qs(split_url2.query)
pprint(parsed_query_2)
exit
exit()
import regex
from pathlib import Path
text = Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').expanduser().read_text()
regex.search(r'(?s)"\[\[Legaman\sad\spaginam\sLatinam\],width=\d+,height=\d+\]", text)
regex.search(r'(?s)\[\[Legaman\sad\spaginam\sLatinam\],width=\d+,height=\d+\]', text)
regex.search(r'(?s)\[\[Legaman\sad\spaginam\sLatinam\]', text)
regex.search(r'(?m)\[\[Legaman\sad\spaginam\sLatinam\]', text)
regex.search(r'(?m)\[\[Legamen\sad\spaginam\sLatinam\]', text)
regex.search(r'(?s)\[\[Legamen\sad\spaginam\sLatinam\]', text)
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\]', text)
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\],width=30,height=20\]', text)
matches = regex.finditer(r'\[\[Legamen\sad\spaginam\sLatinam\],width=30,height=20\]', text)
len(list(matches))
help(regex.Match)
clean_text = regex.replace(r'\[\[Legamen\sad\spaginam\sLatinam\],width=30,height=20\]', '', text)
clean_text = regex.sub(r'\[\[Legamen\sad\spaginam\sLatinam\],width=30,height=20\]', '', text)
from pprint import pprint
pprint(clean_text[:1000])
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\]', text)
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\].\{100}', text)
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\]', clean_text))
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\]', clean_text)
Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').write_text(clean_text)
Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').expanduser().write_text(clean_text)
text = clean_text
matches = regex.finditer(r'link:%0AL\/Roman\/Texts.+?\[image.+?\]', text)
matches = list(matches)
len(matches)
matches[-1]
clean_text = regex.sub(r'link:%0AL\/Roman\/Texts.+?\[image.+?\]', '', text)
import regex
from pathlib import Path
text = Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').expanduser().read_text()
regex.search(r'(?s)"\[\[Legaman\sad\spaginam\sLatinam\],width=\d+,height=\d+\]", text)
regex.search(r'(?s)\[\[Legaman\sad\spaginam\sLatinam\],width=\d+,height=\d+\]', text)
regex.search(r'(?s)\[\[Legaman\sad\spaginam\sLatinam\]', text)
regex.search(r'(?m)\[\[Legaman\sad\spaginam\sLatinam\]', text)
regex.search(r'(?m)\[\[Legamen\sad\spaginam\sLatinam\]', text)
regex.search(r'(?s)\[\[Legamen\sad\spaginam\sLatinam\]', text)
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\]', text)
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\],width=30,height=20\]', text)
matches = regex.finditer(r'\[\[Legamen\sad\spaginam\sLatinam\],width=30,height=20\]', text)
len(list(matches))
help(regex.Match)
clean_text = regex.replace(r'\[\[Legamen\sad\spaginam\sLatinam\],width=30,height=20\]', '', text)
clean_text = regex.sub(r'\[\[Legamen\sad\spaginam\sLatinam\],width=30,height=20\]', '', text)
from pprint import pprint
pprint(clean_text[:1000])
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\]', text)
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\].\{100}', text)
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\]', clean_text))
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\]', clean_text)
Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').write_text(clean_text)
Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').expanduser().write_text(clean_text)
text = clean_text
matches = regex.finditer(r'link:%0AL\/Roman\/Texts.+?\[image.+?\]', text)
matches = list(matches)
len(matches)
matches[-1]
clean_text = regex.sub(r'link:%0AL\/Roman\/Texts.+?\[image.+?\]', '', text)
Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').expanduser().write_text(clean_text)
text = clean_text
PAGE_NUM_RE = regex.compile(r'\[#p\d+\]##\[\.pagenum\]#\sp\d+\s###')
matches = list(PAGE_NUM_RE.finditer(text))
len(matches)
clean_text = PAGE_NUM_RE.sub('', text)
Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').expanduser().write_text(clean_text)
matches = regex.search('.link:%0AE\/Roman\/Texts', clean_text)
matches = regex.search(r'.link:%0AE\/Roman\/Texts', clean_text)
matches[0]
regex.search(r'\u200blink:', clean_text)
print('\u200b')
import unicodedata
unicodedata.name('\u200b')
text = clean_text
clean_text = regex.sub('\u200b', ' ', text)
import regex
from pathlib import Path
text = Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').expanduser().read_text()
regex.search(r'(?s)"\[\[Legaman\sad\spaginam\sLatinam\],width=\d+,height=\d+\]", text)
regex.search(r'(?s)\[\[Legaman\sad\spaginam\sLatinam\],width=\d+,height=\d+\]', text)
regex.search(r'(?s)\[\[Legaman\sad\spaginam\sLatinam\]', text)
regex.search(r'(?m)\[\[Legaman\sad\spaginam\sLatinam\]', text)
regex.search(r'(?m)\[\[Legamen\sad\spaginam\sLatinam\]', text)
regex.search(r'(?s)\[\[Legamen\sad\spaginam\sLatinam\]', text)
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\]', text)
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\],width=30,height=20\]', text)
matches = regex.finditer(r'\[\[Legamen\sad\spaginam\sLatinam\],width=30,height=20\]', text)
len(list(matches))
help(regex.Match)
clean_text = regex.replace(r'\[\[Legamen\sad\spaginam\sLatinam\],width=30,height=20\]', '', text)
clean_text = regex.sub(r'\[\[Legamen\sad\spaginam\sLatinam\],width=30,height=20\]', '', text)
from pprint import pprint
pprint(clean_text[:1000])
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\]', text)
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\].\{100}', text)
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\]', clean_text))
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\]', clean_text)
Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').write_text(clean_text)
Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').expanduser().write_text(clean_text)
text = clean_text
matches = regex.finditer(r'link:%0AL\/Roman\/Texts.+?\[image.+?\]', text)
matches = list(matches)
len(matches)
matches[-1]
clean_text = regex.sub(r'link:%0AL\/Roman\/Texts.+?\[image.+?\]', '', text)
Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').expanduser().write_text(clean_text)
text = clean_text
PAGE_NUM_RE = regex.compile(r'\[#p\d+\]##\[\.pagenum\]#\sp\d+\s###')
matches = list(PAGE_NUM_RE.finditer(text))
len(matches)
clean_text = PAGE_NUM_RE.sub('', text)
Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').expanduser().write_text(clean_text)
matches = regex.search('.link:%0AE\/Roman\/Texts', clean_text)
matches = regex.search(r'.link:%0AE\/Roman\/Texts', clean_text)
matches[0]
regex.search(r'\u200blink:', clean_text)
print('\u200b')
import unicodedata
unicodedata.name('\u200b')
text = clean_text
clean_text = regex.sub('\u200b', ' ', text)
Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').expanduser().write_text(clean_text)
text = clean_text
unicodedata.lookup('SECTION')
unicodedata.name('\u00a7')
CHAPTER_RE = regex.compile(r'\[#(?P<chapter>\d+)\s\.chapter\]#\1#')
matches = list(CHAPTER_RE.finditer(text))
len(matches)
matches[0]
matches[0]['chapter']
clean_text = CHAPTER_RE.sub('===Chapter \1\n', text)
pprint(clean_text[:1000])
pprint(clean_text[1000:2000])
clean_text = CHAPTER_RE.sub('===Chapter \g<1>\r', text)
clean_text = CHAPTER_RE.sub('===Chapter \\g<1>\r', text)
pprint(clean_text[:1000])
pprint(clean_text[1000:2000])
clean_text = CHAPTER_RE.sub('===Chapter \\g<1>\n', text)
pprint(clean_text[:1000])
unicodedata.name('\ua0')
unicodedata.lookup('\ua0')
unicodedata.name('\xa0')
clean_text = regex.sub(r'\xa0', ' ', text)
import regex
from pathlib import Path
text = Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').expanduser().read_text()
regex.search(r'(?s)"\[\[Legaman\sad\spaginam\sLatinam\],width=\d+,height=\d+\]", text)
regex.search(r'(?s)\[\[Legaman\sad\spaginam\sLatinam\],width=\d+,height=\d+\]', text)
regex.search(r'(?s)\[\[Legaman\sad\spaginam\sLatinam\]', text)
regex.search(r'(?m)\[\[Legaman\sad\spaginam\sLatinam\]', text)
regex.search(r'(?m)\[\[Legamen\sad\spaginam\sLatinam\]', text)
regex.search(r'(?s)\[\[Legamen\sad\spaginam\sLatinam\]', text)
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\]', text)
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\],width=30,height=20\]', text)
matches = regex.finditer(r'\[\[Legamen\sad\spaginam\sLatinam\],width=30,height=20\]', text)
len(list(matches))
help(regex.Match)
clean_text = regex.replace(r'\[\[Legamen\sad\spaginam\sLatinam\],width=30,height=20\]', '', text)
clean_text = regex.sub(r'\[\[Legamen\sad\spaginam\sLatinam\],width=30,height=20\]', '', text)
from pprint import pprint
pprint(clean_text[:1000])
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\]', text)
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\].\{100}', text)
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\]', clean_text))
regex.search(r'\[\[Legamen\sad\spaginam\sLatinam\]', clean_text)
Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').write_text(clean_text)
Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').expanduser().write_text(clean_text)
text = clean_text
matches = regex.finditer(r'link:%0AL\/Roman\/Texts.+?\[image.+?\]', text)
matches = list(matches)
len(matches)
matches[-1]
clean_text = regex.sub(r'link:%0AL\/Roman\/Texts.+?\[image.+?\]', '', text)
Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').expanduser().write_text(clean_text)
text = clean_text
PAGE_NUM_RE = regex.compile(r'\[#p\d+\]##\[\.pagenum\]#\sp\d+\s###')
matches = list(PAGE_NUM_RE.finditer(text))
len(matches)
clean_text = PAGE_NUM_RE.sub('', text)
Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').expanduser().write_text(clean_text)
matches = regex.search('.link:%0AE\/Roman\/Texts', clean_text)
matches = regex.search(r'.link:%0AE\/Roman\/Texts', clean_text)
matches[0]
regex.search(r'\u200blink:', clean_text)
print('\u200b')
import unicodedata
unicodedata.name('\u200b')
text = clean_text
clean_text = regex.sub('\u200b', ' ', text)
Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').expanduser().write_text(clean_text)
text = clean_text
unicodedata.lookup('SECTION')
unicodedata.name('\u00a7')
CHAPTER_RE = regex.compile(r'\[#(?P<chapter>\d+)\s\.chapter\]#\1#')
matches = list(CHAPTER_RE.finditer(text))
len(matches)
matches[0]
matches[0]['chapter']
clean_text = CHAPTER_RE.sub('===Chapter \1\n', text)
pprint(clean_text[:1000])
pprint(clean_text[1000:2000])
clean_text = CHAPTER_RE.sub('===Chapter \g<1>\r', text)
clean_text = CHAPTER_RE.sub('===Chapter \\g<1>\r', text)
pprint(clean_text[:1000])
pprint(clean_text[1000:2000])
clean_text = CHAPTER_RE.sub('===Chapter \\g<1>\n', text)
pprint(clean_text[:1000])
unicodedata.name('\ua0')
unicodedata.lookup('\ua0')
unicodedata.name('\xa0')
clean_text = regex.sub(r'\xa0', ' ', text)
Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').expanduser().write_text(clean_text)
text = clean_text
exit()
from pathlib import Path
text = Path('~/Documents/megalopolis/sallust_bellum_catilinae.adoc').expanduser().read_text()
import regex
FOOTNOTE_LINK_REF_RE = regex.compile(r'link:0AE\/Roman\/Texts\/Sallust\/Bellum_Catilinae\*\.html#note(?P<note_num>\d+)%0A[\1]')
matches = list(FOOTNOTE_LINK_REF_RE.finditer(text))
len(matches)
def test_pattern(pattern):
    matches = list(regex.finditer(pattern, texts))
def test_pattern(pattern):
    matches = list(regex.finditer(pattern, text))
    print(f'there are {len(matches)}')
    return matches
test_pattern(r'link:%0AE\/Roman')
results = test_pattern(r'link:%0AE\/Roman\/Texts\/Sallust\/Bellum_Catilinae')
results = test_pattern(r'link:%0AE\/Roman\/Texts\/Sallust\/Bellum_Catilinae\*')
results = test_pattern(r'link:%0AE\/Roman\/Texts\/Sallust\/Bellum_Catilinae\*\.html')
results = test_pattern(r'link:%0AE\/Roman\/Texts\/Sallust\/Bellum_Catilinae\*\.html#')
results = test_pattern(r'link:%0AE\/Roman\/Texts\/Sallust\/Bellum_Catilinae\*\.html#note(\d+)')
results = test_pattern(r'link:%0AE\/Roman\/Texts\/Sallust\/Bellum_Catilinae\*\.html#note(\d+)%0A\[\1\]')
results[0]
results[-1]
pprint(text[107349, 10800])
print(text[107349, 10800])
print(text[107349:10800])
print(text[107349:108000])
print(text[108000:109000])
print(text[109000:110000])
patterns = [r'link:%0AE\/Roman\/Texts\/Sallust\/Bellum_Catilinae\*\.html#note(\d+)%0A\[\1\]']
import pyperclip
pyperclip.copy(patterns[0])
result = test_pattern('link:%0AE\/Roman\/Texts\/Sallust\/Bellum_Catilinae\*\.html')
result = test_pattern(r'link:%0AE\/Roman\/Texts\/Sallust\/Bellum_Catilinae\*\.html')
result = test_pattern(r'link:%0AE\/Roman\/Texts\/Sallust\/Bellum_Catilinae\*\.html#')
result = test_pattern(r'link:%0AE\/Roman\/Texts\/Sallust\/Bellum_Catilinae\*\.html#note')
result = test_pattern(r'link:%0AE\/Roman\/Texts\/Sallust\/Bellum_Catilinae\*\.html#ref')
result = test_pattern(r'link:%0AE\/Roman\/Texts\/Sallust\/Bellum_Catilinae\*\.html#(note|ref)')
result = test_pattern(r'link:%0AE\/Roman\/Texts\/Sallust\/Bellum_Catilinae\*\.html#(?!=(note|ref))')
result = test_pattern(r'link:%0AE\/Roman\/Texts\/Sallust\/Bellum_Catilinae\*\.html#(?!=(note))')
result = test_pattern(r'link:%0AE\/Roman\/Texts\/Sallust\/Bellum_Catilinae\*\.html#(?!(note))')
result = test_pattern(r'link:%0AE\/Roman\/Texts\/Sallust\/Bellum_Catilinae\*\.html#(?!(note|ref))')
results = result
for r in results:
    print(r[0])
    
for r in results:
    print(r.starts)
    
for r in results:
    print(r.start)
    
for r in results:
    print(r.starts)()
for r in results:
    print(r.starts())
for r in results:
    start = r.starts()
for r in results:
    start = r.starts()[0]
    print(text[slice(start, start+110)])
exit()
from bs4 import BeautifulSoup
soup = BeautifulSoup('sallust_bellum_catilinae.html')
with open('sallust_bellum_catilinae.html') as fp:
    soup = BeautifulSoup(fp)
    
image_elements = soup.findAll('img')
len(image_elements)
for img in image_elements:
    img.extract()
    
image_elements = soup.findAll('img')
len(image_elements)
def has_onmouseover(tag):
    return tag.has_attr('onmouseover')
mouseover_elements = soup.findAll(has_mouseover)
mouseover_elements = soup.findAll(has_onmouseover)
len(mouseover_elements)
for e in mouseover_elements:
    x = e.extract()
    
mouseover_elements = soup.findAll(has_onmouseover)
len(mouseover_elements)
with open('sallust_bellum_catilinae.html', mode='w') as fp:
    fp.write(soup.prettify())
    
scripts = soup.findAll('script')
len(scripts)
for script in scripts:
    _ = script.extract()
    
scripts = soup.findAll('script')
len(scripts)
links = soup.findAll('link')
len(links)
for link in links:
    _ = link.extract()
    
from bs4 import BeautifulSoup
soup = BeautifulSoup('sallust_bellum_catilinae.html')
with open('sallust_bellum_catilinae.html') as fp:
    soup = BeautifulSoup(fp)
    
image_elements = soup.findAll('img')
len(image_elements)
for img in image_elements:
    img.extract()
    
image_elements = soup.findAll('img')
len(image_elements)
def has_onmouseover(tag):
    return tag.has_attr('onmouseover')
mouseover_elements = soup.findAll(has_mouseover)
mouseover_elements = soup.findAll(has_onmouseover)
len(mouseover_elements)
for e in mouseover_elements:
    x = e.extract()
    
mouseover_elements = soup.findAll(has_onmouseover)
len(mouseover_elements)
with open('sallust_bellum_catilinae.html', mode='w') as fp:
    fp.write(soup.prettify())
    
scripts = soup.findAll('script')
len(scripts)
for script in scripts:
    _ = script.extract()
    
scripts = soup.findAll('script')
len(scripts)
links = soup.findAll('link')
len(links)
for link in links:
    _ = link.extract()
    
with open('sallust_bellum_catilinae.html', mode='w') as fp:
    fp.write(soup.prettify())
    
tables = soup.findAll('table');print(len(tables))
for t in tables:
    _ = t.extract()
    
with open('sallust_bellum_catilinae.html', mode='w') as fp:
    fp.write(soup.prettify())
    
exit()
from pathlib import Path
lines = Path('persons_glossary_1.txt.txt').read_text().splitlines()
counsel = [f'CC{i} - {line.strip()}' for i, line in enumerate(lines[:6], start=1)]
from pprint import pprint
pprint(counsel)
persons = [f'P{i} - {line.strip()}' for i, line in enumerate(lines[6:], start=1]
persons = [f'P{i} - {line.strip()}' for i, line in enumerate(lines[6:], start=1)]
with Path('persons_glossary_1.txt').open(mode='w') as fp:
    for c in counsel:
        print(c, file=fp)
    for p in persons:
        print(p, file=fp)
        
    
from pathlib import Path
lines = Path('persons_glossary_1.txt.txt').read_text().splitlines()
lines = [line.strip() for line in lines if len(line.strip) > 0]
counsel = [f'CC{i} - {line.strip()}' for i, line in enumerate(lines[:6], start=1)]
from pprint import pprint
pprint(counsel)
persons = [f'P{i} - {line.strip()}' for i, line in enumerate(lines[6:], start=1]
persons = [f'P{i} - {line.strip()}' for i, line in enumerate(lines[6:], start=1)]
with Path('persons_glossary_1.txt').open(mode='w') as fp:
    for c in counsel:
        print(c, file=fp)
    for p in persons:
        print(p, file=fp)
        
    
exit()
from pathlib import Path
from functools import partial
lines = Path('persons_glossary_1.txt.txt').read_text().splitlines()
from pprint import pprint
pprint(lines)
lines[:6]
lawyers = [f'CC{i} - {line}' for i, line in enumerate(lines[:6], start=1)]
pprint(lawyers)
persons = [f'P{i} - {line}' for i, line in enumerate(lines[6:], start=1)]
pprint(persons)
everybody = lawyers + persons
all_together_now = '\n'.join(everybody)
pprint(everybody)
Path('person_glossary_new.txt').write_text(all_together_now)
exit()
from urllib.parse import parse_qs, urlsplit
from pathlib import Path
lines = Path('onetab_urls.txt').read_text().splitlines()
from urllib.parse import unwrap
lines[0]
split_line = urlsplit(lines[0])
split_line
unwrap(lines[0])
len(lines)
len(line for line in lines if line.find(' | ') > -1)
len([line for line in lines if line.find(' | ') > -1])
bad_lines = [line for line in lines if line.find(' | ') == -1]
len(bad_lines)
bad_lines[0]
bad_lines[1]
from pprint import pprint
pprint(bad_lines)
lines = [line for line in lines if len(line.strip()) > 0
]
len(lines)
def split_url_line(line):
    url, description = line.split(' | ')
    return { description: url }
    
urls = [split_url_line(line) for line in lines]
for line in lines:
split_lines = [tuple(line.split(' | ')) for line in lines]
long_lines = [sl for sl in split_lines if len(sl) !=2 ]
len(long_lines)
pprint(long_lines)
help(str.split)
from urllib.parse import parse_qs, urlsplit
from pathlib import Path
lines = Path('onetab_urls.txt').read_text().splitlines()
from urllib.parse import unwrap
split_line = urlsplit(lines[0])
split_line
unwrap(lines[0])
len(lines)
len(line for line in lines if line.find(' | ') > -1)
len([line for line in lines if line.find(' | ') > -1])
bad_lines = [line for line in lines if line.find(' | ') == -1]
len(bad_lines)
bad_lines[0]
bad_lines[1]
from pprint import pprint
pprint(bad_lines)
lines = [line for line in lines if len(line.strip()) > 0
]
len(lines)
def split_url_line(line):
    url, description = line.split(' | ', maxsplit=1)
    return { description: url }
    
urls = [split_url_line(line) for line in lines]
split_lines = [tuple(line.split(' | ')) for line in lines]
long_lines = [sl for sl in split_lines if len(sl) !=2 ]
len(long_lines)
pprint(long_lines)
help(str.split)
split_lines = [tuple(line.split(' | ')) for line in lines]
long_lines = [sl for sl in split_lines if len(sl) !=2 ]
len(long_lines)
exit()
from pathlib import Path
from pprint import pprint
from urllib.parse import parse_qs, urlsplit, unwrap
from typing import NamedTuple
class DescribedUrl(NamedTuple):
    url: str
    description: str
def split_url_line(line):
    url, description = line.split(' | ', maxsplit=1)
    return DescribedUrl(url, description)
lines = [line.strip() for line in 
         Path('onetab_urls.txt').read_text().splitlines()
         if len(line.strip()) > 0]
urls = [split_url_line(line) for line in lines]
urls[0]
unwrap(urls[0].url)
split_url = urlsplit(urls[0].url)
split_url.scheme
split_urls = [{'description': url.description, 'split_url': urlsplit(url.url)} for url in urls]
chrome_extension_scheme = [url for url in split_urls if url['split_url'].scheme == 'chrome-extension']
len(chrome_extension_scheme)
split_url.query
parse_qs(split_url.query)
for url in chrome_extension_scheme:
    qs = parse_qs(url.query)
    if 'title' in qs:
        print(qs['title'])
    if 'url' in qs:
        print(qs['url'])
        
    
for url in chrome_extension_scheme:
from pathlib import Path
from pprint import pprint
from urllib.parse import parse_qs, urlsplit, unwrap
from typing import NamedTuple
class DescribedUrl(NamedTuple):
    url: str
    description: str
def split_url_line(line):
    url, description = line.split(' | ', maxsplit=1)
    return DescribedUrl(url, description)
lines = [line.strip() for line in 
         Path('onetab_urls.txt').read_text().splitlines()
         if len(line.strip()) > 0]
urls = [split_url_line(line) for line in lines]
urls[0]
unwrap(urls[0].url)
split_url = urlsplit(urls[0].url)
split_url.scheme
split_urls = [{'description': url.description, 'split_url': urlsplit(url.url)} for url in urls]
chrome_extension_scheme = [url for url in split_urls if url['split_url'].scheme == 'chrome-extension']
len(chrome_extension_scheme)
split_url.query
parse_qs(split_url.query)
for url in chrome_extension_scheme:
    qs = parse_qs(url['split_url'].query)
    if 'title' in qs:
        print(qs['title'])
    if 'url' in qs:
        print(qs['url'])
from pathlib import Path
from pprint import pprint
from urllib.parse import parse_qs, urlsplit, unwrap
from typing import NamedTuple
class DescribedUrl(NamedTuple):
    url: str
    description: str
def split_url_line(line):
    url, description = line.split(' | ', maxsplit=1)
    return DescribedUrl(url, description)
lines = [line.strip() for line in 
         Path('onetab_urls.txt').read_text().splitlines()
         if len(line.strip()) > 0]
urls = [split_url_line(line) for line in lines]
urls[0]
unwrap(urls[0].url)
split_url = urlsplit(urls[0].url)
split_url.scheme
split_urls = [{'description': url.description, 'split_url': urlsplit(url.url)} for url in urls]
chrome_extension_scheme = [url for url in split_urls if url['split_url'].scheme == 'chrome-extension']
len(chrome_extension_scheme)
split_url.query
parse_qs(split_url.query)
for url in chrome_extension_scheme:
    qs = parse_qs(url['split_url'].query)
    if 'title' in qs:
        print(qs['title'])
    if 'url' in qs:
        print(qs['url'])
other_urls = [url for url in split_urls
              if url['split_url'].scheme != 'chrome-extension']
other_urls[0]
from urllib.parse import urlunsplit
urlunsplit(other_urls[0]['split_url'])
described_urls = [DescribedUrl(url=urlunsplit(u['split_url']), description=u['description']) for u in other_urls]
descripted_urls[:10]
described_urls[:10]
from functools import partial
with open('urls.md', mode='w') as fp:
    printf = partial(print, file=fp)
    printf('OneTab URL export')
from pathlib import Path
from pprint import pprint
from urllib.parse import parse_qs, urlsplit, unwrap
from typing import NamedTuple
class DescribedUrl(NamedTuple):
    url: str
    description: str
def split_url_line(line):
    url, description = line.split(' | ', maxsplit=1)
    return DescribedUrl(url, description)
lines = [line.strip() for line in 
         Path('onetab_urls.txt').read_text().splitlines()
         if len(line.strip()) > 0]
urls = [split_url_line(line) for line in lines]
urls[0]
unwrap(urls[0].url)
split_url = urlsplit(urls[0].url)
split_url.scheme
split_urls = [{'description': url.description, 'split_url': urlsplit(url.url)} for url in urls]
chrome_extension_scheme = [url for url in split_urls if url['split_url'].scheme == 'chrome-extension']
len(chrome_extension_scheme)
split_url.query
parse_qs(split_url.query)
for url in chrome_extension_scheme:
    qs = parse_qs(url['split_url'].query)
    if 'title' in qs:
        print(qs['title'])
    if 'url' in qs:
        print(qs['url'])
other_urls = [url for url in split_urls
              if url['split_url'].scheme != 'chrome-extension']
other_urls[0]
from urllib.parse import urlunsplit
urlunsplit(other_urls[0]['split_url'])
described_urls = [DescribedUrl(url=urlunsplit(u['split_url']), description=u['description']) for u in other_urls]
descripted_urls[:10]
described_urls[:10]
from functools import partial
with open('urls.md', mode='w') as fp:
    printf = partial(print, file=fp)
    printf('# OneTab URL export')
    printf()
    for du in described_urls:
        printf(f'- [{du.description}]({du.url})')
    
exit()
milliseconds_per_hour = 3600 * 1000
9.5 * milliseconds_per_hour
import pyperclip
int(9.5 * milliseconds_per_hour)
s = int(9.5 * milliseconds_per_hour)
pyperclip.copy(s)
from datetime import datetime, date, time
datetime.now
datetime.now()
from datetime import tzinfo, timezone
from toolz.functoolz import pipe, curry, compose_left
from pathlib import Path
import operator
pipe(datetime.now(), timezone.tzname)
datetime.tzname()
tzinfo.tzname()
tzinfo.tzname
datetime.now()
datetime.now().timestamp()
pipe(datetime.now().timestamp(), int)
get_now = compose_left(datetime.now, operator.methodcaller('timestamp'), int)
get_now()
get_now()
Path.cwd().relative_to(Path('~').expanduser())
exit()
from datetime import *
time()
time.now()
datetime.now()
help(time)
help(datetime)
from datetime import datetime, date, time, timedelta
datetime.time()
datetime.now().hour < 12
datetime.now().today
datetime.now().today()
datetime.today()
datetime.now().date()
datetime.timestamp()
datetime.now().timestamp()
exit()
from datetime import datetime
start_time = datetime.now()
end_day = datetime.today()
end_day
start_time
from datetime import timedelta
tomorrow = datetime.today() + timedelta(days=1)
duration = tomorrow - datetime.now()
duration
end_time = datetime(tomorrow.year, tomorrow.month, tomorrow.day, 9, 30)
end_time
end_time.strftime('%Y-%m-%d %H:%M')
(end_time - datetime.now).seconds * 1000
(end_time - datetime.now()).seconds * 1000
exit()
import pyperclip
from datetime import datetime
from datetime import timedelta
next_day = timedelta(days=1)
start_time = datetime.now()
end_time = datetime(start_time.year, start_time.month, start_time.day + 1, 8, 30)
end_time = datetime(start_time.year, start_time.month, start_time.day + 1, 9, 30)
duration = end_time - start_time
duration
timeout = duration.seconds * 1000
timeout
pyperclip.copy(str(timeout))
exit()
#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path
image_dir = Path('20241004')
def get_date_from_file_name(p: Path) -> datetime:
    return datetime.fromtimestamp(p.stem)
def get_files():
p = next(image_dir.iterdir())
p
get_date_from_file_name(p)
#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path
from toolz.functoolz import pipe
image_dir = Path('20241004')
def get_date_from_file_name(p: Path) -> datetime:
    return pipe(p.stem,
                int,
                datetime.fromtimestamp)
p = next(image_dir.iterdir())
p
get_date_from_file_name(p)
from PIL import image
exit()
#!/usr/bin/env python3
from datetime import datetime
from operator import attrgetter, methodcaller
from pathlib import Path
from typing import Callable
from toolz.functoolz import compose_left, pipe
get_date_from_file_name: Callable[[Path], datetime] = (
    compose_left(
        attrgetter('stem'),
        int,
        datetime.fromtimestamp))
get_image_date_string_from_file_name: Callable[[Path], str] = (
    compose_left(
        get_date_from_file_name,
        methodcaller('strftime', '%Y-%m-%d %H:%M:%S')))
image_dir = Path('20241004')
p = next(image_dir.iterdir())
image_date_string = get_image_date_string_from_file_name(p)
print(image_date_string)
### 
help(Image)
from PIL import Image
help(Image)
import inspect
members = inspect.getmembers(Image)
len(members)
members[0]
members[20]
members[100]
static_functions = inspect.getmembers_static(predicate=inspect.isfunction)
static_functions = inspect.getmembers_static(Image, predicate=inspect.isfunction)
len(static_functions)
static_functions[0]
public_static_functions = [(name, value) for name, value in static_functions if not name.startswith('_')]
len(public_static_functions)
public_static_function_names = sorted(name for name, _ in public_static_functions)
for name in public_static_function_names:
    print(name, end=' ')
    
from PIL import ImageDraw, ImageFont
exit()
exit(0
)
def test() -> (int, int):
    return (4, 3)
test()
exit()
import ImageColor
from PIL import ImageColor
help(ImageColor)
import inspect
constants = inspect.getmembers_static(predicate=inspect.iskeyword)
constants = inspect.getmembers_static(ImageColor, predicate=inspect.iskeyword)
constants = inspect.getmembers(ImageColor, predicate=inspect.iskeyword)
 members = inspect.getmembers(ImageColor)
members = inspect.getmembers(ImageColor)
from pprint import pprint
import regex
len(members)
for m in members:
    print(m)
    
ImageColor.getcolor('white', mode='RGBA')
exit()
import time
for s in 'the quick brown fox jumped over the lazy dog'.split():
    print(s, end='\r')
    time.sleep(0.5)
    
import time
for s in 'the quick brown fox jumped over the lazy dog'.split():
from sys import stdout
for s in 'the quick brown fox jumped over the lazy dog'.split():
    print(f'\r{s}', end='')
    stdout.flush()
from datetime import datetime
datetime(2024, 10, 04, 1, 59, 31)
datetime(2024, 10, 4, 1, 59, 31)
datetime(2024, 10, 4, 1, 59, 31).timestamp()
from pathlib import Path
print(str(Path.cwd()))
import pyperclip
ts = int(datetime(2024, 10, 4, 1, 59, 31).timestamp())
ts
import pyperclip
pyperclip.copy(str(ts))
help(datetime.timestamp)
datetime.now().timestamp()
datetime.now() - datetime.fromtimestamp(ts)
import timezone
datetime.fromtimestamp(ts)
files = sorted(p for p in Path('20241004').iterdir(), key=lambda p:int(p.stem))
files = sorted((p for p in Path('20241004').iterdir()), key=lambda p:int(p.stem))
files[0]
file_stems = [p.stem for p in files]
timestamps = [int(s) for s in file_stems]
datetime.fromtimestamp(timestamps[0]).strftime('%Y-%m-%d %H:%M:%S')
dt = '2024-10-05 01:59:31'.strptime('%Y-%m-%d %H:%M:%S') 
dt = datetime.strptime('2024-10-05 01:59:31','%Y-%m-%d %H:%M:%S') 
dt
datetime.timestamp()
dt.timestamp()
timestamps.find(int(dt.timestamp()))
timestamps.index(int(dt.timestamp()))
2305/30
datetime(2024, 10, 5, 5, 13, 18).timestamp
datetime(2024, 10, 5, 5, 13, 18).timestamp()
ts2 = datetime(2024, 10, 5, 5, 13, 18).timestamp()
ts2 = int(ts2)
ttimestamps.index(ts2)
timestamps.index(ts2)
4623/30
154.1 - 76.833
