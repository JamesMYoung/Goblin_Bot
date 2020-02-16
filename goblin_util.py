# goblin_util.py
# A collection of functions separate from any class functionality

from Levenshtein import jaro_winkler


# Selects the best match from provided keywords
# returns None if match value is less than 0.5
def select_best(keywords, text):
    msg = ''
    
    highest_match = 0
    guessed_word = None
    
    best_keyword = None
    
    
    for keyword in keywords:
            word_dist = jaro_winkler(keyword, str(text))
            if highest_match < word_dist:
                guessed_word = keyword
                highest_match = word_dist
            
            if keyword == str(text):
                best_keyword = str(text)
        
    if best_keyword == None and highest_match > 0.8:
        msg += '```'
        msg += 'Converting \"' + str(text) + '\" to \"' + guessed_word + '\"'
        msg += ' with ' + '{0:.1f}%'.format(highest_match*100) + ' certainty\n'
        msg += '```'
        
        best_keyword = guessed_word
    elif highest_match < 0.8:
        msg += '```'
        msg += 'Unable to recognize input \"' + str(text) + '\"\n'
        msg += '```'
        
    return msg, best_keyword