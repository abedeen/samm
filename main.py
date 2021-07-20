import os
import json
file=1
ar={"kk0":'برمجة تطبيقات الاندرويد والايفون'}
eng={"kk0":'Programming Android and iPhone applications'}
kcount={'count':1,'file':1}
def getCount():
    s = kcount['count'] +1
    kcount['count']=s
    return kcount['count']
def nextFile():
    s = kcount['file'] +1
    kcount['file'] =s
    return str(kcount['file'])
def generate(txt, navs):
    nav_main = "<ul>\n @@@ITEM@@@</ul>"
    #nav_drop = ""<li class=\"dropdown\"><a  class=\"menuAnchor\" href=\"\" ><span   data-langkey=\"hosting\">@@@LINK@@@</span> <i class=\"bi bi-chevron-down\"></i></a>\n@@@SUBLINK@@@\n\t</li>"
    #nav_drop = "<li class=\"@@@current@@@ dropdown\"><a class=\"menuAnchor\" href=\"#\">@@@LINK@@@</a>@@@SUBLINK@@@\n</li>"
    nav_drop = "<li class=\"dropdown\"><a href=\"#\"><span data-langkey=\"@@@LINK@@@\"></span> <i class=\"bi bi-chevron-down\"></i></a>@@@SUBLINK@@@\n</li>"
    #nav_link = "<li class=\"@@@current@@@ \"><a class=\"menuAnchor nav-link scrollto\" href=\"/@@@LINK@@@.html\">@@@LINK@@@</a></li>"
    nav_link = "<li><a class=\"nav-link scrollto @@@LINK2@@@-active@\"  href=\"@@@LINK2@@@.html\" data-langkey=\"@@@LINK@@@\"></a></li>"
    str=""
    for k in navs:
         print(txt)
         if len(k)>0:
             linkstr = updateLang(k)
             if checkIsDropDown(k[0]):
                 undder_str=generate(k[0],data[k[0]])
                 if len(undder_str)>0:
                     undder_str = "<ul>"+undder_str+"</ul>"
                 str= str+ nav_drop.replace('@@@LINK@@@',linkstr).replace('@@@SUBLINK@@@',undder_str)+"\t"
             else :
                 str= str+ nav_link.replace('@@@LINK@@@',linkstr).replace("@@@LINK2@@@",nextFile())+"\n"

    return str
def generate(txt, navs):
    nav_main = "<ul>\n @@@ITEM@@@</ul>"
    #nav_drop = ""<li class=\"dropdown\"><a  class=\"menuAnchor\" href=\"\" ><span   data-langkey=\"hosting\">@@@LINK@@@</span> <i class=\"bi bi-chevron-down\"></i></a>\n@@@SUBLINK@@@\n\t</li>"
    #nav_drop = "<li class=\"@@@current@@@ dropdown\"><a class=\"menuAnchor\" href=\"#\">@@@LINK@@@</a>@@@SUBLINK@@@\n</li>"
    nav_drop = "<li class=\"dropdown\"><a href=\"#\"><span data-langkey=\"@@@LINK@@@\"></span> <i class=\"bi bi-chevron-down\"></i></a>@@@SUBLINK@@@\n</li>"
    #nav_link = "<li class=\"@@@current@@@ \"><a class=\"menuAnchor nav-link scrollto\" href=\"/@@@LINK@@@.html\">@@@LINK@@@</a></li>"
    nav_link = "<li><a class=\"nav-link scrollto @@@LINK2@@@-active@\"  href=\"@@@LINK2@@@.html\" data-langkey=\"@@@LINK@@@\"></a></li>"
    str=""
    for k in navs:
         print(txt)
         if len(k)>0:
             linkstr = updateLang(k)
             if checkIsDropDown(k[0]):
                 undder_str=generate(k[0],data[k[0]])
                 if len(undder_str)>0:
                     undder_str = "<ul>"+undder_str+"</ul>"
                 str= str+ nav_drop.replace('@@@LINK@@@',linkstr).replace('@@@SUBLINK@@@',undder_str)+"\t"
             else :
                 str= str+ nav_link.replace('@@@LINK@@@',linkstr).replace("@@@LINK2@@@",nextFile())+"\n"

    return str
main_txt ={'index':"kk0",'0':'kk1','1':'kk2'}
def generate(txt, navs):
    nav_main = "<ul>\n @@@ITEM@@@</ul>"
    #nav_drop = ""<li class=\"dropdown\"><a  class=\"menuAnchor\" href=\"\" ><span   data-langkey=\"hosting\">@@@LINK@@@</span> <i class=\"bi bi-chevron-down\"></i></a>\n@@@SUBLINK@@@\n\t</li>"
    #nav_drop = "<li class=\"@@@current@@@ dropdown\"><a class=\"menuAnchor\" href=\"#\">@@@LINK@@@</a>@@@SUBLINK@@@\n</li>"
    nav_drop = "<li class=\"dropdown\"><a href=\"#\"><span data-langkey=\"@@@LINK@@@\"></span> <i class=\"bi bi-chevron-down\"></i></a>@@@SUBLINK@@@\n</li>"
    #nav_link = "<li class=\"@@@current@@@ \"><a class=\"menuAnchor nav-link scrollto\" href=\"/@@@LINK@@@.html\">@@@LINK@@@</a></li>"
    nav_link = "<li><a class=\"nav-link scrollto @@@LINK2@@@-active@\"  href=\"@@@LINK2@@@.html\" data-langkey=\"@@@LINK@@@\"></a></li>"
    str=""
    for k in navs:
         print(txt)
         if len(k)>0:
             linkstr = updateLang(k)
             if checkIsDropDown(k[0]):
                 undder_str=generate(k[0],data[k[0]])
                 if len(undder_str)>0:
                     undder_str = "<ul>"+undder_str+"</ul>"
                 str= str+ nav_drop.replace('@@@LINK@@@',linkstr).replace('@@@SUBLINK@@@',undder_str)+"\t"
             else :
                 sss = nextFile()
                 main_txt[sss] = linkstr
                 str= str+ nav_link.replace('@@@LINK@@@',linkstr).replace("@@@LINK2@@@",sss)+"\n"

    return str
def readFile(fname):
    with open(fname, 'r') as file:
        data = file.read()
        return data
def generateFiles(olist):
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    menu = readFile(os.path.abspath(os.getcwd())+'/nav.html')
    ifile =os.path.abspath(os.getcwd())+'/index';
    print(main_txt)
    for f in olist:
        if f!='copyHeader.py':
            tfile =os.path.abspath(os.getcwd())+'/'+f;
            txt = readFile(ifile)
            print(f);
            txt =txt.replace("@@FILE1@@",main_txt[f])
            if '@@@MENU@@@' in txt:
                stext = txt.replace('@@@MENU@@@', menu).replace(f+"-active@","active")
                file1 = open(tfile+".html","w")
                file1.write(stext)
                file1.close()
def updateLang(obj):
    c = getCount()
    b = "kk"+str(c)
    eng[b]=obj[0];
    ar[b]=obj[1];
    return b
def readFile(fname):
    with open(fname, 'r') as file:
        data = file.read()
        return data
def checkIsDropDown(obj):
    try:
        s = len(data[obj])
        if s > 0 :
            return True
    except:
        return False
files = [f for f in os.listdir('.') if os.path.isfile(f)]
main = readFile(os.path.abspath(os.getcwd())+'/index')

data ={
'index' :[['main',' بيتي'],['host','استضافة'],['VPS','فى بى اس'],['Servers','سيرفرات'],['Ranges','نطاقات'],['Services','نطاقات'],['About Company','عن الشركة'],['contact','اتصل بنا']],
"main":[['sign in','تسجيل الدخول'],['subscriptions','الاشتراك'],['contact watsapp','تواصل واتس']],
"host":[['web hosting','استضافة المواقع'],['hosting reseller','استضافة ريسلرات']],
"VPS":[['VPS linux','في بي اس لينكس'],['VPS windows','في بي اس ويندوز'],['VPS matin2','في بي اس ماتين 2']],
"servers":[['introductory full servers','سيرفرات كاملة تمهيدية'],['economic full servers','سيرفرات كاملة اقتصادية'],['complete servers for enterprises','سيرفرات كاملة للمؤسسات'],['complete professional servers','سيرفرات كاملة للمحترفين'],['gaming servers','سيرفرات للألعاب'],['storage servers','سيرفرات للتخزين']],
"services":[['web design','تصميم مواقع الانترنت'],['website programming','برمجة مواقع الانترنت'],['smart application programming','برمجة التطبيقات الذكية'],['SSL security certificates','شهادات الأمان SSL'],['wordpress technical support','دعم فني وردبرس']],
"about company":[[]],
"call us":[[]]
}


file1 = open(os.path.abspath(os.getcwd())+"/nav.html","w")
file1.write("<nav id=\"navbar\" class=\"navbar\"><ul>"+generate('index',data['index'])+"<li><a class=\"nav-link scrollto\"><input id=\"languageTxt\" type=\"checkbox\"  onclick=\"updateValue(this)\"  data-on=\"Arabic\" data-off=\"English\" data-onstyle=\"success\" data-offstyle=\"danger\" checked data-toggle=\"toggle\"></li></ul></nav>")

file1.close()
print("total files :"+str(kcount))
with open("/home/abed/samm/assets/i18n/english.json", "w") as outfile:
    outfile.write(json.dumps(eng, indent = 4))
with open("/home/abed/samm/assets/i18n/arabic.json", "w") as outfile:
    outfile.write(json.dumps(ar, indent = 4))
vfile=['index']
for i in range(kcount['file']):
    vfile.append(str(i)+"")
#print(vfile)
generateFiles(vfile)
print(main_txt)
'''
for f in files:
    if f!=:
        tfile =os.path.abspath(os.getcwd())+'/'+f;
        txt = readFile(tfile)
        if '@@@MENU@@@' in txt:
            stext = txt.replace('@@@MENU@@@', menu)
            file1 = open(tfile+".html","w")
            file1.write(stext)
            file1.close()
'''
