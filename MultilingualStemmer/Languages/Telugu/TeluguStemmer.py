import os

from .bin import lemmatiser as lmt
from .bin import unitok_lib as unlib
from .bin import te_helpers as tehp
from .bin import tag2vert as tv

current_dir = os.path.dirname(os.path.realpath(__file__))

# Temp file names
words_tmp_file_name = current_dir + "/telugu_words.tmp"
tagger_op_file = current_dir + "/tagger_out.tmp"
# Tagger file path

tagger_file_path = current_dir+"/bin/tnt"
models_path = current_dir+"/models/telugu"

def write_to_tmp_file(te_list):
    with open(words_tmp_file_name, 'w') as file: 
        file.write("<doc>\n")        
        for word in te_list:
            file.write(word+"\n")        
        file.write("</doc>")        
    return

def run_tagger_script():
    os.system(tagger_file_path + " -H -v0 "+ models_path + " " + words_tmp_file_name + " | sed -e 's/\t\+/\t/g' > " + tagger_op_file)
    return

def read_tagger_output():
    texts_list = []    
    with open(tagger_op_file, 'r') as file:
        file.readline()
        for line in file:
            texts_list.append(line.strip())            
        texts_list.pop()            
    return texts_list

def stem(word:str):
    te_list = unlib.tokenise(word, unlib.LANGUAGE_DATA['telugu']())
    te_list = tehp.remove_non_words(te_list)
    write_to_tmp_file(te_list)
    run_tagger_script()
    te_postags_list = read_tagger_output()
    lmt.load_lemmatiser_default(current_dir+"/models/telugu.lemma")

    for item in te_postags_list:
        word_tag = item.split('\t')
        lemma = lmt.lemmatise_word(word_tag[0], word_tag[1])
        word, lemma_corr, pos_tag = tv.massage_lemma(word_tag[0], lemma, word_tag[1])
        # print(word, lemma_corr, pos_tag)
        print(lemma_corr)