class Anime():
    def __init__(self,string):
        self.lists=string[string.index('. ')+2:len(string)-1].split(" | ")[0]
        self.name=string[string.index('-')+1:string.index('. ')]
        self.kreviews = string[string.index('. ') + 2:len(string) - 1].split(" | ")[1]
        self.reviews = string[string.index('. ') + 2:len(string) - 1].split(" | ")[2]
        self.kcomments = string[string.index('. ') + 2:len(string) - 1].split(" | ")[3]
        self.comments = string[string.index('. ') + 2:len(string) - 1].split(" | ")[4]
        if self.name[:self.name.find("-")].isdigit():
            self.id = self.name[:self.name.find("-")]
        else:
            self.id = self.name[1:self.name.find("-")]
    def __str__(self):
        return "{},{},{},{},{},{}\n".format(self.lists,self.name,self.comments,self.kcomments,self.reviews,self.kreviews)


def ToString(id,group,text,name,number,pastnumber):
    return '"linked_id":{id},"group":"{group}","text":"{number}\\r\\n{text}\\r\\n{pastnumber}","name":"","url":"/animes/{name}"'.format\
        (id=id, group=group, number=number, text=text, pastnumber=pastnumber, name=name)

def PastNumber(list1,list2):
    pastAnime={}
    presentAnime={}
    for i in range(len(list1)):
        w = list1[i].id
        pastAnime[w]=i
    for j in range(len(list2)):
        g = list2[j].id
        try:
            presentAnime[g]=pastAnime[g]-j
            if str(presentAnime[g])[0]!="-" and str(presentAnime[g])[0]!="0":
                presentAnime[g] = "+"+str(pastAnime[g] - j)
        except KeyError:
            presentAnime[g]="Новое в списке"
    return presentAnime
def group_num(k,f=None):
    if f == None:
        if k<=10:
            return "1-10"
        elif 10<k<41:
            return "11-40"
        elif 40<k<81:
            return "41-80"
        elif 80<k<121:
            return "81-120"
        elif 120<k<161:
            return "121-160"
        else:
            return "121-200"
    else:
        if k<=10:
            return f"{f} 1-10"
        elif 10<k<31:
            return f"{f} 11-30"
        elif 30<k<61:
            return f"{f} 31-60"
        else:
            return f"{f} 61-100"
def sort_list_to_json(link1,link2,string="",string2=""):
    s = ''
    k = 0
    link2.sort(key=lambda i: int(sor))
    link1.sort(key=lambda i: int(sor))
    link2, link1 = link2[::-1], link1[::-1]
    num = PastNumber(link1, link2)
    print(list((j.name for j in link2)))
    for i in link2[:100]:
        k += 1
        gr = group_num(k, string)
        pastnumber = num[i.id]
        d = ToString(i.id, gr, "{} {}".format(string2,sor), i.name, k, pastnumber)
        s += "{" + d + "},"
    print(s)
    return s
link1=[]
link2=[]
with open('List of animes 1.txt','r') as comp:
    for i in comp.readlines():
        f=Anime(i)
        link1.append(f)
with open('List of popular anime 2020_1_2.txt','r') as comp:
    for i in comp.readlines():
        f = Anime(i)
        link2.append(f)
sort_list_to_json(link1,link2)
sort_list_to_json(link1,link2)
sort_list_to_json(link1,link2)
sort_list_to_json(link1,link2)
sort_list_to_json(link1,link2)
s=''
k=0
link2.sort(key=lambda i: int(i.comments))
link1.sort(key=lambda i: int(i.comments))
link2, link1 = link2[::-1], link1[::-1]
num = PastNumber(link1, link2)
print(list((j.name for j in link2)))
for i in link2[:100]:
    k+=1
    gr=group_num(k,"САМОЕ БОЛЬШОЕ КОЛИЧЕСТВО КОММЕНТАРИЕВ")
    pastnumber=num[i.id]
    d=ToString(i.id,gr,"{} комментариев".format(i.comments),i.name,k,pastnumber)
    s+="{"+d+"},"
print(s)
s=""
k=0
link2.sort(key=lambda i: float(i.kcomments))
link1.sort(key=lambda i: float(i.kcomments))
link2, link1 = link2[::-1], link1[::-1]
num = PastNumber(link1, link2)
print(list((j.name for j in link2)))
for i in link2[:100]:
    k+=1
    gr=group_num(k,"САМЫЕ 'КОММЕНТИРУЕМЫЕ' АНИМЕ С УЧЕТОМ ПОПУЛЯРНОСТИ")
    pastnumber=num[i.id]
    d=ToString(i.id,gr,"{}".format(i.kcomments),i.name,k,pastnumber)
    s+="{"+d+"},"
print(s)
s=""
k=0
link2.sort(key=lambda i: float(i.reviews))
link1.sort(key=lambda i: float(i.reviews))
link2, link1 = link2[::-1], link1[::-1]
num = PastNumber(link1, link2)
print(list((j.name for j in link2)))
for i in link2[:100]:
    k+=1
    gr=group_num(k,"САМОЕ БОЛЬШОЕ КОЛИЧЕСТВО ОТЗЫВОВ")
    pastnumber=num[i.id]
    d=ToString(i.id,gr,"{} отзывов".format(i.reviews),i.name,k,pastnumber)
    s+="{"+d+"},"
print(s)
s=""
k=0
link2.sort(key=lambda i: float(i.kreviews))
link1.sort(key=lambda i: float(i.kreviews))
link2, link1 = link2[::-1], link1[::-1]
num = PastNumber(link1, link2)
print(list((j.name for j in link2)))
for i in link2[:100]:
    k+=1
    gr=group_num(k,"САМЫЕ 'ОБОЗРЕВАЕМЫЕ' АНИМЕ С УЧЕТОМ ПОПУЛЯРНОСТИ")
    pastnumber=num[i.id]
    d=ToString(i.id,gr,"{}".format(i.reviews),i.name,k,pastnumber)
    s+="{"+d+"},"
print(s)