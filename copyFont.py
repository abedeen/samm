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
            stext = txt.replace('https://fonts.gstatic.com/l/font?kit=hESw6XVnNCxEvkbMow9Xb67-3VEDY0kkYiNvfCWeLAXRLdLPBZvWIGysxcdRt17B4wViu9Bh2N80LAA8WwSFpjWVOEZ-YT1wqpymRA5QPgxVK3pAUKlHglhYhz7F_Ftq4PxtlzOAPSy_VFwuTyVTuM81VubQgv3c5wVaJJa0kDVzqqv5WcxwJ7p4qhmenOFjbLhXTG7YsBYwExmjIlQKpAvHahfabHxbem3vbQb-MfIbDNEXaDk6zvewEYbkykzxPLFs6WbYLqz75pDObDKfQ-rWvK0wT64gnyVDnx5KICXxXzOukW70&skey=c6edfa7a4a5da33&v=v18','https://fonts.gstatic.com/l/font?kit=WwkbxPW1E165rajQKDulEIU6cPIWBHYivgBpqLigmdK_tgiHKVombYoHTz_FHzjXJw3D&skey=42031ebbc54bfc32&v=v16')
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
