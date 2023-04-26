def sort_title(movies):

    if len(movies) == 0:
        return movies

    movie_list = list()

    for movie_to_sort in movies:
        # for first item, just add it
        if len(movie_list) == 0:
            movie_list.append(movie_to_sort)

        else:
            for index, current_movie in enumerate(movie_list):
                # clean titles
                movie_to_sort_title = clean_titles(movie_to_sort["title"])
                current_movie_title = clean_titles(current_movie["title"])

                # CONDITION TO COMPARE
                if movie_to_sort_title <= current_movie_title :
                    movie_list.insert(index, movie_to_sort)
                    break

                # IF END OF LIST, ADD
                elif index == len(movie_list)-1:
                    movie_list.append(movie_to_sort)
                    break

    return movie_list

def sort_year(movies):
    if len(movies) == 0:
        return movies

    movie_list = list()

    for movie_to_sort in movies:
        # for first item, just add it
        if len(movie_list) == 0:
            movie_list.append(movie_to_sort)

        else:
            for index, current_movie in enumerate(movie_list):
                # CONDITION TO COMPARE
                if movie_to_sort["year"] >= current_movie["year"] :
                    movie_list.insert(index, movie_to_sort)
                    break

                # IF END OF LIST, ADD
                elif index == len(movie_list)-1:
                    movie_list.append(movie_to_sort)
                    break

    return movie_list

def titles(movie_list):
    '''
    Creates a list of movie title STRINGS from a list of movie OBJECTS
    Input: list of movie objects
    Output: list of titles
    '''
    output = list()
    for movie in movie_list:
        output.append(movie["title"])
    return output

def clean_titles(name):
    '''
    Removes leading 'a', 'an', 'the' from a title
    Input: string
    Return: string
    '''
    word_list = name.split()
    length = 0

    prefixes = ("a", "an", "the")

    if word_list[0].lower() in prefixes:
        length = len(word_list[0]) + 1

    return name[length:]

if __name__ == "__main__":
    movies = [
        {
            "title": "Beetlejuice",
            "year": 1988,
            "genres": ["Comedy", "Fantasy"],
        },
        {
            "title": "The Cotton Club",
            "year": 1984,
            "genres": ["Crime", "Drama", "Music"],
        },
        {
            "title": "The Shawshank Redemption",
            "year": 1994,
            "genres": ["Crime", "Drama"],
        },
        {
            "title": "Crocodile Dundee",
            "year": 1986,

            "genres": ["Adventure", "Comedy"],
        },
        {
            "title": "Valkyrie",
            "year": 2008,
            "genres": ["Drama", "History", "Thriller"],
        },
        {
            "title": "Ratatouille",
            "year": 2007,
            "genres": ["Animation", "Comedy", "Family"],
        },
        {
            "title": "City of God",
            "year": 2002,

            "genres": ["Crime", "Drama"],
        },
        {
            "title": "Memento",
            "year": 2000,

            "genres": ["Mystery", "Thriller"],
        },
        {
            "title": "The Intouchables",
            "year": 2011,

            "genres": ["Biography", "Comedy", "Drama"],
        },
        {
            "title": "Stardust",
            "year": 2007,
            "genres": ["Adventure", "Family", "Fantasy"],
        },
    ]

    sorted = sort_title(movies)

    print(sorted)


