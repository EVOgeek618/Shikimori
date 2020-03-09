import urllib.request, string
class Wiki():
    def __init__(self,lines):
        self.lines=lines
    def search(self):
        for line in self.lines:
            a = line.index('#')
            b = line.index('"><span')
            c = line.index('toclevel-')
            d = line.index('tocnumber">')
            e = line.index('</span>')
            for q in range(int(line[c + len('toclevel-')]) - 1):
                print('\t', end='')
            for j in range(d + len('tocnumber">'), e):
                print(line[j], end='')
            print(' ', end='')
            for i in range(a + 1, b):
                if line[i] != '_':
                    print(line[i], end='')
                else:
                    print(' ', end='')
            print('\t')
    def glos(self):
        glosarik={}
        for line in self.lines:
                str=[]
                glava=[]
                a = line.index('#')
                b = line.index('"><span')
                d = line.index('tocnumber">')
                e = line.index('</span>')
                for j in range(d + len('tocnumber">'), e):
                    str.append(line[j])
                num=''.join(str)
                for i in range(a + 1, b):
                    if line[i] != '_':
                        glava.append(line[i])
                    else:
                        glava.append(' ')
                zag=''.join(glava)
                glosarik[num]=zag
        return glosarik
    def Wikipedia(self,glosarik):
        st = input('Введите номера нужных глав(через пробел):\n')
        glavs = st.split(' ')
        zam = {'&#91;': '<', '&#93;': '>', '&#160;': '', '&#32;': '', '&#34': '"', '&#39': '\''}
        with open('C:\\Users\\' + name + '\Desktop\WIKIPEDIA.doc', 'w') as print:
            for i in glavs:
                glava = glosarik[i]
                print.write(glava)
                print.write('\n')
                ku = len(lines2)
                for j in range(len(lines2)):
                    if lines2[j].find('h' + str(int((len(i) + 1) / 2) + 1)) != -1 and lines2[j].find(glava) != -1:
                        ku = j
                    elif lines2[j].find('<h') != -1 and lines2[j].find(glava) == -1 and j > ku and int(
                            lines2[j][lines2[j].find('<h') + 2]) <= int((len(i) + 1) / 2) + 1:
                        ki = j
                        break
                for k in range(ku + 1, ki):
                    sec = lines2[k][:]
                    for key in zam:
                        sec = sec.replace(key, zam[key])
                    sec = sec.split('<')
                    sec = '*DELETE'.join(sec)
                    sec = sec.split('>')
                    sec = '*'.join(sec)
                    sec = sec.split('*')

                    for i in sec:
                        if i.find('DELETE') != -1:
                            sec.remove(i)
                    sec = ''.join(sec)
                    sec = sec.split('\n')
                    sec = ''.join(sec)
                    if sec.find('[править | править код]'):
                        print.write('\n\t')
                        sec = sec.replace('[править | править код]', '\n')
                    if sec.find('[en]'):
                        print.write('\n\t')
                        sec = sec.replace('[en]', '')
                    try:
                        print.write(sec)
                    except:
                        for buk in sec:
                            try:
                                print.write(buk)
                            except:
                                continue
                print.write('\n\n\n')


import urllib, string
import time
strih=string.ascii_letters
strih+='_'
try:
    with open('name.txt','r') as comp:
        name=comp.readline()
except FileNotFoundError:
    name=input('Введите название компьютера(Нужно для вывода на рабочий стол):  ')
    with open('name.txt','w') as comp:
        comp.write(name)
pages=[]
notpages=[]
listofanime={}
wer=0
for c in range(1,251):
  try:
    link=urllib.request.urlopen('https://shikimori.one/animes/kind/!music/status/!anons/order-by/popularity/page/'+str(c))
    lines = []
    for line in link.readlines():
            lines.append(line)
    link.close()
    for i in range(len(lines)):
            lines[i] = lines[i].decode('utf-8')
    fg=0
    for h in range(5, len(lines)):
        if lines[h].find("data-tooltip_url=") != -1:
            ng2 = lines[h]
    for f in range(20):
        doc1=[]
        wer=wer+1
        gt=fg
        fg=ng2.find("data-tooltip_url=",fg)+len("data-tooltip_url=")+1
        fg1=ng2.find("href=\"",fg)+len("href=\"")
        fg2=ng2.find("\"",fg1)
        try:
            link = urllib.request.urlopen(ng2[fg1:fg2])
        except ValueError:
           try:
            link = urllib.request.urlopen(ng2[fg:ng2.find("/tooltip",fg)])
           except urllib.error.HTTPError:
               for i in range(1, 61):
                   print("\r" + str(i), end='')
                   time.sleep(1)
               print("\r", end='')
               fg=gt
               wer=wer-1
               f=f-1
               continue
        except urllib.error.HTTPError:
            for i in range(1, 61):
                print("\r" + str(i), end='')
                time.sleep(1)
            print("\r",end='')
            fg=gt
            wer=wer-1
            f = f-1
            continue
        lines1 = []
        for line in link.readlines():
            lines1.append(line)
        link.close()
        for i in range(len(lines1)):
            lines1[i] = lines1[i].decode('utf-8')
        for h in range(5, len(lines1)):
            if lines1[h].find("Все отзывы") != -1:
                doc1 = str(lines1[h]).split('>')
                break
        if doc1==[]:
            print(wer)
            continue
        for i in range(len(doc1)):
            if doc1[i].find("Все отзывы<span class=") != -1:
                num=i+1
            if doc1[i].find("Все комментарии<span class=") != -1:
                num1=i+1
        for h in range(5, len(lines1)):
            if lines1[h].find("Просмотрено&quot;,&quot;value&quot;") != -1:
                doc = str(lines1[h]).split('>')
                break

        try:
            if doc1[num]=='</header':
                continue
        except IndexError:
            continue
        doc[36]=doc[36].replace("&quot;","'")
        prosm=(doc[36][doc[36].find("Просмотрено','value':")+len("Просмотрено','value':"):doc[36].find('}',doc[36].find("Просмотрено','value':"))])
        brosh=(doc[36][doc[36].find("Брошено','value':")+len("Брошено','value':"):doc[36].find('}',doc[36].find("Брошено','value':"))])
        otloz=(doc[36][doc[36].find("Отложено','value':")+len("Отложено','value':"):doc[36].find('}',doc[36].find("Отложено','value':"))])
        zaplo=(doc[36][doc[36].find("Запланировано','value':")+len("Запланировано','value':"):doc[36].find('}',doc[36].find("Запланировано','value':"))])
        smotr=(doc[36][doc[36].find("Смотрю','value':")+len("Смотрю','value':"):doc[36].find('}',doc[36].find("Смотрю','value':"))])
        try:
            summ=int(prosm)+int(brosh)+int(otloz)+int(zaplo)+int(smotr)
            if summ < 3000 or (int(doc1[num].replace('</span',''))<15 and int(doc1[num1].replace('</span',''))<400):
                print(wer,ng2[ng2.find("/animes/",fg1)+len("/animes/"):fg2],doc1[num],"-"*150)
                continue
            listofanime.setdefault(ng2[ng2.find("/animes/",fg1)+len("/animes/"):fg2],(summ,int(doc1[num].replace('</span',''))/int(summ)*10000,doc1[num].replace('</span',''),int(doc1[num1].replace('</span',''))/int(summ)*100,doc1[num1].replace('</span','')))
        except (ValueError):
            continue
        print(wer,ng2[ng2.find("/animes/",fg1)+len("/animes/"):fg2],' | ',summ,"|",int(doc1[num].replace('</span',''))/int(summ)*10000,' | ',doc1[num].replace('</span',''),' | ',int(doc1[num1].replace('</span',''))/int(summ)*100,' | ',doc1[num1].replace('</span',''))
  except urllib.error.HTTPError:
      for i in range(1, 61):
          print("\r" + str(i), end='')
          time.sleep(1)
      c = c - 1
      continue
list_d = list(listofanime.items())
for i in list_d:
    print(i)
list_d.sort(key=lambda i: i[1][0])
n=0
with open('List of popular anime 2020_1_2.txt','w') as comp:
    for i in list_d[::-1]:
        n=n+1
        comp.write(str(n)+"-"+str(i[0])+". "+str(i[1][0])+' | '+str(i[1][1])+' | '+str(i[1][2])+' | '+str(i[1][3])+' | '+str(i[1][4])+"\n")

