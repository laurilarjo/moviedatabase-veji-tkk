from google.appengine.ext import db
import logging

# Represents a movie and its data
#    Title         - movie title (string
#    Year          - release year (string)
#    Director      - movie director (string)
#    Plot          - few line description of move plot (text) can be over 500chars
#    UserRating    - this is popularity rating from 1 to 10 (string)
#    MovieRating   - this is a MPAA rating (string)
#    Runtime       - length in minutes (string)
#    Cast          - a comma separated list of cast members (string)
#    Genres        - a comma separated list of genres (string)
#    Countries     - a comma separated list of countries (string)
#    PosterUrl     - link to movie poster image (string)
#    
class Movie(db.Model):
    id = db.StringProperty(required=True, default="tt0000000")
    title = db.StringProperty(required=True)
    year = db.StringProperty()
    director = db.StringProperty()
    plot = db.TextProperty()
    userRating = db.StringProperty()
    movieRating = db.StringProperty(multiline=True)
    runtime = db.StringProperty()
    cast = db.StringProperty(multiline=True)
    genres = db.StringProperty()
    countries = db.StringProperty()
    posterUrl = db.StringProperty()

    def getValueStringByName(self, valueName):
        if valueName == "title":
            return self.title
        elif valueName == "year":
            return str(self.year)
        elif valueName == "director":
            return self.director
        elif valueName == "plot":
            return self.plot
        elif valueName == "userRating":
            return str(self.userRating)
        elif valueName == "movieRating":
            return str(self.movieRating)
        elif valueName == "runtime":
            return str(self.runtime)
        elif valueName == "cast":
            return self.cast
        elif valueName == "genres":
            return self.genres
        elif valueName == "countries":
            return self.countries
        elif valueName == "posterUrl":
            logging.info(self.posterUrl)
            return "<img src="+self.posterUrl+">"

# Expects a table in the following format 
#    [id, title, year, director, plot, userRating, movieRating, runtime, 
#     cast, genres, countries]
#
    @staticmethod
    def movieConstruct(movieTable, givenUrl):
        if not movieTable:
            logging.info("movieConstruct called, but no movieTable")
            return
        
        return Movie(id         =   movieTable[0],
                     title      =   movieTable[1],
                     year       =   str(movieTable[2]),
                     director   =   movieTable[3],
                     plot       =   movieTable[4],
                     userRating =   str(movieTable[5]),
                     movieRating=   movieTable[6],
                     runtime    =   str(movieTable[7]),
                     cast       =   movieTable[8],
                     genres     =   movieTable[9],
                     countries  =   movieTable[10],
                     posterUrl  =   givenUrl)

class MovieList(db.Model):
    """ Contains links to user's all movies (movielist-items) and also methods
    for handling them """
    usedBy = db.UserProperty(required=True)
    
    @staticmethod
    def getMovieList(user):
        """ Returns the equivalent MovieList for the specified user and
            adds it to the database provided that it's a new user"""
        if not user:
            logging.warning("getMovieList was called with no user")
            return
        
        wantedList = db.Query(MovieList).filter("usedBy =", user).get()
                
        if not wantedList:
            logging.info("New user, adding to database: %s", user)
            wantedList = MovieList(usedBy=user)
            db.put(wantedList)
        else:
            logging.info("Returning user: %s", wantedList.usedBy)
            
        return wantedList
    
    def deleteMovie(self, movieid):
        """ Deletes a single movie from this list by given id provided that it exists """
        movieToDelete = self.getMovie(movieid)
        q = MovieListItem.all().filter("ownedBy =", self).filter("pointsTo =", movieToDelete)
        result = q.fetch(1)
        db.delete(result)
        if movieToDelete and result:
            logging.info("movie deleted: %s", movieid)
        else:
            logging.info("movie deletion failed: %s", movieid)
    
    def getMovies(self):
        """ Returns the Movies on this list"""
        return [movie.pointsTo for movie in self.movies]
    
    def getMovie(self, movieid):
        """ Returns the Movie that has the specified movieid if it's on this list"""
        for movie in self.getMovies():
            if movie.id == movieid:
                logging.info("getMovie requested, found movie: %s", movieid)
                return movie
            
        logging.info("getMovie requested, no movie found: %s", movieid)    
        
    def addMovie(self, movie):
        """ Adds a new Movie to this list
            if the Movie does not exist in the database, it's added there"""
        if not movie:
            logging.warning("addMovie was called with no movie")
            return False
        
        existingMovie = db.Query(Movie).filter("id =", movie.id).get()
        alreadyInList = db.Query(MovieListItem).filter("ownedBy =", self).filter("pointsTo =", existingMovie).get() 
        
        if existingMovie and alreadyInList:
            logging.info("Existing movie and in list: %s", existingMovie.id)
        elif existingMovie and not alreadyInList:
            logging.info("Existing movie but not in list: %s", existingMovie.id)
            db.put(MovieListItem(ownedBy=self, pointsTo=existingMovie))
        else:
            logging.info("New movie and not in list: %s", movie.id)
            db.put(movie)
            db.put(MovieListItem(ownedBy=self, pointsTo=movie))
            
        return True
    
class MovieListItem(db.Model):
    """ This class represents one to many -relationships, which maps user's 
    movies to the actual movie-objects"""
    ownedBy = db.ReferenceProperty(MovieList,
                                   collection_name="movies",
                                   required=True)
    pointsTo = db.ReferenceProperty(Movie,
                                    required=True)
    
class MovieQueries(db.Model):
    
    queryName = db.StringProperty(required=True)
    movieId = db.StringProperty(required=True)
    movieTitle = db.StringProperty(required=True)
    
    @staticmethod
    def getListing(query):
        logging.info("getting movielisting from cache")
        results = db.Query(MovieQueries).filter("queryName =", query).fetch(10)
        
        if not results:
            logging.info("no movies in cache with query: %s", query)
        else:
            for entry in results:
                logging.info("entry: %s", entry.movieTitle)
        
        return results
    
    @staticmethod
    def addEntry(query, movieid, title):
        logging.info("adding %s to cache...", title)
        
        existingMovie = db.Query(MovieQueries).filter("queryName = ", query).filter("movieId =", movieid).get()
        
        if existingMovie:
            logging.info("movie was already in the cache")
            return
        
        else:
            logging.info("New movie and not in cache. Lets add: %s, %s, %s", query, movieid, title)
            movie = MovieQueries(queryName=query,movieId=movieid, movieTitle=title)
            db.put(movie)
        
        
        

def runTest():
    from google.appengine.api import users
    
    logging.debug("Entering datastore runTest() method")

    currentList = MovieList.getMovieList(users.GetCurrentUser())
    currentList.addMovie(Movie(id="tt0000001", title="Saw 2"))
    currentList.addMovie(Movie(id="tt0000002", title="Patriot"))
    
    for movie in currentList.getMovies():
        logging.debug("Found a movie: " + movie.title)
        
    anotherList = MovieList.getMovieList(users.GetCurrentUser())
    anotherList.addMovie(Movie(id="tt0000003", title="Die Hard"))
    anotherList.addMovie(Movie(id="tt0000003", title="Die Hard"))
    anotherList.addMovie(Movie(id="tt0000004", title="Cliffhanger"))
    
    for movie in anotherList.getMovies():
        logging.debug("Found a movie: " + movie.title)
    
    thirdList = MovieList.getMovieList(users.GetCurrentUser())
    
    for movie in thirdList.getMovies():
        logging.debug("Found a movie: " + movie.title)

    logging.debug("Exiting datastore runTest() method")   
    