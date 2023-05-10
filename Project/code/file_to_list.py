from os.path import dirname, join
       
# Returns list of counties or professions from respective file 
def file_to_list(txt):
    file_path = join(dirname(dirname(__file__)), txt)
    return open(file_path, encoding='utf-8').read().splitlines()