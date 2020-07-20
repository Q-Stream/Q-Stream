import pickle, os


def load():
    scorefile = "db.bat"
    if os.path.exists(scorefile):
        with open(scorefile, 'rb') as sf:
            scores = pickle.load(sf)
    else:
        scores = []

    with open(scorefile, "wb") as sf:
        pickle.dump(scores, sf)
    return scores


def scor_func(url):
    scorefile = "db.bat"
    if os.path.exists(scorefile):
        with open(scorefile, 'rb') as sf:
            scores = pickle.load(sf)
    else:
        scores = []
    scores.append(url)

    with open(scorefile, "wb") as sf:
        if len(scores) > 100:
            print("here", scores)
            scores = scores[1:]
        pickle.dump(scores, sf)
    return scores


if __name__ == '__main__':
    # for url in range(1, 101):
    #    scores = scor_func(url)
    print(scor_func(103))

    print(load())
