#python_version == '3.7'

import pickle

def load_data(file):
    try:
        infile = open(file, 'rb')
        result = pickle.load(infile)
        infile.close()
        return result
    except IOError as errormsg:
        print(errormsg)

def query_following(user_name):
    following_num = 0
    data = load_data("followers.pydata")
    for name, followers in data.items():
        if user_name in followers:
            following_num += 1
    return following_num

def update():
    try:
        result = load_data("followers.pydata")
        result["William Smith"].append("Lorna Carrico")
        result["Anne Smelcer"] = ["Christine Phillips", "Charles Mason", "Tim Lathrop"]
        newfile = open('followers-updated.pydata', 'wb')
        pickle.dump(result, newfile)
        newfile.close()
    except IOError as errormsg:
        print(errormsg)       

def get_num_of_followers():
    try:
        countfile = open('followers-updated.pydata', 'rb')
        wholelist = pickle.load(countfile)
        countfile.close()
        count = {}
        for key in wholelist.keys():
            temp = len(wholelist[key])
            count[key] = temp
        return count
    except IOError as errormsg:
        print(errormsg)   

