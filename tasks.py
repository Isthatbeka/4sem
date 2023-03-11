class Task1:

    def __init__(self, french, pianists, swimmers):
        self.french = french
        self.pianists = pianists
        self.swimmers = swimmers

    def special_students(self):
        french = self.french
        pianists  = self.pianists
        swimmers =  self.swimmers
        swimmers_set = set(swimmers)
        pianists_set = set(pianists)
        french_learners_set = set(french)

        result_set = swimmers_set & pianists_set - french_learners_set
        result = list(result_set)
        return result


class Task2:

    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def get_unique_list_1(self):
        return len(set(list_1))

    def get_unique_both_lists(self):
        unique = set(list_1)
        unique.update(set(list_2))
        return len(unique)


class Task3:

    def __init__(self, films):
        self.films = films

    def get_results(films):
        ratings = {}
        for response in films:
            movie = response.lower().strip()
            ratings[movie] = ratings.get(movie, 0) + 1
        sorted_ratings = dict(sorted(ratings.items(), reverse=True))
        return sorted_ratings



class Task4:

    def __init__(self, text):
        self.text = text

    def word_counter(self):
        text = text.translate(str.maketrans('', '', string.punctuation)).lower()
        words = text.split()
        word_dict = {}
        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        sorted_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
        return sorted_dict


class Task5:

    def __init__(self, family):
        self.family = family

    def parents(self, name):
        return self.family[name]

    def grandparents(self, name):
        parents = self.parents(name)
        grandparents = []
        for parent in parents:
            grandparents.extend(self.parents(parent))
        return grandparents

    def siblings(self, name):
        siblings = []
        parents = self.parents(name)
        for parent in parents:
            siblings.extend([sibling for sibling in self.family[parent] if sibling != name])
        return siblings
    
    def children(self, name):
        children = []
        for child in self.family:
            if name in self.parents(child):
                children.append(child)
        return children


    def grandchildren(self, name):
        grandchildren = []
        children = self.children(name)
        for child in children:
            grandchildren.extend(self.children(child))
        return grandchildren

