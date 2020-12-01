import re
print('** Welcome to madlibs game **\n** Mad Libs are a word replacement game **\n** so you will enter some wordes and then **\n** it will replaced in a pharahraph it **\n** may be a funny  and you will lough ... **\n** just answer the qustions and press enter..**')

def read_template(path):
    with open(path,'r') as file:
        content=file.read()
        return content




def  parse():
    f=read_template('assest/madlib.txt')
    parsed = re.sub(r'\{.*?\}','{}',f)
    parsed2 = re.sub('\\(.+?\)','',f)
    list_of_words = re.findall('{(.+?)}',parsed2)

    return list_of_words,parsed

def prompt():

    words=parse()
    user_list=[]
    word_list=words[0]
    text_without_words=words[1]
    #print(words)
    for i in word_list:
        user_input=input('give me  '+i+' ')
        user_list.append(user_input)
    return user_list,text_without_words    

def merge():
    promp=prompt()
    user_list=promp[0]
    text_without_words=promp[1]
    result= text_without_words.format(*tuple(user_list))
    print(result)
    return result

def write_file():
    final_ext=merge()
    with open('madlib_cli/madlib_result.txt','w') as file:
        text=file.write(final_ext)
    with open('madlib_cli/madlib_result.txt','r') as file2:
        text=file2.read()
        return text
        
   
write_file()