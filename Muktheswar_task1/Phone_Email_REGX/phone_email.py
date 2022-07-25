import pyperclip,re
def extractor(text,filename):
    phoneregex=re.compile(r'''((\d{3}|\(\d{3}\))?
                           (\s|-|\.)?
                           (\d{3})
                           (\s|-|\.)
                           (\d{4})
                           (\s*(ext|x|ext.)\s*(\d{2,5}))?
                           )''',re.VERBOSE)

    emailregex=re.compile(r'''([a-zA-Z0-9._%+-]+
                        @
                        [a-zA-Z0-9.-]+
                        (\.[a-zA-Z]{2,4})
                        )''',re.VERBOSE)


    matches_phone = []
    for groups in phoneregex.findall(text):
        phone = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
         phone += ' x' + groups[8]
        matches_phone.append(phone)

    matches_email=[]
    for groups in emailregex.findall(text):
        matches_email.append(groups[0])

    if len(matches_phone) > 0:
        print("\n\nAll phone numbers in the file := " + filename +" are  :")
        print('\n'.join(matches_phone))
    if len(matches_email) > 0:
        print("\n\nAll Email in the file := " + filename +" are  :")
        print('\n'.join(matches_email))
