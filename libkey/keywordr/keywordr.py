import re
import string
from pattern.en import parse

stopwords = []


def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>)"]+'
    match = re.findall(regex, text)
    links = []
    for x in match:
        if x[-1] in string.punctuation:
            links.append(x[:-1])
        else:
            links.append(x)
    return links


def cleanup(query):
    try:
        urls = extract_link(" " + query + " ")
        for url in urls:
            query = re.sub(url, "", query)
        q = query.strip()
    except:
        q = query
    q = re.sub(' RT ', '', ' ' + q + ' ').strip()
    return q


def convert_tag_format(query):
    word = query.split(' ')
    postag = [(x.split('/')[0], x.split('/')[1]) for x in word]
    return postag


def get_pos_tags(text):
    tagged_sent = parse(text)
    return convert_tag_format(tagged_sent), tagged_sent


def normalise(word):
    word = word.lower()
    return word


def acceptable_word(word):
    accepted = bool(2 <= len(word) <= 40
                    and word.lower() not in stopwords)
    return accepted


def extract_entity(filetext):
    last_entity = ''
    last_tag = ''
    mention2entities = {}
    for line in filetext.split('\n'):
        line = line.strip()
        if line == '':
            continue
        line_split = line.split('\t')
        if re.search('B-', line_split[1]):
            if last_entity != '':
                if not last_tag in mention2entities:
                    mention2entities[last_tag] = []
                mention2entities[last_tag].append(last_entity.strip())
            last_entity = line_split[0] + ' '
            last_tag = line_split[1][2:]
        elif re.search('I-', line_split[1]):
            last_entity += line_split[0] + ' '
    if last_entity != '':
        if not last_tag in mention2entities:
            mention2entities[last_tag] = []
        mention2entities[last_tag].append(last_entity.strip())
    return mention2entities


def get_entities_from_phrase(tagged_sent, phrase2consider):
    word = tagged_sent.split(' ')
    bio_tags = [normalise(x.split('/')[0]) + '\t' + x.split('/')[2] for x in word]
    bio_text = '\n'.join(bio_tags)
    mention2entities = extract_entity(bio_text)
    # print mention2entities.keys()

    _mention2entities = {}
    for mention in mention2entities:
        if not mention in phrase2consider:
            continue
        _mention2entities[mention] = []
        for entity in mention2entities[mention]:
            _entity = ' '.join([word for word in entity.split(' ') if acceptable_word(word)]).strip()
            if _entity != '':
                _mention2entities[mention].append(_entity)

    entities = []
    for mention in _mention2entities:
        entities.extend(_mention2entities[mention])
    return entities


def get_keywords(text, phrase2consider=['NP', 'ADJP']):
    _text = cleanup(text)
    try:
        postoks, tagged_sent = get_pos_tags(_text)
        entities = get_entities_from_phrase(tagged_sent, phrase2consider)
    except:
        return []
    return entities


def extract_hashtag(text, to_normalize=True):
    regex = r'#[^\W\d_]+\b'
    if to_normalize: text = normalise(text)
    match = re.findall(regex, text)
    return match


def extract_users(text, to_normalize=True):
    regex = r'@[^\b ]+\b'
    if to_normalize: text = normalise(text)
    match = re.findall(regex, text)
    return match


def all_entities(text, to_normalize=True, with_unigram=True):
    text = text.decode('utf-8')
    if to_normalize: text = normalise(text)
    if with_unigram:
        entities = text.split()
    else:
        entities = []
    keywords = get_keywords(text, ['NP', 'VP', 'ADJP', 'ADVP'])
    for each in keywords:
        if not each in entities:
            entities.append(each)
    return entities