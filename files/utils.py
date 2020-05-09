import json
import os


def read_json(filepath):
    with open(filepath, 'r') as f:
        js = json.load(f)
        f.close()
    return js


def count_files(source, category):
    return len(os.listdir('./data/' + source + '/' + category))


def read_title_tags(filepath):
    with open(filepath, 'r') as f:
        js = json.load(f)
        f.close()
    return js['title'], js['processed_tags']


def article_exists(old, new):
    with open(old, 'r') as f:
        js = json.load(f)
    if js['date'] == new['date'] and js['time'] == new['time']:
        return True
    else:
        return False


def store_data(directory, category, content):
    path = "./data/" + directory + "/" + category + "/"
    dates = []

    exist = False

    for js in os.listdir(path):
        if content['date'] in js:
            if article_exists(path + js, content):
                exist = True
            dates.append(int(js.split('.')[-2]))
    if len(dates) == 0:
        a_id = 1
    else:
        dates.sort()
        a_id = dates[-1] + 1

    print(exist)
    if not exist:
        path = "./data/" + directory + "/" + category + "/" + category + "." + content['date'] + '.{0:0>3}'.format(
            a_id) + ".json"
        print('> Writing file: ', path)
        with open(path, 'w') as f:
            json.dump(content, f, indent=4, ensure_ascii=False)


def reset_df(df, sort_keys):
    # order by DES and reset index
    df = df.sort_values(sort_keys, ascending=False)
    df.reset_index(inplace=True)
    del df['index']
    return df
