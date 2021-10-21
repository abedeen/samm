import os
def readFile(fname):
    with open(fname, 'r') as file:
        data = file.read()
        return data

def generateFiles():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    #menu = readFile(os.path.abspath(os.getcwd())+'/footer')
    #ifile =os.path.abspath(os.getcwd())+'/'+f+".html";

    for f in files:
        if f.endswith(".html"):
            tfile =os.path.abspath(os.getcwd())+'/'+f;
            txt = readFile(tfile)
            stext = txt.replace('BoutrosNewsH1 Bold!important;','Cordoba')
            print(tfile)
            file1 = open(tfile,"w")
            file1.write(stext)
            file1.close()
'''
            stext1 = txt.split('<!-- ======= Footer ======= -->')
            stext2 = txt.split('<!-- End Footer -->')
            print(f+"<><>"+str(len(stext1))+"<><>"+str(len(stext2)))
            stext =stext1[0]+menu+stext2[1]
            print(tfile)
            '''

generateFiles()
