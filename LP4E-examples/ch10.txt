#################################################################
# NOTE: at this point in the code extraction process, I changed
# from using the published draft's PDF, to the Word doc files of
# the final draft I submitted to O'Reilly, in order to avoid
# losing the original whitespace.  PDF cut-and-paste doesn't
# keep spaces (at least as created), and the 30-minute web 
# search didn't turn up many good options (though pyPdf and 
# ReportLab's PageCatcher look like good leads).  Some tweaking
# was done to the book after the final draft, so if the code in
# remaining chapters' files is slightly out of synch with book,
# you'll want to edit the code manually.
#################################################################




while True:
    reply = input('Enter text:')
    if reply == 'stop': break
    print(reply.upper())



>>> reply = '20'
>>> reply ** 2
...error text omitted...

>>> int(reply) ** 2
400



while True:
    reply = input('Enter text:')
    if reply == 'stop': break
    print(int(reply) ** 2)
print('Bye')



>>> S = '123'
>>> T = 'xxx'
>>> S.isdigit(), T.isdigit()
(True, False)



while True:
    reply = input('Enter text:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        print(int(reply) ** 2)
print('Bye')



while True:
    reply = input('Enter text:')
    if reply == 'stop': break
    try:
        num = int(reply)
    except:
        print('Bad!' * 8)
    else:
        print(int(reply) ** 2)
print('Bye')



while True:
    reply = input('Enter text:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        num = int(reply)
        if num < 20:
            print('low')
        else:
            print(num ** 2)
print('Bye')




