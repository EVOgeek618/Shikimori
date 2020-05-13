import urllib.request, string
import urllib, string
import time
def API(st):
    st=st[:len('https://shikimori.one')]+'/api'+st[len('https://shikimori.one'):]
    return st
pages=[]
notpages=[]
listofanime={}
wer=0
for c in range(1,2426):
  try:
    link=urllib.request.urlopen('https://shikimori.one/characters/page/'+str(c))
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
    for f in range(48):
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
            if lines1[h].find("Комментарии<div class=") != -1:
                doc1 = str(lines1[h]).split('>')
                break
        if doc1==[]:
            print(wer,end=' ')
            continue
        for i in range(len(doc1)):
            if doc1[i].find("Комментарии<div class=") != -1:
                num1=i+1
        try:
            if int(doc1[num1].replace('</div','')) >=200:
                listofanime.setdefault(ng2[ng2.find("/characters/",fg1)+len("/characters/"):fg2],doc1[num1].replace('</div',''))
                print('\n',wer, ng2[ng2.find("/characters/", fg1) + len("/characters/"):fg2], ' | ',doc1[num1].replace('</div', ''))
                list_d = list(listofanime.items())
                list_d.sort(key=lambda i: i[1])
                for i in range(len(list_d)):
                    list_d[i] = list(list_d[i])
                    list_d[i][0] = list_d[i][0].split('-')
                    list_d[i][0][1] = ' '.join(list_d[i][0][1:])
                    list_d[i][0] = list_d[i][0][0:2]
                with open('List of popular ch.txt', 'w') as comp:
                        for i in list_d[::-1]:
                            comp.write("[character=" + str(i[0][0]) + ']' + str(i[0][1]).title() + '[/character] ' + str(i[1]) + "\n")
            else:
                print("\r" + str(wer), end='')
        except (ValueError):
            continue
  except urllib.error.HTTPError:
      for i in range(1, 61):
          print("\r" + str(i), end='')
          time.sleep(1)
      c = c - 1
      continue
list_d = list(listofanime.items())
list_d.sort(key=lambda i: i[1])
for i in range(len(list_d)):
    list_d[i]=list(list_d[i])
    list_d[i][0]=list_d[i][0].split('-')
    list_d[i][0][1]=' '.join(list_d[i][0][1:])
    list_d[i][0]=list_d[i][0][0:2]
for i in range(len(list_d)):
    print(list_d[i])
n=0
with open('List of popular char 2020_2.txt','w') as comp:
    for i in list_d[::-1]:
        n=n+1
        comp.write("[character="+str(i[0][0])+']'+str(i[0][1]).title()+'[/character] '+str(i[1])+"\n")

