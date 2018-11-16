def log_to_file(text):
    f=open('log.txt','a+')
    f.write(text)
    f.close()