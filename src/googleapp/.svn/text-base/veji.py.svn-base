#!/usr/bin/env python
#
# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A movie list web application built on Google App Engine."""

__author__ = 'Lauri Larjo and Joona Olkkola'

import logging
import datetime
import os
import random
import string
import sys
import wsgiref.handlers

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import login_required

import model.datastore
import connector.imdbConnector
import testclasses.stubs

# Set to true if we want to have our webapp print stack traces, etc
_DEBUG = True
logging.getLogger().setLevel(logging.DEBUG)


class BaseRequestHandler(webapp.RequestHandler):
  """Supplies a common template generation function.

  When you call generate(), we augment the template variables supplied with
  the current user in the 'user' variable and the current webapp request
  in the 'request' variable.
  """
  def generate(self, template_name, template_values={}):
    values = {
      'request': self.request,
      'user': users.GetCurrentUser(),
      'login_url': users.CreateLoginURL(self.request.uri),
      'logout_url': users.CreateLogoutURL('http://' + self.request.host + '/'),
      'debug': self.request.get('deb'),
      'application_name': 'Veji Multimedia Library',
    }
    values.update(template_values)
    directory = os.path.dirname(__file__)
    path = os.path.join(directory, os.path.join('templates', template_name))
    self.response.out.write(template.render(path, values, debug=_DEBUG))


class MainPage(BaseRequestHandler):
  """Lists the movies for logged user and acts as a main page"""
  @login_required
  def get(self):
    usersMovieList = model.datastore.MovieList.getMovieList(users.get_current_user())
    movies = usersMovieList.getMovies()

#    for movie in movies:
#        logging.info("movie: %s", movie.id)

    self.generate('index.html', {
      'movies': movies })

class SynopsisPage(BaseRequestHandler):
  """easter egg :D"""
  @login_required
  def get(self):
    
    self.response.out.write("""Hahaa, you found our easter egg! <br/><br/>
    <img src="http://www.penny-arcade.com/images/2008/20080915.jpg"/>""")

class ShowMovieDetailsAction(BaseRequestHandler):
    """ Receives movieid and makes a database query with it. Returns that movie's
    details back to user one at a time (not very good performance, but this provides
    better layout handling in index.html)"""
    def post(self):
        movieid = self.request.get('movieid')
        getelement = self.request.get('getelement')
        
        if not movieid:
            logging.info("showMovieDetails called, but movieid was not recognized")
            self.error(403)
            return
        elif not getelement:
            logging.info("showMovieDetails called, but getelement was not recognized")
            self.error(403)
            return
        else:
            logging.info("showMovieDetails called for: %s %s", movieid, getelement)
        
        currentList = model.datastore.MovieList.getMovieList(users.get_current_user())
        requestedMovie = currentList.getMovie(movieid)
        
        if not requestedMovie:
            logging.info("no details found for movie: %s", movieid)
            return
        else:
            logging.info("details were successfully found for movie: %s", requestedMovie.id)

        self.response.out.write(requestedMovie.getValueStringByName(getelement))
       

class AddNewMovieAction(BaseRequestHandler):
  """Adds a new movie for the current user. Movieid is used to get the 
  information from imdb database"""
  def post(self):
    user = users.GetCurrentUser()
    
    title = self.request.get('movietitle')
    movieid = self.request.get('movieid')
    logging.info("addNewMovieAction called with user: %s for movieid: %s", user, movieid)
    
    if not user or not movieid:
      self.error(403)
      logging.info("user or movieid not recognized, exiting addNewMovieAction")
      self.redirect('/')
      return
    
    movieTable = connector.imdbConnector.IConnector.getMovieData(movieid)
    posterUrl = connector.imdbConnector.IConnector.getMoviePoster(movieid)
    movieList = model.datastore.MovieList.getMovieList(user)
    
    if movieList.addMovie(model.datastore.Movie.movieConstruct(movieTable, posterUrl)):
        logging.info("Movie added successfully to list")
    else:
        logging.info("Movie was not added to list")

    if self.request.get('next'):
      self.redirect(self.request.get('next'))
    else:
      self.redirect('/')


class QueryMoviesAction(BaseRequestHandler):
  """Handles the movie search and add query.
  """
  def post(self):
    query = self.request.get('query')
    
    #check how many results we get from cache
    logging.info("check cache if we have results for %s", query)
    results = model.datastore.MovieQueries.getListing(query)
    
    string = ""
    if not results:
    
        results = connector.imdbConnector.IConnector.getMovieList(query)
        logging.info("we got parsed results with query: %s", query)
        
            
        i = 0
        while i < len(results):
            model.datastore.MovieQueries.addEntry(query, results[i], results[i+1])
            i = i+2
                
        #print results found by parsing
        i = 0
        while i < len(results): 
            string += "<option value=\""+results[i]+"\">"+results[i+1]+"</option>"
            i = i+2
    
    else:
        logging.info("from cache was found %s", results[0].movieTitle)
        
    
        for entry in results:
            string += "<option value=\""+entry.movieId+"\">"+entry.movieTitle+"</option>"

        
        
    logging.info("options: %s", string)
    
    self.response.out.write(string)
    
    

class MainFormAction(BaseRequestHandler):
  """Performs an action in the user's MovieList. Only 'Delete' action
  is supported
  """
  def post(self):
    action = self.request.get('action')
    moviesToDelete = self.request.get('list', allow_multiple=True)
    
    #if someone is hax0ring
    if action != 'Delete':
      self.error(403)
      return
  
    #get this users movie list
    movieList = model.datastore.MovieList.getMovieList(users.get_current_user())
          
    for movieid in moviesToDelete:
        logging.debug("calling delete for %s", movieid)
        movieList.deleteMovie(movieid)

    self.redirect(self.request.get('next'))




def main():
  application = webapp.WSGIApplication([
    ('/', MainPage),
    ('/synopsis', SynopsisPage),
    ('/addnewmovie.do', AddNewMovieAction),
    ('/querymovies.do', QueryMoviesAction),
    ('/showmoviedetails.do', ShowMovieDetailsAction),
    ('/mainformaction.do', MainFormAction),
  ], debug=_DEBUG)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
  #testclasses.stubs.VejiTests.runTests()
