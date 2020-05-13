import urllib.request, string
import time
dic={}
n=input()
r=input().split(' ')
for li in range(int(n)):
    #link=urllib.request.urlopen("https://shikimori.one/people/"+r[li]+"/roles") #Люди
    link = urllib.request.urlopen("https://shikimori.one/animes/" + r[li] + "/characters") #Аниме
    #link = urllib.request.urlopen("https://shikimori.one/mangas/" + r[li] + "/characters") #Манга
    list2 = []
    for line in link.readlines():
        list2.append(line)
    link.close()
    for i in range(len(list2)):
        list2[i] = list2[i].decode('utf-8')
    ng=list2[len(list2)-5]
    while (ng):
      try:
        gt = i
        i = ng.find("<a class=\"cover anime-tooltip\" data-delay=\"150\" data-tooltip_url=\"https://shikimori.one/characters/", i) + len("<a class=\"cover anime-tooltip\" data-delay=\"150\" data-tooltip_url=\"https://shikimori.one/characters/")
        c = ng.find("/tooltip\"", i)
        link1 = urllib.request.urlopen("https://shikimori.one/characters/"+ng[i:c])
        list1 = []
        for line in link1.readlines():
            list1.append(line)
        link1.close()
        for j in range(len(list1)):
            list1[j] = list1[j].decode('utf-8')
        #doc=list1
        #for h in doc:
         #   print(h)
        ng1="0"
        ng2="0"
        for h in range(5, len(list1)):
            if list1[h].find("</script></head><body") != -1:
                ng2 = list1[h]
            elif list1[h].find(">В избранном") != -1:
                ng1 = list1[h]
        i1=0
        i2=0
        i3 = 0
        ret=set()
        i1 = ng2.find("<h1>",i1) + len("<h1>")
        c1 = ng2.find("<", i1)
        print(ng2[i1:c1])
        dic.setdefault(ng2[i1:c1], 0)
        dt="0"
        i2 = ng1.find(">В избранном<div class=\"count\">", i2) + len(">В избранном<div class=\"count\">")
        c2 = ng1.find("<", i2)
        dt=ng1[i2:c2]
        if dt=="ass=\"preview\">":
            for ki in range(12):
                i3=ng1.find("b-user c-column avatar",i3)+1
                ret.add(i3)
            dt=len(ret)-1
        elif dt=="":
            del dic[ng2[i1:c1]]
            continue
        dic[ng2[i1:c1]]=int(dt)
      except(UnicodeEncodeError):
            break
      except Exception as e:
          i=gt
          continue

list_d = list(dic.items())
list_d.sort(key=lambda i: i[1])
list_d=list_d[::-1]
for i in list_d:
    print(i[0], ':', i[1])
'''

#<a class="" href="https://shikimori.one/characters/50691-hidenori-tabata/favoured">В избранном<div class=\"count\">112</div></a>
            #<a class=\"cover anime-tooltip\" data-delay=\"150\" data-tooltip_url=\"https://shikimori.one/characters/'''
