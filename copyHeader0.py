import os
def readFile(fname):
    with open(fname, 'r') as file:
        data = file.read()
        return data
def generateFiles(olist):
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    menu = readFile(os.path.abspath(os.getcwd())+'/footer')
    #ifile =os.path.abspath(os.getcwd())+'/'+f+".html";

    for f in olist:
        if f!='copyHeader.py':
            tfile =os.path.abspath(os.getcwd())+'/'+f+".html";
            txt = readFile(tfile)

            stext1 = txt.split('<!-- ======= Footer ======= -->')
            stext2 = txt.split('<!-- End Footer -->')
            print(f+"<><>"+str(len(stext1))+"<><>"+str(len(stext2)))
            stext =stext1[0]+menu+stext2[1]
            print(tfile)
            file1 = open(tfile,"w")
            file1.write(stext)
            file1.close()
list = ['index']
for i in range(13):

    list.append(str(i))
generateFiles(list)
