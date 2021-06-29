
import os 
import sys
import re
from collections import defaultdict

'''
this is a content generator based on tags within all markdown files.
tags should be enteren ar the bottom of the file
'''

def file_name (filepath):
    '''
    Return the filename which is at the first line of the file
    '''
    with open(filepath, "r") as f1:
        first_line = f1.readline()
        return first_line


def tag_name (filepath):
    '''
    Return a list contains tags within the file. 
    '''
    result = []
    # to support tag in lines, we use regular expression to match with.
    pattern = re.compile(r'#[^ #]+#')
    with open(filepath, "r") as f:
        for line in f:
            curr = pattern.findall(line)
            if curr != []:
                for elem in curr:
                    result.append(elem.replace("#",''))
        if result ==[]:
            return ["Untagged"]
        else:
            return result


def connecter(filepath):
    '''
    make connection between file name and the tag_name
    keep the result into a dictionary.
    '''
    # get a dictionary whos key:tag, value:filepath
    list_dir = os.walk(filepath)
    dic_firstline = defaultdict(list)
    for root, dirs, files in list_dir:
        for f in files:
            file_type = f.split('.') [1]
            file_path = os.path.join(root, f)
            if file_type == "md":
                for elem in tag_name(file_path):
                    dic_firstline.setdefault(elem, []).append(file_path)
                
    #after we get the dictionary, we check tags have higher level but empty at lower level.
    keys = []
    count = 0
    for elem in dic_firstline.keys():
        keys.append(elem)
        count += get_level(elem)+1
    number = len(keys)
# a terriable solution but works well anyway.
    while number < count:
        for tags in keys:

            if tags not in keys:
                dic_firstline[tags] = []
                keys.append(tags)
                number +=1
            if get_level(tags) != 0 and get_front(tags) not in keys:
                dic_firstline[get_front(tags)] = []
                keys.append(get_front(tags))
                number +=1
        number +=1# since the count is always greater or equal to the real number of tags
            # this count actually provide a upper bounder
    return  dic_firstline

def get_level(tag:str):
    return tag.count("/")

def get_front(tag:str) -> str:
    '''
    Get the front tag 
    '''
    for i in range (len(tag)-1, -1,-1):
        if tag[i] == '/':
            return tag[:i]
        
    return "Nfound"

def get_end(tag:str):
    for i in range (len(tag)-1, -1, -1):
        if tag[i] == '/':
            return tag[i+1:]
    return tag

def num_of_tag(dic:dict)-> int:
    result = 0
    for elem in dic.keys():
        for elem2 in dic[elem]:
            result += 1
    return result
        

def order_dic(dic:dict):
    '''
    this will return a dictionary which is ordered by its tag.
    '''
    list_keys = []
    for elem in dic.keys():
        list_keys.append(elem)
    result = []
    no_front = []
    #order the tags
    for elem in sorted(list_keys, key = get_level):
        front = get_front(elem)
        if get_level(elem) == 0:
            result.append(elem)
        elif front in result:
            position = result.index(front)
            result.insert(position+1, elem)
        else:
            no_front.append(elem)
    
    # add no front into the final result list 
    for elem in no_front:
        result.append(elem)
    return result

        
def markdown_maker(dic: dict, filepath):
    '''
    Write infromations form the dictionary to a markdown file
    the markdown file is using tag system, which maintian a link to its 
    title to the actually page itself, classified by tags
    '''
    filepath = os.path.join(filepath, "tag.md")
    print("The final path is :",filepath)
    order_list1 = order_dic(dic)
    with open(filepath, 'w+') as f:
        for tags in order_list1:
            real_tag =repr(tags)
            level = real_tag.count('/') + 1
            f.write("#"*level + " " + get_end(tags) + "\n")
            for file_path in dic[tags]:
                file_title = file_name(file_path)
                f.write("[" + file_title.replace("#",'') + ']' + '(' + file_path + ')\n')
            print("Success!")
    return 

if __name__ == "__main__":
    try:
        markdown_maker(connecter(os.getcwd()), os.getcwd())
    except Exception as e:
        print("An Error occurs:\n", e)