import logging
import re

from common import parser
from testclasses import stubs
from google.appengine.api import urlfetch

class IConnector:
    """Static class which acts as a connector for retrieving IMDB-data.
    Makes a URLfetch to IMDB and retrieves one html-page, which it parses
    depending on the information wanted from it. The methods return
    the response in a structured string-array."""
        
    @staticmethod
    def getMoviePoster(movieid):
        """ Queries IMDB for this specific movie's poster picture URI.
        Returns it as a string """
        
        logging.debug("looking for movie poster")
        myparser = parser.Parser("1")
        
        url = "http://www.imdb.com/title/" + movieid + "/posters"
        
        #stub = stubs.IMDBStub()
        #data = stub.getPosterPage(url)
        data = urlfetch.fetch(url)
        
        if not data.content or data.status_code != 200:
            logging.debug("urlfetch failed")
            return ""
        
        data = data.content
        #logging.debug(data)
        
        host = "http://posters.imdb.com/posters/"

        uri = myparser.parseBetween(data, host, "\"><td><td><a href=\"")
        logging.debug("uri found: %s", uri)
        
        if uri:
            uri = host + uri
            logging.debug("poster found: %s", uri)
        else:
            logging.debug("no poster found")
        
        return uri
    
    
    
    @staticmethod
    def getMovieList(query):
        """searches IMDB with the given query and returns results using the array format:
        [1.st movie_id, 1.st movie_name, 2.nd movie_id, 2nd. movie_name, etc]"""
        
        logging.getLogger().setLevel(logging.DEBUG)
        myparser = parser.Parser("1")
        logging.debug("searching movies, query: %s", query)
        
        #this is to convert white spaces into %20, so that urlfetch works
        query = str(query)
        substr = query
        for i in range(0, len(query)):
            if query[i] == ' ':
                substr = query[0:i] + "%20"
                substr += query[i+1:len(query)]
                
                
        url = "http://www.imdb.com/find?q=" + substr
        
        # stub-implementaatio, korvaa urlfetchilla        
        #stub = stubs.IMDBStub()
        #data = stub.getSearchPage(url)
        
        
        
        data = urlfetch.fetch(url)
        
        if not data.content or data.status_code != 200:
            logging.debug("urlfetch failed")
            return ""
        
        data = data.content
        #logging.debug(data)
        
        #check if we got many results, or if we are directly at movie details-page
        #looking for 'add=<movieid>" target=' which only exists on a details-page
        movieid = myparser.parseBetween(data, "add=", "\"")
        if not movieid:
            movieid = myparser.parseBetween(data, ";add=", "'")
        
        if movieid:
            logging.debug("we found match: movieid: %s", movieid)
            
        if not movieid:
            logging.debug("we found several results")
        
        #extract possible matches
        popular_results = myparser.parseBetween(data, "<b>Popular Titles</b>",\
                                                 "</table>")
        exact_results = myparser.parseBetween(data, "<b>Titles (Exact Matches)</b>",\
                                              "</table>")
        partial_results = myparser.parseBetween(data, "<b>Titles (Partial Matches)</b>",\
                                              "</table>")
        
        logging.debug("popular_results: %s", popular_results)
        logging.debug("exact_results: %s", exact_results)
        logging.debug("partial_results: %s", partial_results)
        
        #gather all the matches
        data = popular_results + exact_results
        #if no exact or popular matches, resort to partial matches
        if not data:
            data = partial_results
        
        #if still no results, return empty answer    
        if not data:
            result = ["0", ""]
            return result
        
        logging.debug("start parsing... %s", data)
        
        begin = "<tr>"
        end = "</tr>"
        count = 0
        year = ""
        title = ""
        results = []
        
        startreading = data.find(begin)
        finishreading = data.find(end, startreading)
        logging.debug("startread: %d finish: %d", startreading, finishreading)
        
        #go through all the matches
        while (startreading != -1 and startreading < len(data)):
            logging.debug("startreading=%d", startreading)
            startreading += len(begin)
            entry = data[startreading:finishreading]
            logging.debug("entry: %s", entry)
            
            startreading = data.find(begin, finishreading + 1)
            finishreading = data.find(end, startreading)
            
            #parse the matched-line
            entry = re.findall('<a href="\/title\/tt(\d+)\/.*\">(.+)<\/a> \((\d+)\/?[a-z]*\)(?: \((.+)\))?', entry)
            logging.debug("entry: %s", entry)
            if entry:
                movieid = entry[0][0]
                title = entry[0][1]
                year = entry[0][2]
            else:
                continue
            logging.debug("title: %s", title)
             
            results.append("tt" + movieid)
            results.append(title + " ("+year+")")
            
            logging.info("retrieved movie listing for %s", title)
            if len(results) >= 20:
                logging.debug("we found enough results (10), exiting...")
                break
            
        return results
    
    
    
    @staticmethod
    def getMovieData(movienumber):
        """fetches moviedata from IMDB and returns it in a defined array 
        [id, title, year, director, plot, userRating, mpaarating, runtime, 
        cast, genres, countries]"""
        
        logging.getLogger().setLevel(logging.INFO)
        movieid = movienumber
        title = ""
        year = ""
        director = ""
        plot = ""
        userrating = ""
        mpaarating = ""
        runtime = ""
        cast = ""
        genres = ""
        countries = ""
        
        myparser = parser.Parser("1")
        #this regexp-pattern is used when searching names from links (doesn't work)
        #namepattern = re.compile('<a href="/name/[^"]*">([^<]*)</a>')
        
        
        logging.debug("looking for movie id: " + movieid)
        
        url = "http://www.imdb.com/title/" + movieid
        
        # stub-implementaatio, korvaa urlfetchilla        
        stub = stubs.IMDBStub()
        data = stub.getDataPage(url)
        
        data = urlfetch.fetch(url)
        
        if not data.content or data.status_code != 200:
            logging.debug("urlfetch failed")
            return ""
        
        data = data.content
        #logging.debug(data)
        
        #parse title & year
        titleData = myparser.parseBetween(data, "<title>", "</title>")
        logging.debug("title: " + titleData)

        titleData2 = re.findall('(.+) \((\d+).*\)', titleData)
        
        if titleData2:
            title = titleData2[0][0]
            year = titleData2[0][1]
        else: # NOT TESTED
            titleData2 = re.findall('(.+) \(\?\?\?\?\)', titleData)
            title = titleData2[0][0]
            
        logging.debug("after regexp: %s - %s", title, year)
        
        
        #parse director
        director = myparser.parseBetween(data, ">Director:</h5>", "</div>")
        if not len(director):
            director = myparser.parseBetween(data, ">Directors:</h5>", "</div>") 
        logging.debug("director: %s", director)
        director = re.findall('>...*?<', director)

        logging.debug("after regexp: %s", director)
        director = director[0]
        director = director[1:len(director)-1]
        logging.debug("director: %s", director)
        
        #parse user rating
        userrating = myparser.parseBetween(data, ">User Rating:</h5>", "</b>")
        userrating = myparser.parseBetween(userrating, "<b>", "/")
        logging.debug("userrating: %s", userrating)
        
        #parse mpaarating
        ratingcountry = "USA";
        mpaarating = myparser.parseBetween(data, ">MPAA</a>:</h5>", "</div>")
        
        if not mpaarating:
            mpaarating = myparser.parseBetween(data, ">Certification:</h5>", "</div>")
            mpaarating = myparser.parseBetween(mpaarating, "certificates=$ratingcountry","/a>")
            mpaarating = myparser.parseBetween(mpaarating, ">", "<")
            
        mpaarating.strip()
        logging.debug("mpaarating: %s", mpaarating)
        
        #parse actors (name-link pattern -regexp does not work, this doesn't work)
        runtime = "124"
        cast = "Mel Gibson, Scarlett Johansson"
        genres = "Action, Romance"
        countries = "US"
        
        #parse plot
        plot = myparser.parseBetween(data, ">Plot Outline:</h5> ", "</div>")
        if not plot:
            plot = myparser.parseBetween(data, ">Plot Summary:</h5> ", "</div>")

        if not plot:
            plot = myparser.parseBetween(data, ">Plot:</h5>", "</div>")

        
        plot = plot.strip()
        
        #this removes the synopsis and full description links
        #plot_end = plot.find("<a ")
        #if plot_end != -1:
        #    plot = plot[0:plot_end]
        
        link_index = plot.find("href=\"")
        temp = plot[0:link_index] + "href=\"http://www.imdb.com" + plot[link_index+6:len(plot)]
        
        plot = temp
            
        logging.debug("plot: %s", plot)
        
        #construct the result table
        result = [movieid, title, year, director,plot, userrating, \
                  mpaarating,runtime,cast,genres,countries]
        
        logging.info("retrieved movie info")
        return result
  
    
def runTest():
    
    logging.debug("Getting movieListing...")
    movieList = IConnector.getMovieList("matrix")
    i = 0
    while i < len(movieList): 
        logging.debug("found: %s - %s", movieList[i], movieList[i+1])
        i = i+2
        
    logging.debug("Getting movieData for tt0187393...")
    movieData = IConnector.getMovieData("tt0187393")
    logging.debug("found: %s - %s - %s", movieData[0], movieData[1], movieData[2])
    
    logging.debug("Getting moviePoster for tt0187393...")
    posterUrl = IConnector.getMoviePoster("tt0187393")
    logging.debug("Movie Poster: %s", posterUrl)
    
#runTest()