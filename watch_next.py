import spacy


def get_movie_suggestions(movie_description, movies):
    """Returns the most similar movie to the movie description

    Parameters
    movie_description: str  # The description of the movie
    movies: dict  # A dictionary of movie names and descriptions"""
    nlp = spacy.load("en_core_web_md")
    nlp_movie_description = nlp(movie_description)
    highest_similarity = 0
    most_similar_movie = ""
    for movie_name, movie in movies.items():
        similarity = nlp_movie_description.similarity(nlp(movie))
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_movie = movie_name
    return most_similar_movie


def main():
    """Reads movies.txt to a dictionary,
    splits the line by colon to get the movie name and description, removing trailing whitespace.
    and then calls get_movie_suggestions to get the most similar movie"""
    movies = {}
    with open("movies.txt", "r") as f:
        for line in f:
            movie_name, movie_description = line.split(":")
            movies[movie_name] = movie_description.strip()
    test_movie = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""
    print(get_movie_suggestions(test_movie, movies))


if __name__ == '__main__':
    main()
