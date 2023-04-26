# Code Challenge 28 Sorting Comparisons

Write functions which sort domain objects.

Your functions will receive an array of Movie objects.

Each Movie object has a title (string), a year (number), and a list of genres (array of strings).

One function will sort the movies by most recent year first.

One function will sort the movies, alphabetical by title, but will ignore any leading “A”s, “An”s, or “The”s.

## Whiteboard Process
![Whiteboard image](whiteboard28.png)

[Whiteboard link](https://www.figma.com/file/PjEdjU5eyM96Uosw7yl5dJ/Code-Challenge-28?node-id=0%3A1&t=vUWT9DmARiJFQ77I-1)

## Approach & Efficiency

1. Create output list
2. Iterate through movie list (movie_to_sort):
  1. If first movie, add it to output list
  2. Iterate through output list (current_movie):
     1. Compare movie_to_sort against current_movie. If movie_to_sort year >= current_movie year, insert movie_to_sort ***
     2. If end of output list, append movie_to_sort
3. Return output list

*** Comparison changes for year vs title.

Time: O(n!), because have to go through the entire list, then we have to go through the output list

Space: O(n), because we need a temporary list to hold the output


## Solution

[Link to code](https://github.com/mikeshen7/data-structures-and-algorithms/blob/main/python/code_challenges/movies/movies.py)

To run file, from code_challenges/movies/ directory:

python movies.py

To test, from code_challenges/movies/ directory:

pytest
