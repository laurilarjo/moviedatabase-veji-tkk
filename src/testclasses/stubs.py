
import model.datastore
import connector.imdbConnector

class VejiTests:
    
    @staticmethod
    def runTests():
        model.datastore.runTest()
        connector.imdbConnector.runTest()
    
class IMDBStub:
    
    def getDataPage(self, url):
        result = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">

<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=7" />
<meta http-equiv="content-type" content="text/html; charset=iso-8859-1">
<title>The Patriot (2000)</title>
<meta name="title" content="The Patriot (2000)">
<meta name="description" content="Directed by Roland Emmerich.  With Mel Gibson, Heath Ledger, Joely Richardson. Peaceful farmer Benjamin Martin is driven to lead the Colonial Militia during the American Revolution when a sadistic British officer murders his son. Visit IMDb for Photos, Showtimes, Cast, Crew, Reviews, Plot Summary, Comments, Discussions, Taglines, Trailers, Posters, Fan Sites">

<meta name="keywords" content="Reviews, Showtimes, DVDs, Photos, Message Boards, User Ratings, Synopsis, Trailers, Credits">
<link rel="stylesheet" type="text/css" media="screen" href="http://i.media-imdb.com/images/SF06e7dce069189b1d2d32527382dfcebb/css2/consumersite.css" />
<script type="text/javascript" src="http://i.media-imdb.com/images/SF112739c68dcd8909b2a019a53e03b31c/a/js/ads.js"></script>
<link rel="icon" href="http://i.imdb.com/favicon.ico" />
<link rel="apple-touch-icon" href="http://i.media-imdb.com/apple-touch-icon.png" />
<style type="text/css">.showtimes { font-family: Arial, Helvetica, sans-serif }.showtimes .heading { font-size: 16px; font-weight: bold }.showtimes .time { color: #ff0000 }.tabular { border-collapse: collapse; border: 1px solid #9999ff }.tabular td.heading { background: #bbbbff }.tabular td.heading-right { background: #bbbbff; text-align: right; font-size: small }.tabular td.address { font-size: small; color: #666666; background: #eeeeee }.tabular td.detail { font-size: small; background: #eeeeee }.tabular tr.alternate { background: #eeeeee }.tabular td.item { border: 1px solid #9999ff }</style><link rel="stylesheet" type="text/css" href="http://i.media-imdb.com/images/SFca2cd0a5ab9db43ff9d7f7af6cc6f361/tn15/tn15.css" />




<link rel="stylesheet" type="text/css" media="screen" href="http://i.media-imdb.com/images/SF2c798c76034e2cd9e0b278a275ee3096/wheel/base.css" />

<link rel="stylesheet" type="text/css" media="screen" href="http://i.media-imdb.com/images/SF2db9d72d9c300f0b307f0a3ae3ac0ef9/wheel/widgets.css" />
<link rel="stylesheet" type="text/css" media="screen" href="http://i.media-imdb.com/images/SFb72d7f17aa6a7c4db68966d02a8587d3/wheel/layout.css" />

<!--[if IE]>
<link rel="stylesheet" type="text/css" media="screen" href="http://i.media-imdb.com/images/SF6f54b7612c95a3ca71b33f74bb197e49/wheel/ie.css" />
<![endif]-->
<link rel="stylesheet" type="text/css" href="http://i.media-imdb.com/images/SFf4998318a26e5a6e8304e5bbbef6581a/wheel/fixed.css" />

</head>
<!-- h=iop506 i=2008-11-04 s=legacy(default) t='Wed Nov  5 13:32:41 2008' -->

<body bgcolor="#ffffff" text="#000000" id="styleguide-v2" class="fixed">
<div id="wrapper">



<script language="JavaScript" type="text/javascript">ord = ((this.ad_utils) && (this.ad_utils.ord)) ? this.ad_utils.ord : Math.random()*10000000000000000; </script><!-- begin FLOATING1 -->
<div id="floating1_wrapper">
<script language="JavaScript" type="text/javascript">

//<![CDATA[
document.write('<iframe src="/images/a/ifb/doubleclick/expand.html#imdb.consumer.title/maindetails;tile=1;sz=1x1;p=f1;dcopt=ist;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=' + ord + '?" id="floating1" name="floating1" width="0" height="0" marginwidth="0" marginheight="0" frameborder="0" scrolling="no" allowtransparency="true" onload="ad_utils.resize_iframe(this)">');
if (navigator.userAgent.indexOf("Gecko")==-1)
{document.write('<script language="JavaScript" src="http://ad.doubleclick.net/adj/imdb.consumer.title/maindetails;tile=1;sz=1x1;abr=!ie;p=f1;dcopt=ist;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=' + ord + '?" type="text/javascript"><\/script>');
}
document.write('</iframe>');

//]]>
</script>
<noscript><a href="http://ad.doubleclick.net/jump/imdb.consumer.title/maindetails;tile=1;sz=1x1;p=f1;dcopt=ist;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=427710139430?" target="_blank"><img src="http://ad.doubleclick.net/ad/imdb.consumer.title/maindetails;tile=1;sz=1x1;p=f1;dcopt=ist;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=427710139430?"  border="0" alt="advertisement" /></a></noscript>

</div>
<!-- End FLOATING1 -->



<div id="root">
<layer name="root">

<div id="nb15">
 <div id="nb15supertab">


<!-- begin TOP_AD -->
<div id="top_ad_wrapper">
<script language="JavaScript" type="text/javascript">

//<![CDATA[
document.write('<iframe src="/images/a/ifb/doubleclick/expand.html#imdb.consumer.title/maindetails;tile=2;sz=468x60,728x90,1008x150;p=t;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=' + ord + '?" id="top_ad" name="top_ad" width="0" height="80" marginwidth="0" marginheight="0" frameborder="0" scrolling="no" allowtransparency="true" onload="ad_utils.resize_iframe(this)">');
if (navigator.userAgent.indexOf("Gecko")==-1)
{document.write('<script language="JavaScript" src="http://ad.doubleclick.net/adj/imdb.consumer.title/maindetails;tile=2;sz=468x60,728x90,1008x150;abr=!ie;p=t;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=' + ord + '?" type="text/javascript"><\/script>');
}
document.write('</iframe>');

//]]>
</script>
<noscript><a href="http://ad.doubleclick.net/jump/imdb.consumer.title/maindetails;tile=2;sz=468x60,728x90,1008x150;p=t;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=427710139430?" target="_blank"><img src="http://ad.doubleclick.net/ad/imdb.consumer.title/maindetails;tile=2;sz=468x60,728x90,1008x150;p=t;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=427710139430?"  border="0" alt="advertisement" /></a></noscript>

</div>
<!-- End TOP_AD --></div>
  <div id="nb15home">
   <a href="/" onClick="(new Image()).src='/rg/nav-home/navbar/images/b.gif?link=/';"><img src="http://i.media-imdb.com/images/nb15/logo2.gif" alt="Home" 
   title="The Internet Movie Database" border="0" width="177" height="78"></a>
  </div>
 <div id="nb15botbg">
 
  <div id="nb15tabs">
   <a id="nb15nowplaying" href="/nowplaying/" onClick="(new Image()).src='/rg/nav-nowplaying/navbar/images/b.gif?link=/nowplaying/';"><i>Now Playing</i></a>
   <a id="nb15news" href="/news/" onClick="(new Image()).src='/rg/nav-news/navbar/images/b.gif?link=/news/';"><i>Movie/TV News</i></a>
   <a id="nb15mm" href="/mymovies/list" onClick="(new Image()).src='/rg/nav-mymovies/navbar/images/b.gif?link=/mymovies/list';"><i>My Movies</i></a>
   <a id="nb15dvd" href="/sections/dvd/" onClick="(new Image()).src='/rg/nav-video/navbar/images/b.gif?link=/sections/dvd/';"><i>DVD New Releases</i></a>
   <a id="nb15imdbtv" href="/sections/tv/" onClick="(new Image()).src='/rg/nav-imdbtv/navbar/images/b.gif?link=/sections/tv/';"><i>IMDbTV</i></a>
   <a id="nb15boards" href="/boards/" onClick="(new Image()).src='/rg/nav-boards/navbar/images/b.gif?link=/boards/';"><i>Message Boards</i></a>
   <a id="nb15showtimes" href="/showtimes/" onClick="(new Image()).src='/rg/nav-showtimes/navbar/images/b.gif?link=/showtimes/';"><i>Showtimes &amp; Tickets</i></a>
   <a id="nb15pro" href="http://pro.imdb.com/r/imdb-nav/" onClick="(new Image()).src='/rg/nav-pro/navbar/images/b.gif?link=http://pro.imdb.com/r/imdb-nav/';"><i>IMDbPro</i></a>
   <a id="nb15resume" href="http://resume.imdb.com/" onClick="(new Image()).src='/rg/nav-resume/navbar/images/b.gif?link=http://resume.imdb.com/';"><i>IMDb Resume</i></a>
  </div>
 
  <div id="nb15topbg">
   <div id="nb15iesux">
    <div id="nb15personal">

     &nbsp;<span><a href="/register/login" onClick="(new Image()).src='/rg/sub-login/navbar/images/b.gif?link=/register/login';">Login</a> | 
     <a href="/register/?why=personalize" onClick="(new Image()).src='/rg/sub-register/navbar/images/b.gif?link=/register/?why=personalize';">Register</a></span>

    </div>
   </div>
  </div>
  <div id="nb15sub">
   <div>
   <a href="/" onClick="(new Image()).src='/rg/sub-home/navbar/images/b.gif?link=/';">Home</a> |
   
    <a href="/chart/" onClick="(new Image()).src='/rg/sub-top/navbar/images/b.gif?link=/chart/';">Top&nbsp;Movies</a> |
    <a href="/sections/gallery/" onClick="(new Image()).src='/rg/sub-gallery/navbar/images/b.gif?link=/sections/gallery/';">Photos</a> |
    <a href="/indie/" onClick="(new Image()).src='/rg/sub-indie/navbar/images/b.gif?link=/indie/';">Independent&nbsp;Film</a> |
    <a href="/sections/games/" onClick="(new Image()).src='/rg/sub-gamebase/navbar/images/b.gif?link=/sections/games/';">GameBase</a> |
    <a href="/Browse/" onClick="(new Image()).src='/rg/sub-browse/navbar/images/b.gif?link=/Browse/';">Browse</a> |
   
   <a href="/help/" onClick="(new Image()).src='/rg/sub-help/navbar/images/b.gif?link=/help/';">Help</a>
   </div>
  </div>
  <div id="nb15search"> 
   <span class=search><a href="/search" onClick="(new Image()).src='/rg/search-img/navbar/images/b.gif?link=/search';">search</a></span>
   <form method="get" action="/find" name="find">
    <select name="s">
     <option value="all" selected>All</option>
     <option value="tt">Titles</option>
     <option value="ep">TV Episodes</option>
     
      <option>My Movies</option>
     
     <option value="nm">Names</option>
     <option value="co">Companies</option>
     
      <option value="kw">Keywords</option>
     
     
     <option value="char">Characters</option>
     
      <option>Quotes</option>
      <option>Bios</option>
      <option>Plots</option>
    
    </select>
   <input name="q" size="28" value="">
    
    
    <input type="image"  id="nb15go_image"  src="http://i.media-imdb.com/images/intl/en/go.gif" alt="go" value="go" title="go">
    
    
    <span id="nb15searchlinks">
    
     <a href="/search" onClick="(new Image()).src='/rg/search-more/navbar/images/b.gif?link=/search';">more</a> | 
     <a href="/help/show_leaf?searchtips" onClick="(new Image()).src='/rg/search-tips/navbar/images/b.gif?link=/help/show_leaf?searchtips';">tips</a>
    
    </span>
   </form>
  </div>
 </div>
</div>



<!-- begin NAVSTRIP -->
<div id="navstrip_wrapper">
<script language="JavaScript" type="text/javascript">

//<![CDATA[
document.write('<iframe src="/images/a/ifb/doubleclick/expand.html#imdb.consumer.title/maindetails;tile=3;sz=1008x40;p=ns;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=' + ord + '?" id="navstrip" name="navstrip" width="0" height="0" marginwidth="0" marginheight="0" frameborder="0" scrolling="no" allowtransparency="true" onload="ad_utils.resize_iframe(this)">');
if (navigator.userAgent.indexOf("Gecko")==-1)
{document.write('<script language="JavaScript" src="http://ad.doubleclick.net/adj/imdb.consumer.title/maindetails;tile=3;sz=1008x40;abr=!ie;p=ns;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=' + ord + '?" type="text/javascript"><\/script>');
}
document.write('</iframe>');

//]]>
</script>
<noscript><a href="http://ad.doubleclick.net/jump/imdb.consumer.title/maindetails;tile=3;sz=1008x40;p=ns;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=427710139430?" target="_blank"><img src="http://ad.doubleclick.net/ad/imdb.consumer.title/maindetails;tile=3;sz=1008x40;p=ns;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=427710139430?"  border="0" alt="advertisement" /></a></noscript>

</div>
<!-- End NAVSTRIP -->
<div id="pagecontent">

<div id="tn15" class="maindetails">
<div id="tn15crumbs">
<a href="/">IMDb</a> &gt;
<b>The Patriot (2000)</b>
</div>
<div id="tn15lhs">

<div class="photo">
<a name="poster" href="/rg/action-box-title/primary-photo/media/rm1069653504/tt0187393" title="The Patriot"><img border="0" alt="The Patriot" title="The Patriot" src="http://ia.media-imdb.com/images/M/MV5BMTk1MTgyNTE2M15BMl5BanBnXkFtZTYwNTE1MDI5._V1._SX96_SY140_.jpg" /></a>
</div>

<div id="action-box" class="action-box">
<a class="linkasbutton-primary disabled" >Watch It</a>

<p><a href="/rg/action-box-title/watch-at-amazon/r/50403000000050a0904747031383733393330000001036a08046f677e6c6f6164600000010d6a02064940000001037a0104700000010f5a0403786f6070000001047">Watch it at Amazon</a></p>

<p><img src="/images/wheel/or-graphic.png" /></p>

<a class="linkasbutton-secondary" href="/rg/action-box-title/buy-at-amazon/r/50403000000050a0904747031383733393330000001036a03016c6c600000010d6a02064940000001037a0104700000010f5a0403786f6070000001047">Buy it at Amazon</a>
<hr />
<a class="linkasbutton-secondary" href="/rg/action-box-title/pro-link/http://pro.imdb.com/title/tt0187393/">More at IMDb Pro</a>

<a class="linkasbutton-secondary" href="/rg/action-box-title/boards-link/title/tt0187393/board">Discuss in Boards</a>

<a class="linkasbutton-secondary" href="/rg/action-box-title/add-to-my-movies/mymovies/list?pending&amp;add=0187393">Add to My Movies</a>
<a class="linkasbutton-secondary" href="/rg/action-box-title/update-data/updates?auto=legacy/title/tt0187393/">Update Data</a>
</div>

<h6 style="margin-top: 4px">Quicklinks</h6><form><select id="quicklinks_select" onchange="document.location = this.options[this.selectedIndex].value">
<option value="maindetails" selected>main details</option><option value="combined">combined details</option><option value="fullcredits">full cast and crew</option><option value="companycredits">company credits</option><option value="tvschedule">tv schedule</option><option value="usercomments">user comments</option><option value="externalreviews">external reviews</option><option value="newsgroupreviews">newsgroup reviews</option><option value="awards">awards</option><option value="ratings">user ratings</option><option value="parentalguide">parents guide</option><option value="recommendations">recommendations</option><option value="board">message board</option><option value="plotsummary">plot summary</option><option value="synopsis">plot synopsis</option><option value="keywords">plot keywords</option><option value="quotes">memorable quotes</option><option value="trivia">trivia</option><option value="goofs">goofs</option><option value="soundtrack">soundtrack listing</option><option value="alternateversions">alternate versions</option><option value="movieconnections">movie connections</option><option value="sales">merchandising links</option><option value="business">box office/business</option><option value="releaseinfo">release dates</option><option value="locations">filming locations</option><option value="technical">technical specs</option><option value="dvd">DVD details</option><option value="literature">literature listings</option><option value="news">NewsDesk</option><option value="taglines">taglines</option><option value="trailers">trailers and videos</option><option value="posters">posters</option><option value="photogallery">photo gallery</option><option value="miscsites">miscellaneous</option><option value="photosites">photographs</option><option value="soundsites">sound clips</option>
</select></form>
<h6>Top Links</h6>
<a onClick="(new Image()).src='/rg/title-top-links/trailers/images/b.gif?link=/title/tt0187393/trailers';" href="/title/tt0187393/trailers" class="link">trailers and videos</a><a onClick="(new Image()).src='/rg/title-top-links/fullcredits/images/b.gif?link=/title/tt0187393/fullcredits';" href="/title/tt0187393/fullcredits" class="link">full cast and crew</a><a onClick="(new Image()).src='/rg/title-top-links/trivia/images/b.gif?link=/title/tt0187393/trivia';" href="/title/tt0187393/trivia" class="link">trivia</a><a onClick="(new Image()).src='/rg/title-top-links/officialsites/images/b.gif?link=/title/tt0187393/officialsites';" href="/title/tt0187393/officialsites" class="link empty">official sites</a><a onClick="(new Image()).src='/rg/title-top-links/quotes/images/b.gif?link=/title/tt0187393/quotes';" href="/title/tt0187393/quotes" class="link">memorable quotes</a>
<h6>Overview</h6>
<a href="maindetails" class="link selected">main details</a><a href="combined" class="link">combined details</a><a href="fullcredits" class="link">full cast and crew</a><a href="companycredits" class="link">company credits</a><a href="tvschedule" class="link">tv schedule</a>
<h6>Awards & Reviews</h6>
<a href="usercomments" class="link">user comments</a><a href="externalreviews" class="link">external reviews</a><a href="newsgroupreviews" class="link">newsgroup reviews</a><a href="awards" class="link">awards</a><a href="ratings" class="link">user ratings</a><a href="parentalguide" class="link">parents guide</a><a href="recommendations" class="link">recommendations</a><a href="board" class="link">message board</a>
<h6>Plot & Quotes</h6>
<a href="plotsummary" class="link">plot summary</a><a href="synopsis" class="link">plot synopsis</a><a href="keywords" class="link">plot keywords</a><a href="amazon" class="link empty">Amazon.com summary</a><a href="quotes" class="link">memorable quotes</a>
<h6>Fun Stuff</h6>
<a href="trivia" class="link">trivia</a><a href="goofs" class="link">goofs</a><a href="soundtrack" class="link">soundtrack listing</a><a href="crazycredits" class="link empty">crazy credits</a><a href="alternateversions" class="link">alternate versions</a><a href="movieconnections" class="link">movie connections</a><a href="faq" class="link empty">FAQ</a>
<h6>Other Info</h6>

  <a href="sales" class="link">merchandising links</a><a href="business" class="link">box office/business</a><a href="releaseinfo" class="link">release dates</a><a href="locations" class="link">filming locations</a><a href="technical" class="link">technical specs</a><a href="laserdisc" class="link empty">laserdisc details</a><a href="dvd" class="link">DVD details</a><a href="literature" class="link">literature listings</a><a href="news" class="link">NewsDesk</a>
  <h6>Promotional</h6>
  <a href="taglines" class="link">taglines</a>
  <a href="trailers" class="link">trailers and videos</a>
  <a href="posters" class="link">posters</a>
  <a href="photogallery" class="link">photo gallery</a>
  

<h6>External Links</h6>
<a href="cinemashowtimes" class="link empty">showtimes</a><a href="officialsites" class="link empty">official sites</a><a href="miscsites" class="link">miscellaneous</a><a href="photosites" class="link">photographs</a><a href="soundsites" class="link">sound clips</a><a href="videosites" class="link empty">video clips</a>



</div>
<div id="tn15main">

<div id="tn15title">
<h1>The Patriot <span>(<a href="/Sections/Years/2000/">2000</a>) <span class="pro-link"><a href="http://pro.imdb.com/rg/maindetails-title/tconst-pro-header-link/title/tt0187393/">More at IMDb Pro &raquo;</a></span></span></h1>
</div>

<div id="tn15content">
 
 
 

<style type="text/css">

.media_strip_thumbs img {
    margin-right:0.2em;
    border:none;
}

.media_strip_thumbs {
  overflow: hidden;
  height: 90px;
}
.media_strip_thumb img {
  margin-right: 0.2em;
}
.media_strip_thumb {
  float: left; 
  margin-bottom: 50px;
  text-align: right;
  font-family: Tahoma,Verdana,sans-serif;
  font-size: 10pt;
  color:#333333;
}
</style>

<table style="border-collapse:collapse;">
<tr>

<td  class="media_strip_header">
<b>Photos</b>
<span>(<a href="/rg/photos-title/gallery-link/title/tt0187393/mediaindex">see all 209</a> | <a href="/rg/photos-title/slideshow-link/media/rm898144768/tt0187393?slideshow=1">slideshow</a>)</span>
</td>


</tr>
<tr>

<td>
<div class="media_strip_thumbs">
<div class="media_strip_thumb"><a href="/rg/photos-title/summary/media/rm898144768/tt0187393"><img height="90" width="90" src="http://ia.media-imdb.com/images/M/MV5BMTQ0ODk4OTU0OV5BMl5BanBnXkFtZTYwMjM3MTAz._V1._CR64,0,321,321_SS90_.jpg" border="0"></a></div>
<div class="media_strip_thumb"><a href="/rg/photos-title/summary/media/rm3692992512/tt0187393"><img height="90" width="90" src="http://ia.media-imdb.com/images/M/MV5BMTI4ODQwNzc5M15BMl5BanBnXkFtZTYwNzI2OTk2._V1._CR75,0,300,300_SS90_.jpg" border="0"></a></div>
<div class="media_strip_thumb"><a href="/rg/photos-title/summary/media/rm3676215296/tt0187393"><img height="90" width="90" src="http://ia.media-imdb.com/images/M/MV5BMTM0NzQwNDI1MF5BMl5BanBnXkFtZTYwOTI2OTk2._V1._CR0,0,450,450_SS90_.jpg" border="0"></a></div>
<div class="media_strip_thumb"><a href="/rg/photos-title/summary/media/rm3659438080/tt0187393"><img height="90" width="90" src="http://ia.media-imdb.com/images/M/MV5BMjA2NjI3ODg0NV5BMl5BanBnXkFtZTYwMTM2OTk2._V1._CR75,0,300,300_SS90_.jpg" border="0"></a></div>
<div class="media_strip_thumb"><a href="/rg/photos-title/summary/media/rm3642660864/tt0187393"><img height="90" width="90" src="http://ia.media-imdb.com/images/M/MV5BMTMxOTc4NjkwMl5BMl5BanBnXkFtZTYwMzM2OTk2._V1._CR75,0,300,300_SS90_.jpg" border="0"></a></div>
<div class="media_strip_thumb"><a href="/rg/photos-title/summary/media/rm3625883648/tt0187393"><img height="90" width="90" src="http://ia.media-imdb.com/images/M/MV5BMTM2MjEzNzM5Nl5BMl5BanBnXkFtZTYwNTM2OTk2._V1._CR0,0,450,450_SS90_.jpg" border="0"></a></div>
<div class="media_strip_thumb"><a href="/rg/photos-title/summary/media/rm656381952/tt0187393"><img height="90" width="90" src="http://ia.media-imdb.com/images/M/MV5BMTQzNjQzNjQ2OV5BMl5BanBnXkFtZTYwNzM2OTk2._V1._CR75,0,300,300_SS90_.jpg" border="0"></a></div>
<div class="media_strip_thumb"><a href="/rg/photos-title/summary/media/rm639604736/tt0187393"><img height="90" width="90" src="http://ia.media-imdb.com/images/M/MV5BMTY1MDA1MjA3M15BMl5BanBnXkFtZTYwMDQ2OTk2._V1._CR0,0,450,450_SS90_.jpg" border="0"></a></div>
<div class="media_strip_thumb"><a href="/rg/photos-title/summary/media/rm622827520/tt0187393"><img height="90" width="90" src="http://ia.media-imdb.com/images/M/MV5BMTI2NTYwNzMwMF5BMl5BanBnXkFtZTYwMjQ2OTk2._V1._CR0,0,450,450_SS90_.jpg" border="0"></a></div>
<div class="media_strip_thumb"><a href="/rg/photos-title/summary/media/rm606050304/tt0187393"><img height="90" width="90" src="http://ia.media-imdb.com/images/M/MV5BMTQ2MTU2NzA4OF5BMl5BanBnXkFtZTYwMzQ2OTk2._V1._CR0,0,450,450_SS90_.jpg" border="0"></a></div>
</div>
</td>


</tr>
</table>



<hr/>

<div id="tn15adrhs">



<!-- begin TOP_RHS -->
<div id="top_rhs_wrapper">
<script language="JavaScript" type="text/javascript">

//<![CDATA[
document.write('<iframe src="/images/a/ifb/doubleclick/expand.html#imdb.consumer.title/maindetails;tile=4;sz=300x250,300x600,160x600,171x600;p=tr;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=' + ord + '?" id="top_rhs" name="top_rhs" width="0" height="0" marginwidth="0" marginheight="0" frameborder="0" scrolling="no" allowtransparency="true" onload="ad_utils.resize_iframe(this)">');
if (navigator.userAgent.indexOf("Gecko")==-1)
{document.write('<script language="JavaScript" src="http://ad.doubleclick.net/adj/imdb.consumer.title/maindetails;tile=4;sz=300x250,300x600,160x600,171x600;abr=!ie;p=tr;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=' + ord + '?" type="text/javascript"><\/script>');
}
document.write('</iframe>');

//]]>
</script>
<noscript><a href="http://ad.doubleclick.net/jump/imdb.consumer.title/maindetails;tile=4;sz=300x250,300x600,160x600,171x600;p=tr;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=427710139430?" target="_blank"><img src="http://ad.doubleclick.net/ad/imdb.consumer.title/maindetails;tile=4;sz=300x250,300x600,160x600,171x600;p=tr;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=427710139430?"  border="0" alt="advertisement" /></a></noscript>

</div>
<!-- End TOP_RHS --><div id="top_rhs_after" class="after_ad hidden">advertisement</div>



</div>



<!-- begin TOP_CENTER -->
<div id="top_center_wrapper">
<script language="JavaScript" type="text/javascript">

//<![CDATA[
document.write('<iframe src="/images/a/ifb/doubleclick/expand.html#imdb.consumer.title/maindetails;tile=5;sz=450x35;p=tc;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=' + ord + '?" id="top_center" name="top_center" width="0" height="0" marginwidth="0" marginheight="0" frameborder="0" scrolling="no" allowtransparency="true" onload="ad_utils.resize_iframe(this)">');
if (navigator.userAgent.indexOf("Gecko")==-1)
{document.write('<script language="JavaScript" src="http://ad.doubleclick.net/adj/imdb.consumer.title/maindetails;tile=5;sz=450x35;abr=!ie;p=tc;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=' + ord + '?" type="text/javascript"><\/script>');
}
document.write('</iframe>');

//]]>
</script>
<noscript><a href="http://ad.doubleclick.net/jump/imdb.consumer.title/maindetails;tile=5;sz=450x35;p=tc;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=427710139430?" target="_blank"><img src="http://ad.doubleclick.net/ad/imdb.consumer.title/maindetails;tile=5;sz=450x35;p=tc;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=427710139430?"  border="0" alt="advertisement" /></a></noscript>

</div>
<!-- End TOP_CENTER --><div id="top_center_after" class="after_ad hidden"><div></div></div>
<h3>Overview</h3>

<style type="text/css">
#tn15rating,
#tn15rating.unrated {
    overflow:visible;
    width:360px;
}
#tn15rating .usr {
    z-index: 10;
}
#tn15rating .general {
    z-index: 5;
}
#tn15rating.two .usr {
    left:0px;
    top:40px;
    height:3em;
}
#tn15rating.two .general {
    top: -40px;
}
#tn15rating.guest .usr {
    top:30px !important;
}
#tn15rating.one {
    height:30px;
}
#tn15rating.one .general {
    top:-20px;
}
#tn15rating.one .usr {
    width:200px;
}
#tn15rating.one .usr h5 {
    display:none;
}
.starbar .outer {
    float:left;
    position:relative;
}
.meta {
    left:210px;
    position:absolute;
    top:0px;
}
#tn15rating .rating {
    width:360px;
}
.starbar small a {
    display:inline ;
    height:auto;
    left:0pt;
    position:relative;
    top:0pt;
}
#tn15rating .message .extra a {
    position:relative;
    display:inline;
}
#tn15rating .message .extra a.del {
    right:auto;
}
#tn15rating .bottom div.left {
    top:20px;
}
</style>
<div class="info">
<h5>User Rating:</h5>
<div id="tn15rating" class="two guest">
<div class="usr rating">

</div>
<div class="general rating">
<div class="starbar static">
    <div class="outer">
        <div class="inner" style="width: 136px"></div>
    </div>
</div>
<div class="meta">
<b>6.8/10</b> 

&nbsp;&nbsp;<a href="ratings" class="tn15more">61,979 votes</a>
</div>

<div class="bottom">

<!-- <a class="tn15more" href="ratings">more</a> -->

</div>

</div>
</div>
</div> <!-- end info -->

<div class="info">
<h5>Director:</h5>
<a href="/name/nm0000386/">Roland Emmerich</a><br/>
</div>

<div class="info">
<h5>Writer <a href="/wga">(WGA)</a>:</h5>
<a href="/name/nm0734441/">Robert Rodat</a> (written by)<br/>
</div>

<div class="info">
<h5>Release Date:</h5> 
28 July 2000 (Finland)
 <a class="tn15more inline" href="/title/tt0187393/releaseinfo" onClick="(new Image()).src='/rg/title-tease/releasedates/images/b.gif?link=/title/tt0187393/releaseinfo';">more</a>
</div>

<div class="info">
<h5>Genre:</h5>
<a href="/Sections/Genres/Action/">Action</a> | <a href="/Sections/Genres/Drama/">Drama</a> | <a href="/Sections/Genres/War/">War</a> <a class="tn15more inline" href="/title/tt0187393/keywords" onClick="(new Image()).src='/rg/title-tease/keywords/images/b.gif?link=/title/tt0187393/keywords';">more</a>
</div>

<div class="info">
<h5>Tagline:</h5>
What would you do if they destroyed your home, threatened your family. Where would you draw the line? <a class="tn15more inline" href="/title/tt0187393/taglines" onClick="(new Image()).src='/rg/title-tease/taglines/images/b.gif?link=/title/tt0187393/taglines';">more</a>
</div>

<div class="info">
<h5>Plot:</h5>
Peaceful farmer Benjamin Martin is driven to lead the Colonial Militia during the American Revolution when a sadistic British officer murders his son. <a class="tn15more inline" href="/title/tt0187393/plotsummary" onClick="(new Image()).src='/rg/title-tease/plotsummary/images/b.gif?link=/title/tt0187393/plotsummary';">full summary</a> | <a class="tn15more inline" href="synopsis">full synopsis</a>
</div>

<div class="info">
<h5>Plot Keywords:</h5>
<div id="tn15plotkeywords" style="display:inline;"><span>

<a href="/keyword/colonial-america/">Colonial&#160;America</a>
 | 
<a href="/keyword/tears/">Tears</a>
 | 
<a href="/keyword/violence/">Violence</a>
 | 
<a href="/keyword/murder/">Murder</a>
 | 
<a href="/keyword/man-in-uniform/">Man&#160;In&#160;Uniform</a>

</span></div>

<a class="tn15more inline" href="/title/tt0187393/keywords" onClick="(new Image()).src='/rg/title-tease/keywords/images/b.gif?link=/title/tt0187393/keywords';">more</a>

</div>

<script type="text/javascript">
var k = document.getElementById("tn15plotkeywords");
k.className = "keyword-spoiler";
k.onmouseover = function() {if (!window.hasVoted) this.className += ' hover';};
k.onmouseout=   function() {if (!window.hasVoted) this.className='keyword-spoiler';}
</script>

<div class="info">
<h5>Awards:</h5> 
Nominated for 3 Oscars.
 Another 8 wins
&amp;
17 nominations
<a class="tn15more inline" href="/title/tt0187393/awards" onClick="(new Image()).src='/rg/title-tease/awards/images/b.gif?link=/title/tt0187393/awards';">more</a>
</div>
<div class="info">
<h5>NewsDesk<span>:</span><br/>
<small>(<a onClick="(new Image()).src='/rg/maindetails-count/newsdesk/images/b.gif?link=%2Ftitle%2Ftt0187393%2Fnews';" href="/title/tt0187393/news">49 articles</a>)</small>
</h5>
<strong><a onClick="(new Image()).src='/rg/maindetails-headline/newsdesk/images/b.gif?link=%2Ftitle%2Ftt0187393%2Fnews%23ni0580507';" href="/title/tt0187393/news#ni0580507">Warner to develop live-action &lsquo;Tom Thumb&rsquo;</a></strong> <small><br />&nbsp;(From <a onClick="(new Image()).src='/rg/maindetails-source/newsdesk/images/b.gif?link=%2Fnews%2Fns0000035%2F';" href="/news/ns0000035/">screeninglog</a>. 8 October 2008, 2:12 PM, PDT)</small>
<br/>
<strong><a onClick="(new Image()).src='/rg/maindetails-headline/newsdesk/images/b.gif?link=%2Ftitle%2Ftt0187393%2Fnews%23ni0181778';" href="/title/tt0187393/news#ni0181778">Gibson: &#39;I&#39;m A Manic Depressive&#39;</a></strong> <small><br />&nbsp;(From <a onClick="(new Image()).src='/rg/maindetails-source/newsdesk/images/b.gif?link=%2Fnews%2Fns0000002%2F';" href="/news/ns0000002/">WENN</a>. 15 May 2008, 9:14 AM, PDT)</small>
<br/>
<div style="width:1px;height:0.5em;"></div></div>

<div class="info">
<h5>User Comments:</h5>
Heroes and Villains
<a class="tn15more inline" href="#comment">more</a>
</div>

<hr/>
<div class="headerinline"><h3>Cast</h3>&nbsp;<small style="position: relative; bottom: 1px">(Cast overview, first billed only)</small></div><div class="info"><table class="cast">  <tr class="odd"><td class="hs"><a href="/name/nm0000154/" onClick="(new Image()).src='/rg/title-tease/tinyhead/images/b.gif?link=/name/nm0000154/';"><img src="http://ia.media-imdb.com/images/M/MV5BNzA1MDkyMTM0NV5BMl5BanBnXkFtZTcwNjQxNjQxMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a><br></td><td class="nm"><a href="/name/nm0000154/">Mel Gibson</a></td><td class="ddd"> ... </td><td class="char"><a href="/character/ch0006309/">Benjamin Martin</a></td></tr><tr class="even"><td class="hs"><a href="/name/nm0005132/" onClick="(new Image()).src='/rg/title-tease/tinyhead/images/b.gif?link=/name/nm0005132/';"><img src="http://ia.media-imdb.com/images/M/MV5BMTQyNDMzNjA0M15BMl5BanBnXkFtZTcwOTg5NjYyMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a><br></td><td class="nm"><a href="/name/nm0005132/">Heath Ledger</a></td><td class="ddd"> ... </td><td class="char"><a href="/character/ch0006307/">Gabriel Martin</a></td></tr><tr class="odd"><td class="hs"><a href="/name/nm0000613/" onClick="(new Image()).src='/rg/title-tease/tinyhead/images/b.gif?link=/name/nm0000613/';"><img src="http://ia.media-imdb.com/images/M/MV5BMjA4NzcyMTc1N15BMl5BanBnXkFtZTcwOTI0NjQxMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a><br></td><td class="nm"><a href="/name/nm0000613/">Joely Richardson</a></td><td class="ddd"> ... </td><td class="char"><a href="/character/ch0006312/">Charlotte Selton</a></td></tr><tr class="even"><td class="hs"><a href="/name/nm0005042/" onClick="(new Image()).src='/rg/title-tease/tinyhead/images/b.gif?link=/name/nm0005042/';"><img src="http://ia.media-imdb.com/images/M/MV5BNTkzMTYzNjc1OF5BMl5BanBnXkFtZTcwMTQ3OTYyMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a><br></td><td class="nm"><a href="/name/nm0005042/">Jason Isaacs</a></td><td class="ddd"> ... </td><td class="char"><a href="/character/ch0006311/">Col. William Tavington</a></td></tr><tr class="odd"><td class="hs"><a href="/name/nm0177933/" onClick="(new Image()).src='/rg/title-tease/tinyhead/images/b.gif?link=/name/nm0177933/';"><img src="http://ia.media-imdb.com/images/M/MV5BMTkxNDQ4NDEyMV5BMl5BanBnXkFtZTcwNTMzODQxMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a><br></td><td class="nm"><a href="/name/nm0177933/">Chris Cooper</a></td><td class="ddd"> ... </td><td class="char"><a href="/character/ch0006310/">Col. Harry Burwell</a></td></tr><tr class="even"><td class="hs"><a href="/name/nm0001409/" onClick="(new Image()).src='/rg/title-tease/tinyhead/images/b.gif?link=/name/nm0001409/';"><img src="http://ia.media-imdb.com/images/M/MV5BOTIwNjE4MjIwOV5BMl5BanBnXkFtZTcwNjY0NjQxMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a><br></td><td class="nm"><a href="/name/nm0001409/">Tch&#233;ky Karyo</a></td><td class="ddd"> ... </td><td class="char"><a href="/character/ch0006319/">Jean Villeneuve</a></td></tr><tr class="odd"><td class="hs"><a href="/name/nm0041281/" onClick="(new Image()).src='/rg/title-tease/tinyhead/images/b.gif?link=/name/nm0041281/';"><img src="http://ia.media-imdb.com/images/M/MV5BMTUxNTY1NDU0NV5BMl5BanBnXkFtZTcwMDUyMTkyMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a><br></td><td class="nm"><a href="/name/nm0041281/">Rene Auberjonois</a></td><td class="ddd"> ... </td><td class="char"><a href="/character/ch0006316/">Reverend Oliver</a></td></tr><tr class="even"><td class="hs"><a href="/name/nm0004773/" onClick="(new Image()).src='/rg/title-tease/tinyhead/images/b.gif?link=/name/nm0004773/';"><img src="http://ia.media-imdb.com/images/M/MV5BMTIwNjYxNzYzNV5BMl5BanBnXkFtZTcwMDcyMDkyMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a><br></td><td class="nm"><a href="/name/nm0004773/">Lisa Brenner</a></td><td class="ddd"> ... </td><td class="char"><a href="/character/ch0006320/">Anne Howard</a></td></tr><tr class="odd"><td class="hs"><a href="/name/nm0929489/" onClick="(new Image()).src='/rg/title-tease/tinyhead/images/b.gif?link=/name/nm0929489/';"><img src="http://ia.media-imdb.com/images/M/MV5BMTk5MjAzMDExN15BMl5BanBnXkFtZTcwMTM3NDAyMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a><br></td><td class="nm"><a href="/name/nm0929489/">Tom Wilkinson</a></td><td class="ddd"> ... </td><td class="char"><a href="/character/ch0006314/">Gen. Lord Charles Cornwallis</a></td></tr><tr class="even"><td class="hs"><a href="/name/nm0006610/" onClick="(new Image()).src='/rg/title-tease/tinyhead/images/b.gif?link=/name/nm0006610/';"><img src="http://ia.media-imdb.com/images/M/MV5BMTY2MjQwMzk3Nl5BMl5BanBnXkFtZTcwMzk5NzQxMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a><br></td><td class="nm"><a href="/name/nm0006610/">Donal Logue</a></td><td class="ddd"> ... </td><td class="char"><a href="/character/ch0006315/">Dan Scott</a></td></tr><tr class="odd"><td class="hs"><a href="/name/nm0728132/" onClick="(new Image()).src='/rg/title-tease/tinyhead/images/b.gif?link=/name/nm0728132/';"><img src="http://ia.media-imdb.com/images/M/MV5BMTg4MzE3NDA5M15BMl5BanBnXkFtZTcwMDc4MDEzMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a><br></td><td class="nm"><a href="/name/nm0728132/">Leon Rippy</a></td><td class="ddd"> ... </td><td class="char"><a href="/character/ch0006317/">John Billings</a></td></tr><tr class="even"><td class="hs"><a href="/name/nm0000284/" onClick="(new Image()).src='/rg/title-tease/tinyhead/images/b.gif?link=/name/nm0000284/';"><img src="http://ia.media-imdb.com/images/M/MV5BMTMyODY4ODQ5MF5BMl5BanBnXkFtZTcwNDgwMzgyMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a><br></td><td class="nm"><a href="/name/nm0000284/">Adam Baldwin</a></td><td class="ddd"> ... </td><td class="char"><a href="/character/ch0006308/">Capt. Wilkins</a></td></tr><tr class="odd"><td class="hs"><a href="/name/nm0428326/" onClick="(new Image()).src='/rg/title-tease/tinyhead/images/b.gif?link=/name/nm0428326/';"><img src="http://ia.media-imdb.com/images/M/MV5BMTA2MjAzNTM2MjBeQTJeQWpwZ15BbWU3MDUwODYyMzE@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a><br></td><td class="nm"><a href="/name/nm0428326/">Jay Arlen Jones</a></td><td class="ddd"> ... </td><td class="char">Occam</td></tr><tr class="even"><td class="hs"><a href="/name/nm0896649/" onClick="(new Image()).src='/rg/title-tease/tinyhead/images/b.gif?link=/name/nm0896649/';"><img src="http://ia.media-imdb.com/images/M/MV5BMTIxMzk5MDg1MV5BMl5BanBnXkFtZTcwMjA5NDcyMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a><br></td><td class="nm"><a href="/name/nm0896649/">Joey D. Vieira</a></td><td class="ddd"> ... </td><td class="char"><a href="/character/ch0006321/">Peter Howard</a></td></tr><tr class="odd"><td class="hs"><a href="/name/nm0808376/" onClick="(new Image()).src='/rg/title-tease/tinyhead/images/b.gif?link=/name/nm0808376/';"><img src="http://ia.media-imdb.com/images/M/MV5BMTUxODM1NTI0OF5BMl5BanBnXkFtZTcwNzk1ODkyMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a><br></td><td class="nm"><a href="/name/nm0808376/">Gregory Smith</a></td><td class="ddd"> ... </td><td class="char"><a href="/character/ch0006313/">Thomas Martin</a></td></tr></table><a class="tn15more" href="fullcredits#cast">more</a></div>  <div><form action="/character/create" method="post"><input type="hidden" name="title" value="tt0187393">Create a character page for:&#32;<select name="name" onchange="if (this.options[this.selectedIndex].value == '...') document.location='fullcredits#cast'"><option>Occam</option><option disabled="disabled">-----------</option><option value="...">more...</option></select>&#32;<input style="font: Tahoma, Verdana, sans-serif; font-size: 8pt; font-weight: bold; background-color: #eeeeee; border-color: #ccccee; color: black" type="submit" value="Create &raquo;">&#32;<a target="_blank" href="/help/show_leaf?createchar"><img src="http://i.media-imdb.com/images/help13x10.gif" width="13" height="10" border="0" alt="?"></a></form></div>


<!-- sid: test01-channel : MIDDLE_CENTER -->

<script type="text/javascript">
if (typeof afc_data == "undefined") {
    afc_data = new Object();
}

afc_data["MIDDLE_CENTER"] = { channel:  "test01-channel",
                       title:    "People Viewing This Page May Also Be Interested In These Sponsored Links",
                       help:     "What's This?"
                     };
</script>

<div id="sponsored_links_afc_div_MIDDLE_CENTER" name="sponsored_links_afc_div_MIDDLE_CENTER"></div>

<iframe id="sponsored_links_afc_iframe_MIDDLE_CENTER" width="0" height="0" scrolling="no" frameborder="0"
        allowtransparency="true" marginheight="0" marginwidth="0"
        name="sponsored_links_afc_iframe"
        src="/images/a/ifb/google_afc.html#key:MIDDLE_CENTER">
</iframe>

<hr />

<h3>Additional Details</h3>

<div class="info">

  <h5>Also Known As:</h5>Patriot, Der (Germany)&#32; <br>
  
  
<a class="tn15more" href="/title/tt0187393/releaseinfo#akas" onClick="(new Image()).src='/rg/title-tease/akas/images/b.gif?link=/title/tt0187393/releaseinfo#akas';">more</a>

</div>

<div class="info">
<h5><a href="/mpaa">MPAA</a>:</h5> 
Rated R for strong war violence.
</div>

<div class="info">
<h5>Parents Guide:</h5>
<a href="parentalguide">View content advisory for parents</a>
</div>

<div class="info">
<h5>Runtime:</h5>
165 min  | 175 min (extended version)
</div>

<div class="info">
<h5>Country:</h5>

<a href="/Sections/Countries/Germany/">
Germany</a>
 | 
<a href="/Sections/Countries/USA/">
USA</a>

</div>

<div class="info">
<h5>Language:</h5>

<a href="/Sections/Languages/English/">
English</a>

</div>

<div class="info">
<h5>Color:</h5>

<a href="/List?color-info=Color&&heading=13;Color">
Color</a> <i>(Technicolor)</i>
</div>

<div class="info">
<h5>Aspect Ratio:</h5>
2.35 : 1 <a class="tn15more inline" href="/title/tt0187393/technical" onClick="(new Image()).src='/rg/title-tease/aspect/images/b.gif?link=/title/tt0187393/technical';">more</a>
</div>

<div class="info">
<h5>Sound Mix:</h5>

<a href="/List?sound-mix=DTS&&heading=15;DTS">
DTS</a>  | 
<a href="/List?sound-mix=Dolby%20Digital&&heading=15;Dolby%20Digital">
Dolby Digital</a>  | 
<a href="/List?sound-mix=SDDS&&heading=15;SDDS">
SDDS</a> 
</div>

<div class="info">
<h5>Certification:</h5>

<a href="/List?certificates=USA:Unrated&&heading=14;USA:Unrated">
USA:Unrated</a> <i>(extended version)</i> | 
<a href="/List?certificates=Iceland:16&&heading=14;Iceland:16">
Iceland:16</a>  | 
<a href="/List?certificates=Malaysia:U&&heading=14;Malaysia:U">
Malaysia:U</a>  | 
<a href="/List?certificates=Australia:MA&&heading=14;Australia:MA">
Australia:MA</a>  | 
<a href="/List?certificates=Canada:14A&&heading=14;Canada:14A">
Canada:14A</a>  | 
<a href="/List?certificates=Denmark:15&&heading=14;Denmark:15">
Denmark:15</a>  | 
<a href="/List?certificates=Finland:K-14&&heading=14;Finland:K-14">
Finland:K-14</a>  | 
<a href="/List?certificates=France:U&&heading=14;France:U">
France:U</a>  | 
<a href="/List?certificates=Germany:16&&heading=14;Germany:16">
Germany:16</a>  | 
<a href="/List?certificates=Hong%20Kong:IIB&&heading=14;Hong%20Kong:IIB">
Hong Kong:IIB</a>  | 
<a href="/List?certificates=Netherlands:16&&heading=14;Netherlands:16">
Netherlands:16</a>  | 
<a href="/List?certificates=New%20Zealand:R15&&heading=14;New%20Zealand:R15">
New Zealand:R15</a>  | 
<a href="/List?certificates=Norway:15&&heading=14;Norway:15">
Norway:15</a>  | 
<a href="/List?certificates=Philippines:PG-13&&heading=14;Philippines:PG-13">
Philippines:PG-13</a>  | 
<a href="/List?certificates=Singapore:PG&&heading=14;Singapore:PG">
Singapore:PG</a>  | 
<a href="/List?certificates=South%20Korea:15&&heading=14;South%20Korea:15">
South Korea:15</a>  | 
<a href="/List?certificates=Spain:13&&heading=14;Spain:13">
Spain:13</a>  | 
<a href="/List?certificates=Sweden:15&&heading=14;Sweden:15">
Sweden:15</a>  | 
<a href="/List?certificates=UK:15&&heading=14;UK:15">
UK:15</a>  | 
<a href="/List?certificates=USA:R&&heading=14;USA:R">
USA:R</a> <i>(Certificate #37232)</i>
</div>

<div class="info">
<h5>Filming Locations:</h5> 

<a  href="/List?endings=on&&locations=Botany%20Bay%20Plantation%20-%207510%20Botany%20Bay%20Road,%20Edisto%20Island,%20South%20Carolina,%20USA&&heading=18;with+locations+including;Botany%20Bay%20Plantation%20-%207510%20Botany%20Bay%20Road,%20Edisto%20Island,%20South%20Carolina,%20USA">
Botany Bay Plantation - 7510 Botany Bay Road, Edisto Island, South Carolina, USA</a>

<a class="tn15more inline" href="/title/tt0187393/locations" onClick="(new Image()).src='/rg/title-tease/locations/images/b.gif?link=/title/tt0187393/locations';">more</a>

</div>

<div class="info">
<h5>MOVIEmeter: <a href="/help/show_leaf?prowhatisstarmeter"><img src="http://i.media-imdb.com/images/tn15/meter_help.gif" width="12" height="12" border="0" alt="?"></a></h5>
<span class="meter">
<span class="down"><img src="http://i.media-imdb.com/images/tn15/meter_down.gif" width="9" height="8" alt="V" valign="middle"/> 17% </span>since last week
<a href="http://pro.imdb.com/title/tt0187393/graph-data" onClick="(new Image()).src='/rg/meter-tease/title/images/b.gif?link=http://pro.imdb.com/title/tt0187393/graph-data';">why?</a>
</span>
</div>

<div class="info">
<h5>Company:</h5>
<a href="/company/co0050868/">Columbia Pictures Corporation</a>

<a class="tn15more inline" href="/title/tt0187393/companycredits">more</a>
</div>

<hr/> 
<h3>Fun Stuff</h3>

<div class="info">
<h5>Trivia:</h5>
Rocking chairs are not believed to have been common furniture before the early 19th century. While Col. Martin is waiting in Gen. Cornwalis' office, he notices and begins to specifically examine the rocking chair in the corner, finally going so far as to sit in it. (Though apocryphal, Benjamin Franklin is sometimes attributed with inventing the rocking chair.)
<a class="tn15more inline" href="/title/tt0187393/trivia" onClick="(new Image()).src='/rg/title-tease/trivia/images/b.gif?link=/title/tt0187393/trivia';">more</a>
</div>

<div class="info">
<h5>Goofs:</h5>
Miscellaneous: A major error in the final battle (Guilford Courthouse) is when Cornwallis orders "Sound the retreat." The British controlled the battlefield at the end of the day with Greene's army having escaped intact across the river. Cornwallis delivered both the wounded British and American to a nearby Quaker settlement for treatment.
<a class="tn15more inline" href="/title/tt0187393/goofs" onClick="(new Image()).src='/rg/title-tease/goofs/images/b.gif?link=/title/tt0187393/goofs';">more</a>
</div>

<div class="info">
<h5>Quotes:</h5>

<b><a href="/name/nm0005132/">Gabriel Edward Martin</a></b>:
I've come to call on Anne. <br>[<i class="fine">Anne's father puts an ear piece in his ear to hear. Gabriel leans in and tries again louder</i>] <br>
<b><a href="/name/nm0005132/">Gabriel Edward Martin</a></b>:
I've come to call on Anne. <br>
<b><a href="/name/nm0896649/">Mr. Howard</a></b>:
Well of course you call yourself a man! <br>
<b><a href="/name/nm0004773/">Miss Anne Howard/ Mrs. Anne Martin</a></b>:
Father stop it! You heard him!<br>
<a class="tn15more" href="/title/tt0187393/quotes" onClick="(new Image()).src='/rg/title-tease/quotes/images/b.gif?link=/title/tt0187393/quotes';">more</a>
</div>

<div class="info">
<h5>Movie Connections:</h5> 
Referenced in <a href="/title/tt0443431/">Another Gay Movie</a> (2006)
<a class="tn15more inline" href="/title/tt0187393/movieconnections" onClick="(new Image()).src='/rg/title-tease/movieconnections/images/b.gif?link=/title/tt0187393/movieconnections';">more</a>
</div>

<div class="info">
<h5>Soundtrack:</h5> 
Boney
<a class="tn15more inline" href="/title/tt0187393/soundtrack" onClick="(new Image()).src='/rg/title-tease/soundtrack/images/b.gif?link=/title/tt0187393/soundtrack';">more</a>
</div>

<hr/>
<h3>FAQ</h3>

<a href="/title/tt0187393/faq" onClick="(new Image()).src='/rg/title-tease/faq-empty/images/b.gif?link=/title/tt0187393/faq';">This FAQ is empty. Add the first question.</a>

<hr/>
<div class="headerinline">
<a name="comment"><h3>User Comments</h3></a>&nbsp;&nbsp;&nbsp;<a href="usercomments-enter"><span>(Comment on this title)</span></a>
</div>

<div class="comment">
<script type="text/javascript">
<!--
function yn(id, vote) {
  if (!document.getElementById || !document.createElement || !document.removeChild || !document.appendChild || !document.childNodes || !document.createTextNode) return true;
  var i = new Image();
  i.onload =  function() { ynd(id, 1) };
  i.onerror = function() { ynd(id, 0) };
  i.src = 'usercomments-vote?yni_'+id+'='+vote;
  return false;
}
function ynd(id, status) {
  var d, s, t;
  if (!(d = document.getElementById('ynd_'+id))) return true;
  while (d.childNodes.length) d.removeChild(d.childNodes[0]);
  var s = document.createElement('span');
  if (!status) s.setAttribute('class', 'error');
  var t = document.createTextNode(status ? 'Thank you, your vote will be counted and appear on this page within 24 hours.' : 'Sorry, there was a problem collecting your vote.');
  s.appendChild(t);
  d.appendChild(s);
}
//-->
</script>

<div class="small">
27 out of 40 people found the following comment useful:-
</div>

<b>Heroes and Villains</b>, 9 March 2007<br>
<img width="102" height="12" alt="6/10" src="http://i.media-imdb.com/images/showtimes/60.gif"><br>
<div class="small">
Author:
<a href="/user/ur2955724/comments">James Hitchcock</a> <small>from Tunbridge Wells, England</small>
</div>

</p>
<p>
&quot;The Patriot&quot;, the story of an American farmer who fights in the War of
Independence, is sometimes used, together with &quot;Braveheart&quot;, as
evidence of a supposed anti-British prejudice on the part of Mel
Gibson. This is perhaps unfair to Gibson, who has gone on record as
supporting the ties between Australia and the British monarchy (hardly
the stance of a Brit-hating bigot). Although &quot;Braveheart&quot;, which he
produced and directed, was very much Gibson&#39;s own pet project, he was
neither the producer, director or scriptwriter of &quot;The Patriot&quot;.
Indeed, he was not even first choice to play the lead. The producers
originally wanted Harrison Ford who turned the part down, reportedly
because he felt that the script turned the American Revolution into the
story of one man&#39;s quest for revenge.<br><br>Because of its anti-British stance, the film was badly received in
Britain. One newspaper accused it of blackening the character of the
British officer Banastre Tarleton who served as the inspiration for the
villainous Colonel Tavington. One commentator went so far as to say
that it was the sort of film that the Nazis might have made about the
American Revolution had they won World War II. Unlike some of my
fellow-countrymen, I was not too worried about this aspect of the film.
The total death toll in the American War of Independence was remarkably
low, not only by modern standards but even by the standards of other
wars of this era, such as the Napoleonic War. Nevertheless, in every
war ever fought there have been crimes on both sides, and the War of
Independence was no exception. (The rebels could be as ruthless as the
British, but none of their atrocities are shown in this film). Some of
the deeds attributed to Tavington may be fictitious, such as the
church-burning scene, but in real life Tarleton had a well-deserved
reputation for brutality, and was not only loathed by the American
colonists but also distrusted by his own side. In the film the British
commander Lord Cornwallis is shown as outwardly gentlemanly and
honourable, but prepared secretly to countenance Tavington&#39;s methods.
In reality, Cornwallis wanted to have Tarleton court-martialled;
Tarleton was only saved by his influential connections.<br><br>I did, however, have some reservations about the way these events were
portrayed. It was originally intended to make the film about Francis
Marion, a real-life figure. Unfortunately Marion, although undoubtedly
courageous and a skilled guerrilla leader, was also a slave-owner (as
any landowner of substance in 1770s South Carolina would have been) and
was therefore deemed unworthy to be the hero of a modern blockbuster
(even though a TV series about him was made in the fifties). His
exploits, therefore, are credited to a fictitious &quot;Benjamin Martin&quot;.
The slavery issue could have been avoided by moving the action to, say,
New England, but instead the film gives us a wholly unrealistic picture
of race relations in the period. The black workers on Martin&#39;s land are
all free men, and black and white live together in harmony, with black
soldiers willingly fighting alongside whites in the Continental Army.
This sort of dishonest, idealised portrayal of slavery was at one time
common in films like &quot;Gone with the Wind&quot;, but I thought that it had
died out with the growth of the Civil Rights movement.<br><br>(Incidentally, a reason why so many Southerners supported the
revolutionaries was that slavery had been declared illegal in Britain
itself in 1771 and they feared that the British Parliament would
eventually legislate to ban it in the colonies. Needless to say, there
is no mention of this attitude in the film. In later life Tarleton
became MP for Liverpool, and a vehement defender of slavery. In this,
if in nothing else, he and Marion had something in common).<br><br>My other reservation about the film&#39;s political stance is similar to
Ford&#39;s. The film probably concentrated so heavily on British brutality
because it is difficult to interest a modern audience, even an American
audience, in the actual reasons why the war was fought. It is easy to
make out an intellectual case for the principle of &quot;no taxation without
representation&quot;, which had been part of British constitutional thought
since at least the Civil War in the 1640s. It is much less easy to
justify the spilling of blood in defence of that principle, and Martin,
scarred by his experiences in the French and Indian Wars, is originally
shown as a pacifist, unwilling to fight or to support the Declaration
of Independence which he believes will lead to war. His son Gabriel,
however, joins the Continental Army, but is wrongly accused of being a
spy and threatened with execution. Tavington, believing Martin to be a
rebel sympathiser, burns down his home and murders another son, Thomas.
Martin is forced to take up arms to defend his family and then forms a
guerrilla band which he leads against the British. Despite the title of
the film, however, Martin is not really motivated by patriotism; he
seems less a patriot than a pacifist who has abandoned his principles
in order to seek revenge.<br><br>The film is attractively photographed, although I felt that it
sometimes showed a sanitised, prettified version of eighteenth-century
life. In some ways it reminded me of &quot;The Last Samurai&quot;, another
visually attractive epic flawed by a dishonest approach to history and
by excessive length, although I would rate it slightly higher, largely
because Gibson makes a more commanding and impressive epic hero than
does Tom Cruise. From the viewpoint of anyone without patriotic
preconceptions, it can be seen simply as an exciting (if overlong)
adventure film- my wife, who is not British by birth, was cheering on
Martin and booing Tavington. Nevertheless, its approach to history
never gets beyond a simplified story of heroes and villains. 6/10
</p>

<div class="yn" id="ynd_1614117">
<form method="get" action="/register/">
<input type="hidden" name="why" value="comment_vote">Was the above comment useful to you?
<input class="click" type="image"  value="yes" src="http://i.media-imdb.com/images/tn15/btn_yes.gif" width="34" height="19">
<input class="click" type="image"  value="no" src="http://i.media-imdb.com/images/tn15/btn_no.gif" width="34" height="19">

</form>
</div>

</div>

<a class="tn15more" href="/title/tt0187393/usercomments" onClick="(new Image()).src='/rg/title-tease/comments-bottom/images/b.gif?link=/title/tt0187393/usercomments';">more</a>

<hr/>
<h3>Message Boards</h3>
Discuss this title with other users on <a href="/title/tt0187393/board" onClick="(new Image()).src='/rg/title-tease/boards-top/images/b.gif?link=/title/tt0187393/board';">IMDb message board for The Patriot (2000)</a>

<table class="boards">
<tr><th class="left">Recent Posts (updated daily)</th><th class="right">User</th></tr>

<tr class="odd">
<td><a href="/rg/title-tease/boards-subject/title/tt0187393/board/nest/110419514">Any Americans getting tired of getting blamed for this movie?</a></td>
<td><a href="/rg/title-tease/boards-user/user/ur13064821/boards/profile">amylou_n</a></td>
</tr>

<tr class="even">
<td><a href="/rg/title-tease/boards-subject/title/tt0187393/board/nest/119195460">Historical Accuracies/Inaccuraci es</a></td>
<td><a href="/rg/title-tease/boards-user/user/ur15736299/boards/profile">minerva_89</a></td>
</tr>

<tr class="odd">
<td><a href="/rg/title-tease/boards-subject/title/tt0187393/board/nest/120421254">I watched this movie for the first time today</a></td>
<td><a href="/rg/title-tease/boards-user/user/ur5570418/boards/profile">PhantasmFolly</a></td>
</tr>

<tr class="even">
<td><a href="/rg/title-tease/boards-subject/title/tt0187393/board/nest/118369681">Was there a light bulb or a car?</a></td>
<td><a href="/rg/title-tease/boards-user/user/ur2951744/boards/profile">JV20bucks</a></td>
</tr>

<tr class="odd">
<td><a href="/rg/title-tease/boards-subject/title/tt0187393/board/nest/111626892">How would people react...</a></td>
<td><a href="/rg/title-tease/boards-user/user/ur3394807/boards/profile">pelopen3bc</a></td>
</tr>

<tr class="even">
<td><a href="/rg/title-tease/boards-subject/title/tt0187393/board/nest/118129988">Baby???</a></td>
<td><a href="/rg/title-tease/boards-user/user/ur10120318/boards/profile">bluemonkeywtf</a></td>
</tr>

</table>
<a class="tn15more" href="/title/tt0187393/board" onClick="(new Image()).src='/rg/title-tease/boards-bottom/images/b.gif?link=/title/tt0187393/board';">more</a>

<hr/>

<h3>Recommendations</h3>
<div class="strip">
If you enjoyed this title, our database also recommends:
<table class="recs">
<tr class="poster">

<td><a href="/title/tt0032851/">
<img class="poster"     alt="-"     width="93"     height="158"     src="http://ia.media-imdb.com/images/M/MV5BMTM1NjUyNDg0M15BMl5BanBnXkFtZTcwMDM4MDYyMQ@@._V1._SX93_.jpg" >
</a></td>

<td><a href="/title/tt0266308/">
<img class="poster"     alt="-"     width="93"     height="140"     src="http://ia.media-imdb.com/images/M/MV5BMTIwMjIwMDQ2OV5BMl5BanBnXkFtZTcwODc5ODIzMQ@@._V1._SX93_.jpg" >
</a></td>

<td><a href="/title/tt0112573/">
<img class="poster"     alt="-"     width="93"     height="132"     src="http://ia.media-imdb.com/images/M/MV5BMTYwODQ3MzQ1NF5BMl5BanBnXkFtZTcwMDM3MDU1MQ@@._V1._SX93_.jpg" >
</a></td>

<td><a href="/title/tt0120815/">
<img class="poster"     alt="-"     width="93"     height="139"     src="http://ia.media-imdb.com/images/M/MV5BMjg0NTMzNzc2MV5BMl5BanBnXkFtZTYwODI5MzU5._V1._SX93_.jpg" >
</a></td>

<td><a href="/title/tt0442933/">
<img class="poster"     alt="-"     width="93"     height="137"     src="http://ia.media-imdb.com/images/M/MV5BMjAzNDkzOTQ5MV5BMl5BanBnXkFtZTcwODA1MTU1MQ@@._V1._SX93_.jpg" >
</a></td>

</tr>
<tr>

<td><a href="/title/tt0032851/">'Northwest Passage' (Book I -- Rogers' Rangers)</a></td>

<td><a href="/title/tt0266308/">Batoru rowaiaru</a></td>

<td><a href="/title/tt0112573/">Braveheart</a></td>

<td><a href="/title/tt0120815/">Saving Private Ryan</a></td>

<td><a href="/title/tt0442933/">Beowulf</a></td>

</tr>
<tr class="rating">

<td class="first">
<small>IMDb User Rating:</small>
<br/>
<div class="tinystarbar"><div style="width: 71px"></div></div>
</td>

<td>
<small>IMDb User Rating:</small>
<br/>
<div class="tinystarbar"><div style="width: 79px"></div></div>
</td>

<td>
<small>IMDb User Rating:</small>
<br/>
<div class="tinystarbar"><div style="width: 83px"></div></div>
</td>

<td>
<small>IMDb User Rating:</small>
<br/>
<div class="tinystarbar"><div style="width: 84px"></div></div>
</td>

<td>
<small>IMDb User Rating:</small>
<br/>
<div class="tinystarbar"><div style="width: 66px"></div></div>
</td>

</tr>
</table>
<a href="/title/tt0187393/recommendations" onClick="(new Image()).src='/rg/title-tease/recommendations/images/b.gif?link=/title/tt0187393/recommendations';">Show more recommendations</a>
</div>
<h3>Related Links</h3><table>
<tr><td width="33%" style="width: 400px"> <a href="/title/tt0187393/fullcredits" onClick="(new Image()).src='/rg/title-related/maindetails-fullcredits/images/b.gif?link=/title/tt0187393/fullcredits';">Full cast and crew</a></td><td width="33%" style="width: 400px"> <a href="/title/tt0187393/companycredits" onClick="(new Image()).src='/rg/title-related/maindetails-companycredits/images/b.gif?link=/title/tt0187393/companycredits';">Company credits</a></td><td width="33%" style="width: 400px"> <a href="/title/tt0187393/externalreviews" onClick="(new Image()).src='/rg/title-related/maindetails-externalreviews/images/b.gif?link=/title/tt0187393/externalreviews';">External reviews</a></td></tr><tr><td width="33%" style="width: 400px"> <a href="/title/tt0187393/news" onClick="(new Image()).src='/rg/title-related/maindetails-news/images/b.gif?link=/title/tt0187393/news';">News articles</a></td><td width="33%" style="width: 400px"> <a href="/Sections/Genres/Action/" onClick="(new Image()).src='/rg/title-related/maindetails-genre/images/b.gif?link=/Sections/Genres/Action/';">IMDb Action section</a></td><td width="33%" style="width: 400px"> <a href="/Sections/Countries/Germany/" onClick="(new Image()).src='/rg/title-related/maindetails-country/images/b.gif?link=/Sections/Countries/Germany/';">IMDb Germany section</a></td></tr><tr><td width="33%" style="width: 400px"> <a href="/mymovies/list?pending&amp;add=0187393" onClick="(new Image()).src='/rg/title-related/maindetails-mymovies/images/b.gif?link=/mymovies/list?pending&amp;add=0187393';">Add this title to MyMovies</a></td>
</table>
<div id="tn15bot">
 <div class="right">
  



 </div>
 <div class="left">
  <p><form method="post" action="/updates"><input type="hidden" name="auto" value="legacy/title/tt0187393/"><input type="image" width="67" height="21" name="Update" src="http://i.media-imdb.com/images/tn15/update.gif" border="0" alt="Update"></p><p><i>You may report errors and omissions on this page to the IMDb database managers. They will be examined and if approved will be included in a future update. Clicking the 'Update' button  will take you through a step-by-step process.</i></p></form>

 </div>
</div>

</div>
</div> 
</div> 
<br style="clear:left;" />
</div>

<div id="footer" class="ft">
<hr width="100%" size=1>
<p class="footer" align="center">
<a href="/">Home</a>&nbsp;
  | <a href="/search">Search</A>&nbsp;
  | <a href="/NowPlaying/">Now Playing</a>&nbsp;
  | <a href="/News/">News</A>&nbsp;
  | <a href="/register/?why=mymovies_footer">My Movies</A>&nbsp;
  | <a href="/Games/">Games</A>&nbsp;
  | <a href="/boards/">Boards</A>&nbsp;
| <a href="/help/">Help</a>&nbsp;
  | <A HREF="/Showtimes">US&nbsp;Movie&nbsp;Showtimes</A>&nbsp;
| <A HREF="/top_250_films">Top 250</A>&nbsp;
| <a href="/register/?why=footer">Register</a>&nbsp;
  | <A HREF="/recommends/">Recommendations</A>&nbsp;
  | <A HREF="/widgets/">Widgets</A><br>
  <A HREF="/Charts/">Box&nbsp;Office</A> 
  | <A HREF="/a2z">Index</A> 
  | <A HREF="/Sections/Trailers/">Trailers</A> 
  
  | <a href="/jobs"><b>Jobs</b></a>&nbsp;
  | <a href="https://secure.imdb.com/register/subscribe?c=a394d4442664f6f6475627" onClick="(new Image()).src='/rg/PRO_FOOT/FOOTER/images/b.gif?link=https://secure.imdb.com/register/subscribe?c=a394d4442664f6f6475627';">
    <span style="color:#cc3333"><b>IMDbPro.com&nbsp;-&nbsp;Free&nbsp;Trial</b></span></a> 
  | <a href="http://resume.imdb.com" onClick="(new Image()).src='/rg/resume-footer/footer/images/b.gif?link=http://resume.imdb.com';"><span style="color:#cc3333"><b>IMDb Resume</b></span></a>
<br><br>
<a href="/help/show_article?conditions">Copyright &copy;</a> 1990-2008 
<a href="/help/">IMDb.com, Inc.</a><br>
<a href="/help/show_article?conditions">Terms</a> and <a href="/privacy">Privacy Policy</a> under which this service is provided to you.<br>
An <a href="http://www.amazon.com/exec/obidos/redirect-home/internetmoviedat"><img align="middle" width="86" height="18" border="0" src="http://i.media-imdb.com/images/icons/amazon_logo.gif" alt="Amazon.com"></a> company.&nbsp;
<a href="/advertising/">Advertise</a> on IMDb.&nbsp;
<a href="/tiger_redirect?FT_LIC&/licensing/">License</a> our content.
</p>
<p class="footer" align="center">IMDb is powered by Perl and <b><a href="/rg/jobs/footer-pbp//help/show_leaf?jobatimdb">we are hiring</a></b>!</p>
</div>

</layer>
</div>



<!-- begin BOTTOM_AD -->
<div id="bottom_ad_wrapper">
<script language="JavaScript" type="text/javascript">

//<![CDATA[
document.write('<iframe src="/images/a/ifb/doubleclick/expand.html#imdb.consumer.title/maindetails;tile=7;sz=728x90;p=b;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=' + ord + '?" id="bottom_ad" name="bottom_ad" width="0" height="0" marginwidth="0" marginheight="0" frameborder="0" scrolling="no" allowtransparency="true" onload="ad_utils.resize_iframe(this)">');
if (navigator.userAgent.indexOf("Gecko")==-1)
{document.write('<script language="JavaScript" src="http://ad.doubleclick.net/adj/imdb.consumer.title/maindetails;tile=7;sz=728x90;abr=!ie;p=b;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=' + ord + '?" type="text/javascript"><\/script>');
}
document.write('</iframe>');

//]]>
</script>
<noscript><a href="http://ad.doubleclick.net/jump/imdb.consumer.title/maindetails;tile=7;sz=728x90;p=b;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=427710139430?" target="_blank"><img src="http://ad.doubleclick.net/ad/imdb.consumer.title/maindetails;tile=7;sz=728x90;p=b;k=m;g=ac;m=R;tt=f;g=dr;coo=de;coo=usa;id=tt0187393;g=baa;k=c;g=war;ord=427710139430?"  border="0" alt="advertisement" /></a></noscript>

</div>
<!-- End BOTTOM_AD -->





<!-- sid : 78242 : BOTTOM_SCRIPT -->
<SCRIPT language='JavaScript'>
var rnd = Math.round(Math.random()*10000000);
var https = false; try { https = document.location.href.indexOf('https')==0 } catch(e) {}
document.writeln('<IFRAME src="http'+(https?'s':'')+'://media.adrevolver.com/adrevolver/trace?sip=78&cpy='+rnd+'" width="1" height="1" frameborder="0" marginheight="0" marginwidth="0"></IFRAME>');
</SCRIPT>



<img src="/rd/?q=50403000000030a090f29616f226e276966600000010c6a0e02303038313130353c273832343230000001037a040379646370000001047&cb=122592076127935" width="1" height="1" alt="" border="0">
</div> <!-- id="wrapper" -->
<iframe src="http://images.amazon.com/images/G/01/advertising/associate._V259486457_.html?850-5920761-6059643" width="0" height="0" frameborder="0" style="display:none;"></iframe>
</body>
</html>"""

        return result
    
    def getSearchPage(self, url):
        
        result = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">

<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=7" />
<meta http-equiv="content-type" content="text/html; charset=iso-8859-1">
<title>IMDb Search</title>
<meta name="title" content="IMDb Search">
<meta name="description" content="IMDb: The biggest, best, most award-winning movie site on the planet.">

<meta name="keywords" content="movies,films,movie database,actors,actresses,directors,hollywood,stars,quotes">
<link rel="stylesheet" type="text/css" media="screen" href="http://i.media-imdb.com/images/SF06e7dce069189b1d2d32527382dfcebb/css2/consumersite.css" />
<script type="text/javascript" src="http://i.media-imdb.com/images/SFa66621e6aaaa5f4883e0a05f1530eef2/a/js/ads.js"></script>
<link rel="icon" href="http://i.imdb.com/favicon.ico" />

<link rel="apple-touch-icon" href="http://i.media-imdb.com/apple-touch-icon.png" />




<link rel="stylesheet" type="text/css" media="screen" href="http://i.media-imdb.com/images/SF2db9d72d9c300f0b307f0a3ae3ac0ef9/wheel/widgets.css" />
<link rel="stylesheet" type="text/css" media="screen" href="http://i.media-imdb.com/images/SFb72d7f17aa6a7c4db68966d02a8587d3/wheel/layout.css" />

<!--[if IE]>
<link rel="stylesheet" type="text/css" media="screen" href="http://i.media-imdb.com/images/SF6f54b7612c95a3ca71b33f74bb197e49/wheel/ie.css" />
<![endif]-->
<link rel="stylesheet" type="text/css" href="http://i.media-imdb.com/images/SFf4998318a26e5a6e8304e5bbbef6581a/wheel/fixed.css" />

</head>
<!-- h=iof114 i=2008-11-09 s=legacy(default) t='Sun Nov  9 16:36:11 2008' -->

<body bgcolor="#ffffff" text="#000000" id="styleguide-v2" class="fixed">
<div id="wrapper">


<script language="JavaScript" type="text/javascript">ord = ((this.ad_utils) && (this.ad_utils.ord)) ? this.ad_utils.ord : Math.random()*10000000000000000; </script><!-- begin FLOATING1 -->
<div id="floating1_wrapper">
<script language="JavaScript" type="text/javascript">

//<![CDATA[
document.write('<iframe src="/images/a/ifb/doubleclick/expand.html#imdb.consumer.main/find;tile=1;sz=1x1;p=f1;dcopt=ist;ord=' + ord + '?" id="floating1" name="floating1" width="0" height="0" marginwidth="0" marginheight="0" frameborder="0" scrolling="no" allowtransparency="true" onload="ad_utils.resize_iframe(this)">');
if (navigator.userAgent.indexOf("Gecko")==-1)
{document.write('<script language="JavaScript" src="http://ad.doubleclick.net/adj/imdb.consumer.main/find;tile=1;sz=1x1;abr=!ie;p=f1;dcopt=ist;ord=' + ord + '?" type="text/javascript"><\/script>');
}
document.write('</iframe>');

//]]>
</script>
<noscript><a href="http://ad.doubleclick.net/jump/imdb.consumer.main/find;tile=1;sz=1x1;p=f1;dcopt=ist;ord=584014849113?" target="_blank"><img src="http://ad.doubleclick.net/ad/imdb.consumer.main/find;tile=1;sz=1x1;p=f1;dcopt=ist;ord=584014849113?"  border="0" alt="advertisement" /></a></noscript>

</div>
<!-- End FLOATING1 -->



<div id="root">
<layer name="root">

<div id="nb15">
 <div id="nb15supertab">


<!-- begin TOP_AD -->
<div id="top_ad_wrapper">
<script language="JavaScript" type="text/javascript">

//<![CDATA[
document.write('<iframe src="/images/a/ifb/doubleclick/expand.html#imdb.consumer.main/find;tile=2;sz=468x60,728x90,1008x150;p=t;ord=' + ord + '?" id="top_ad" name="top_ad" width="0" height="80" marginwidth="0" marginheight="0" frameborder="0" scrolling="no" allowtransparency="true" onload="ad_utils.resize_iframe(this)">');
if (navigator.userAgent.indexOf("Gecko")==-1)
{document.write('<script language="JavaScript" src="http://ad.doubleclick.net/adj/imdb.consumer.main/find;tile=2;sz=468x60,728x90,1008x150;abr=!ie;p=t;ord=' + ord + '?" type="text/javascript"><\/script>');
}
document.write('</iframe>');

//]]>
</script>
<noscript><a href="http://ad.doubleclick.net/jump/imdb.consumer.main/find;tile=2;sz=468x60,728x90,1008x150;p=t;ord=584014849113?" target="_blank"><img src="http://ad.doubleclick.net/ad/imdb.consumer.main/find;tile=2;sz=468x60,728x90,1008x150;p=t;ord=584014849113?"  border="0" alt="advertisement" /></a></noscript>

</div>
<!-- End TOP_AD --></div>
  <div id="nb15home">

   <a href="/" onClick="(new Image()).src='/rg/nav-home/navbar/images/b.gif?link=/';"><img src="http://i.media-imdb.com/images/nb15/logo2.gif" alt="Home" 
   title="The Internet Movie Database" border="0" width="177" height="78"></a>
  </div>
 <div id="nb15botbg">
 
  <div id="nb15tabs">
   <a id="nb15nowplaying" href="/nowplaying/" onClick="(new Image()).src='/rg/nav-nowplaying/navbar/images/b.gif?link=/nowplaying/';"><i>Now Playing</i></a>
   <a id="nb15news" href="/news/" onClick="(new Image()).src='/rg/nav-news/navbar/images/b.gif?link=/news/';"><i>Movie/TV News</i></a>
   <a id="nb15mm" href="/mymovies/list" onClick="(new Image()).src='/rg/nav-mymovies/navbar/images/b.gif?link=/mymovies/list';"><i>My Movies</i></a>

   <a id="nb15dvd" href="/sections/dvd/" onClick="(new Image()).src='/rg/nav-video/navbar/images/b.gif?link=/sections/dvd/';"><i>DVD New Releases</i></a>
   <a id="nb15imdbtv" href="/sections/tv/" onClick="(new Image()).src='/rg/nav-imdbtv/navbar/images/b.gif?link=/sections/tv/';"><i>IMDbTV</i></a>
   <a id="nb15boards" href="/boards/" onClick="(new Image()).src='/rg/nav-boards/navbar/images/b.gif?link=/boards/';"><i>Message Boards</i></a>
   <a id="nb15showtimes" href="/showtimes/" onClick="(new Image()).src='/rg/nav-showtimes/navbar/images/b.gif?link=/showtimes/';"><i>Showtimes &amp; Tickets</i></a>
   <a id="nb15pro" href="http://pro.imdb.com/r/imdb-nav/" onClick="(new Image()).src='/rg/nav-pro/navbar/images/b.gif?link=http://pro.imdb.com/r/imdb-nav/';"><i>IMDbPro</i></a>

   <a id="nb15resume" href="http://resume.imdb.com/" onClick="(new Image()).src='/rg/nav-resume/navbar/images/b.gif?link=http://resume.imdb.com/';"><i>IMDb Resume</i></a>
  </div>
 
  <div id="nb15topbg">
   <div id="nb15iesux">
    <div id="nb15personal">

     &nbsp;<span><a href="/register/login" onClick="(new Image()).src='/rg/sub-login/navbar/images/b.gif?link=/register/login';">Login</a> | 
     <a href="/register/?why=personalize" onClick="(new Image()).src='/rg/sub-register/navbar/images/b.gif?link=/register/?why=personalize';">Register</a></span>

    </div>
   </div>
  </div>
  <div id="nb15sub">
   <div>
   <a href="/" onClick="(new Image()).src='/rg/sub-home/navbar/images/b.gif?link=/';">Home</a> |
   
    <a href="/chart/" onClick="(new Image()).src='/rg/sub-top/navbar/images/b.gif?link=/chart/';">Top&nbsp;Movies</a> |
    <a href="/sections/gallery/" onClick="(new Image()).src='/rg/sub-gallery/navbar/images/b.gif?link=/sections/gallery/';">Photos</a> |
    <a href="/indie/" onClick="(new Image()).src='/rg/sub-indie/navbar/images/b.gif?link=/indie/';">Independent&nbsp;Film</a> |
    <a href="/sections/games/" onClick="(new Image()).src='/rg/sub-gamebase/navbar/images/b.gif?link=/sections/games/';">GameBase</a> |
    <a href="/Browse/" onClick="(new Image()).src='/rg/sub-browse/navbar/images/b.gif?link=/Browse/';">Browse</a> |
   
   <a href="/help/" onClick="(new Image()).src='/rg/sub-help/navbar/images/b.gif?link=/help/';">Help</a>

   </div>
  </div>
  <div id="nb15search"> 
   <span class=search><a href="/search" onClick="(new Image()).src='/rg/search-img/navbar/images/b.gif?link=/search';">search</a></span>
   <form method="get" action="/find" name="find">
    <select name="s">
     <option value="all" selected>All</option>
     <option value="tt">Titles</option>

     <option value="ep">TV Episodes</option>
     
      <option>My Movies</option>
     
     <option value="nm">Names</option>
     <option value="co">Companies</option>
     
      <option value="kw">Keywords</option>
     
     
     <option value="char">Characters</option>

     
      <option>Quotes</option>
      <option>Bios</option>
      <option>Plots</option>
    
    </select>
   <input name="q" size="28" value="">
    
    
    <input type="image"  id="nb15go_image"  src="http://i.media-imdb.com/images/intl/en/go.gif" alt="go" value="go" title="go">
    
    
    <span id="nb15searchlinks">

    
     <a href="/search" onClick="(new Image()).src='/rg/search-more/navbar/images/b.gif?link=/search';">more</a> | 
     <a href="/help/show_leaf?searchtips" onClick="(new Image()).src='/rg/search-tips/navbar/images/b.gif?link=/help/show_leaf?searchtips';">tips</a>
    
    </span>
   </form>
  </div>
 </div>
</div>


<!-- begin NAVSTRIP -->
<div id="navstrip_wrapper">
<script language="JavaScript" type="text/javascript">

//<![CDATA[
document.write('<iframe src="/images/a/ifb/doubleclick/expand.html#imdb.consumer.main/find;tile=3;sz=1008x40;p=ns;ord=' + ord + '?" id="navstrip" name="navstrip" width="0" height="0" marginwidth="0" marginheight="0" frameborder="0" scrolling="no" allowtransparency="true" onload="ad_utils.resize_iframe(this)">');
if (navigator.userAgent.indexOf("Gecko")==-1)
{document.write('<script language="JavaScript" src="http://ad.doubleclick.net/adj/imdb.consumer.main/find;tile=3;sz=1008x40;abr=!ie;p=ns;ord=' + ord + '?" type="text/javascript"><\/script>');
}
document.write('</iframe>');

//]]>
</script>
<noscript><a href="http://ad.doubleclick.net/jump/imdb.consumer.main/find;tile=3;sz=1008x40;p=ns;ord=584014849113?" target="_blank"><img src="http://ad.doubleclick.net/ad/imdb.consumer.main/find;tile=3;sz=1008x40;p=ns;ord=584014849113?"  border="0" alt="advertisement" /></a></noscript>

</div>
<!-- End NAVSTRIP -->
<div id="pagecontent">

<table id="outerbody" border="0" width="100%" cellspacing="0" cellpadding="0" class="outer_body">
 <tr valign="top" align="left">
   
   
   <td width="100%" valign="top" align="left">

   
<table border="0" width="100%">
  <td valign="top">
    <table width="100%" border=0 cellspacing="0" cellpadding="0">
      <tr> 
        <td colspan="2" height="12"> </td>
      </tr>
      <tr>
        <td>
<style type="text/css">
ul li {
          list-style-type: none;
      }

</style>
      

<script language="JavaScript">
<!--
function set_cookie(name, value) {
  var date = new Date();
  date.setTime(date.getTime()+600000);
  var cookie = name + "=" + escape(value) +
    "; path=/" +
    "; expires=" + date.toGMTString();
  document.cookie = cookie;
}
function set_args(id, fc, fm) {
  var cookie = id + "/" + fc + "/83/c2M9MXxsbT01MDB8ZmI9Y3x0dD0xfG14PTIwfGh0bWw9MXxjaD0xfGNvPTF8cG49MHxmdD0xfGt3PTF8c2l0ZT1kZnxxPW1hdHJpeHxubT0x";
  if (fm) {
    cookie = cookie + "/" + fm;
  }
  set_cookie("fd", cookie);
}

//-->
</script>
<p style="margin:0 0 0.5em 0;"><b>Media from&nbsp;<a href="/title/tt0133093/">The Matrix</a> (1999)</b></p>
<style type="text/css">

.media_strip_thumbs img {
    margin-right:0.2em;
    border:none;
}

.media_strip_thumbs {
  overflow: hidden;
  height: 90px;
}
.media_strip_thumb img {
  margin-right: 0.2em;
}
.media_strip_thumb {
  float: left; 
  margin-bottom: 50px;
  text-align: right;
  font-family: Tahoma,Verdana,sans-serif;
  font-size: 10pt;
  color:#333333;
}
</style>

<table style="border-collapse:collapse;">
<tr>

<td  class="media_strip_header">
<b>Photos</b>

<span>(<a href="/rg/photos-title/gallery-link/title/tt0133093/mediaindex">see all 112</a> | <a href="/rg/photos-title/slideshow-link/media/rm2302712064/tt0133093?slideshow=1">slideshow</a>)</span>
</td>


</tr>
<tr>

<td>
<div class="media_strip_thumbs">
<div class="media_strip_thumb"><a href="/rg/photos-title/summary/media/rm2302712064/tt0133093"><img height="90" width="90" src="http://ia.media-imdb.com/images/M/MV5BMTAyMDc1MTU0MDBeQTJeQWpwZ15BbWU2MDI5MzU3Nw@@._V1._CR0,0,580,580_SS90_.jpg" border="0"></a></div>
<div class="media_strip_thumb"><a href="/rg/photos-title/summary/media/rm2537593088/tt0133093"><img height="90" width="90" src="http://ia.media-imdb.com/images/M/MV5BMTk2MDgyNzQxMV5BMl5BanBnXkFtZTYwMzkzNTc3._V1._CR0,0,595,595_SS90_.jpg" border="0"></a></div>

<div class="media_strip_thumb"><a href="/rg/photos-title/summary/media/rm2520815872/tt0133093"><img height="90" width="90" src="http://ia.media-imdb.com/images/M/MV5BMTIwMDMzODgyOV5BMl5BanBnXkFtZTYwNjkzNTc3._V1._CR0,0,582,582_SS90_.jpg" border="0"></a></div>
<div class="media_strip_thumb"><a href="/rg/photos-title/summary/media/rm2487261440/tt0133093"><img height="90" width="90" src="http://ia.media-imdb.com/images/M/MV5BNTI0MTI0Mzg5NV5BMl5BanBnXkFtZTYwNzkzNTc3._V1._CR0,0,578,578_SS90_.jpg" border="0"></a></div>
<div class="media_strip_thumb"><a href="/rg/photos-title/summary/media/rm2453707008/tt0133093"><img height="90" width="90" src="http://ia.media-imdb.com/images/M/MV5BMjE1NjI1ODM5M15BMl5BanBnXkFtZTYwOTkzNTc3._V1._CR0,0,586,586_SS90_.jpg" border="0"></a></div>
<div class="media_strip_thumb"><a href="/rg/photos-title/summary/media/rm854104576/tt0133093"><img height="90" width="90" src="http://ia.media-imdb.com/images/M/MV5BMTQwMzk0MzI5NV5BMl5BanBnXkFtZTYwMDEzNDYy._V1._CR84,0,296,296_SS90_.jpg" border="0"></a></div>
<div class="media_strip_thumb"><a href="/rg/photos-title/summary/media/rm837327360/tt0133093"><img height="90" width="90" src="http://ia.media-imdb.com/images/M/MV5BMTI2NjY5MDc0MF5BMl5BanBnXkFtZTYwMjEzNDYy._V1._CR0,0,365,365_SS90_.jpg" border="0"></a></div>
<div class="media_strip_thumb"><a href="/rg/photos-title/summary/media/rm820550144/tt0133093"><img height="90" width="90" src="http://ia.media-imdb.com/images/M/MV5BMTc1NjgzMjU1MF5BMl5BanBnXkFtZTYwNDEzNDYy._V1._CR90,0,285,285_SS90_.jpg" border="0"></a></div>
<div class="media_strip_thumb"><a href="/rg/photos-title/summary/media/rm1072208384/tt0133093"><img height="90" width="90" src="http://ia.media-imdb.com/images/M/MV5BMTY5NzY3NDQ5MF5BMl5BanBnXkFtZTYwNjEzNDYy._V1._CR101,0,185,185_SS90_.jpg" border="0"></a></div>
<div class="media_strip_thumb"><a href="/rg/photos-title/summary/media/rm1055431168/tt0133093"><img height="90" width="90" src="http://ia.media-imdb.com/images/M/MV5BMTU5NDk2Mjg3N15BMl5BanBnXkFtZTYwODEzNDYy._V1._CR59,0,195,195_SS90_.jpg" border="0"></a></div>
</div>
</td>


</tr>
</table>


 <p><b>Popular Titles</b> (Displaying 4 Results)<table><tr> <td valign="top"><a href="/title/tt0133093/" onClick="(new Image()).src='/rg/photo-find/title-tiny/images/b.gif?link=/title/tt0133093/';"><img src="http://ia.media-imdb.com/images/M/MV5BMjEzNjg1NTg2NV5BMl5BanBnXkFtZTYwNjY3MzQ5._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a>&nbsp;</td><td align="right" valign="top"><img src="/images/b.gif" width="1" height="6"><br>1.</td><td valign="top"><img src="/images/b.gif" width="1" height="6"><br><a href="/title/tt0133093/">The Matrix</a> (1999)</td></tr><tr> <td valign="top"><a href="/title/tt0234215/" onClick="(new Image()).src='/rg/photo-find/title-tiny/images/b.gif?link=/title/tt0234215/';"><img src="http://ia.media-imdb.com/images/M/MV5BMTIzMzM3Nzg0N15BMl5BanBnXkFtZTcwMTk0MTYyMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a>&nbsp;</td><td align="right" valign="top"><img src="/images/b.gif" width="1" height="6"><br>2.</td><td valign="top"><img src="/images/b.gif" width="1" height="6"><br><a href="/title/tt0234215/">The Matrix Reloaded</a> (2003)<br>&#160;aka <em>"The Matrix 2"</em> - USA <em>(working title)</em><br>&#160;aka <em>"The Matrix Reloaded: The IMAX Experience"</em> - USA <em>(IMAX version) (promotional title)</em></td></tr><tr> <td valign="top"><a href="/title/tt0242653/" onClick="(new Image()).src='/rg/photo-find/title-tiny/images/b.gif?link=/title/tt0242653/';"><img src="http://ia.media-imdb.com/images/M/MV5BNzg2NTA1NTUwNF5BMl5BanBnXkFtZTcwNDk0MTYyMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a>&nbsp;</td><td align="right" valign="top"><img src="/images/b.gif" width="1" height="6"><br>3.</td><td valign="top"><img src="/images/b.gif" width="1" height="6"><br><a href="/title/tt0242653/">The Matrix Revolutions</a> (2003)<br>&#160;aka <em>"The Matrix Revolutions: The IMAX Experience"</em> - USA <em>(IMAX version) (promotional title)</em><br>&#160;aka <em>"The Matrix 3"</em> - USA <em>(working title)</em></td></tr><tr> <td valign="top"><a href="/title/tt0092106/" onClick="(new Image()).src='/rg/photo-find/title-tiny/images/b.gif?link=/title/tt0092106/';"><img src="http://ia.media-imdb.com/images/M/MV5BMTM2MzQ1NDA3OV5BMl5BanBnXkFtZTcwNjM2OTczMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a>&nbsp;</td><td align="right" valign="top"><img src="/images/b.gif" width="1" height="6"><br>4.</td><td valign="top"><img src="/images/b.gif" width="1" height="6"><br><a href="/title/tt0092106/">The Transformers: The Movie</a> (1986)<br>&#160;aka <em>"Transformers the Movie: Apocalypse! Matrix Forever"</em> - Japan <em>(English title)</em> <em>(working title)</em><br>&#160;aka <em>"Transformers: Matrix yo eien ni"</em> - Japan<br>&#160;aka <em>"Transformers the Movie: Mokushiroku - Matrix yo eien ni"</em> - Japan <em>(working title)</em></td></tr></table> </p> <p><b>Titles (Exact Matches)</b> (Displaying 1 Result)<table><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">1.</td><td valign="top"><a href="/title/tt0106062/">&#34;Matrix&#34;</a> (1993) <small>(TV series)</small></td></tr></table> </p> <p><b>Names (Exact Matches)</b> (Displaying 3 Results)<table><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">1.</td><td valign="top"><a href="/name/nm2181131/">Marco Pancrazi</a>  <small>(Stunts, <a href="/title/tt0808151/">Angels &#38; Demons</a> (2009))</small><br>&#160;nickname <em>"Matrix"</em></td></tr><tr> <td valign="top"><a href="/name/nm2584122/" onClick="(new Image()).src='/rg/photo-find/name-tiny/images/b.gif?link=/name/nm2584122/';"><img src="http://ia.media-imdb.com/images/M/MV5BMTQwMzIxMTk5Nl5BMl5BanBnXkFyZXN1bWU@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a>&nbsp;</td><td align="right" valign="top"><img src="/images/b.gif" width="1" height="6"><br>2.</td><td valign="top"><img src="/images/b.gif" width="1" height="6"><br><a href="/name/nm2584122/">Eddie Mariano</a>  <small>(Casting Department, <a href="/title/tt0430357/">Miami Vice</a> (2006))</small><br>&#160;nickname <em>"Eddie Matrix"</em><br>&#160;nickname <em>"Matrix"</em></td></tr><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">3.</td><td valign="top"><a href="/name/nm2309403/">Marco Materazzi</a>  <small>(Self, <a href="/title/tt0496190/">&#34;2006 FIFA World Cup&#34;</a> (2006))</small><br>&#160;nickname <em>"Matrix"</em></td></tr></table> </p> <p><b>Characters (Exact Matches)</b> (Displaying 1 Result)<table><tr>  <td valign="top"><img src="http://i.media-imdb.com/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">1.</td><td valign="top"><a href="/character/ch0029474/">Matrix</a> <small>(<a href="/title/tt0108903/">&#34;ReBoot&#34;</a> (1994), <a href="/name/nm0229928/">Paul Dobson</a>)</small><br>&nbsp;aka <em>&quot;Enzo Matrix #3&quot;</em><br>&nbsp;aka <em>&quot;Enzo Matrix #1&quot;</em><br>&nbsp;aka <em>&quot;Enzo Matrix #4&quot;</em><br>&nbsp;aka <em>&quot;Enzo Matrix&quot;</em></td></tr></table> </p> <p><b>Companies (Exact Matches)</b> (Displaying 3 Results)<table><tr>

<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">1.</td><td valign="top"><a href="/company/co0228478/">Matrix</a> [jp] (Special Effects)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">2.</td><td valign="top"><a href="/company/co0127567/">Matrix</a> [gb] (Miscellaneous)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">3.</td><td valign="top"><a href="/company/co0099311/">Matrix</a> [us] (Film, Video and Audio Stock)</td></tr></table> </p> <p><b>Keywords (Exact Matches)</b> (Displaying 1 Result)<table><tr>

<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">1.</td><td valign="top"><a href="/keyword/matrix/">matrix</a> (11 titles - <a href="/title/tt0069293/">Solyaris</a> (1972), ...)</td></tr></table> </p> <p><b>Titles (Partial Matches)</b> (Displaying 22 Results)<table><tr> <td valign="top"><a href="/title/tt0295432/" onClick="(new Image()).src='/rg/photo-find/title-tiny/images/b.gif?link=/title/tt0295432/';"><img src="http://ia.media-imdb.com/images/M/MV5BMTIzMTA4NDI4NF5BMl5BanBnXkFtZTYwNjg5Nzg4._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a>&nbsp;</td><td align="right" valign="top"><img src="/images/b.gif" width="1" height="6"><br>1.</td><td valign="top"><img src="/images/b.gif" width="1" height="6"><br><a href="/title/tt0295432/">The Matrix Revisited</a> (2001) (V)</td></tr><tr> <td valign="top"><a href="/title/tt0109151/" onClick="(new Image()).src='/rg/photo-find/title-tiny/images/b.gif?link=/title/tt0109151/';"><img src="http://ia.media-imdb.com/images/M/MV5BMjA1Nzg1ODU2MF5BMl5BanBnXkFtZTcwNDQ5NjQyMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a>&nbsp;</td><td align="right" valign="top"><img src="/images/b.gif" width="1" height="6"><br>2.</td><td valign="top"><img src="/images/b.gif" width="1" height="6"><br><a href="/title/tt0109151/">Armitage III: Poly Matrix</a> (1997) (V)</td></tr><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">3.</td><td valign="top"><a href="/title/tt0277828/">Enter the Matrix</a> (2003) (VG)</td></tr><tr> <td valign="top"><a href="/title/tt0303678/" onClick="(new Image()).src='/rg/photo-find/title-tiny/images/b.gif?link=/title/tt0303678/';"><img src="http://ia.media-imdb.com/images/M/MV5BOTUwOTY3Mjg1MF5BMl5BanBnXkFtZTcwODI2MTAyMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a>&nbsp;</td><td align="right" valign="top"><img src="/images/b.gif" width="1" height="6"><br>4.</td><td valign="top"><img src="/images/b.gif" width="1" height="6"><br><a href="/title/tt0303678/">Armitage: Dual Matrix</a> (2002) (V)<br>&#160;aka <em>"Armitage III: Dual Matrix"</em> - Japan <em>(working title)</em></td></tr><tr> <td valign="top"><a href="/title/tt0364888/" onClick="(new Image()).src='/rg/photo-find/title-tiny/images/b.gif?link=/title/tt0364888/';"><img src="http://ia.media-imdb.com/images/M/MV5BMjk4MTA1NDA1Ml5BMl5BanBnXkFtZTcwOTM3Njk0MQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a>&nbsp;</td><td align="right" valign="top"><img src="/images/b.gif" width="1" height="6"><br>5.</td><td valign="top"><img src="/images/b.gif" width="1" height="6"><br><a href="/title/tt0364888/">&#34;Threat Matrix&#34;</a> (2003) <small>(TV series)</small></td></tr><tr> <td valign="top"><a href="/title/tt0390244/" onClick="(new Image()).src='/rg/photo-find/title-tiny/images/b.gif?link=/title/tt0390244/';"><img src="http://ia.media-imdb.com/images/M/MV5BMTYxNTM5MDkwMF5BMl5BanBnXkFtZTcwMTAzMTEzMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a>&nbsp;</td><td align="right" valign="top"><img src="/images/b.gif" width="1" height="6"><br>6.</td><td valign="top"><img src="/images/b.gif" width="1" height="6"><br><a href="/title/tt0390244/">The Matrix Online</a> (2005) (VG)</td></tr><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">7.</td><td valign="top"><a href="/title/tt0274085/">Sex and the Matrix</a> (2000) (TV)</td></tr><tr> <td valign="top"><a href="/title/tt0270841/" onClick="(new Image()).src='/rg/photo-find/title-tiny/images/b.gif?link=/title/tt0270841/';"><img src="http://ia.media-imdb.com/images/M/MV5BMTk5MDAwNDMxMF5BMl5BanBnXkFtZTcwODUzNzIzMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a>&nbsp;</td><td align="right" valign="top"><img src="/images/b.gif" width="1" height="6"><br>8.</td><td valign="top"><img src="/images/b.gif" width="1" height="6"><br><a href="/title/tt0270841/">Avatar</a> (2004)<br>&#160;aka <em>"Matrix Hunter"</em> - Japan <em>(English title)</em> <em>(DVD title)</em>, USA <em>(video title)</em></td></tr><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">9.</td><td valign="top"><a href="/title/tt0451118/">The Matrix: Path of Neo</a> (2005) (VG)</td></tr><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">10.</td><td valign="top"><a href="/title/tt0365467/">Making 'The Matrix'</a> (1999) (TV)</td></tr><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">11.</td><td valign="top"><a href="/title/tt0970173/">Buhera m&#225;trix</a> (2007)</td></tr><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">12.</td><td valign="top"><a href="/title/tt0391319/">Making 'Enter the Matrix'</a> (2003) (V)</td></tr><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">13.</td><td valign="top"><a href="/title/tt0410519/">The Matrix Recalibrated</a> (2004) (V)</td></tr><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">14.</td><td valign="top"><a href="/title/tt0439783/">Return to Source: Philosophy &#38; 'The Matrix'</a> (2004) (V)</td></tr><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">15.</td><td valign="top"><a href="/title/tt0437137/">Crash Course</a> (2003) (V)<br>&#160;aka <em>"The Matrix Reloaded: The Freeway Chase"</em> - USA</td></tr><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">16.</td><td valign="top"><a href="/title/tt0389150/">The Matrix Defence</a> (2003) (TV)</td></tr><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">17.</td><td valign="top"><a href="/title/tt0438231/">The Matrix: The Movie Special</a> (1999) (TV)</td></tr><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">18.</td><td valign="top"><a href="/title/tt0339779/">That 70's Matrix</a> (2001)</td></tr><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">19.</td><td valign="top"><a href="/title/tt0211096/">V-World Matrix</a> (1999) (V)</td></tr><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">20.</td><td valign="top"><a href="/title/tt1074193/">Decoded: The Making of 'The Matrix Reloaded'</a> (2003) (TV)</td></tr><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">21.</td><td valign="top"><a href="/title/tt0333846/">M.A.N.: Matrix Adjusted Normal</a> (1992)</td></tr><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">22.</td><td valign="top"><a href="/title/tt1025014/">New York 360&#186; Presents: The 2007 Matrix Awards</a> (2007) (TV)</td></tr></table> </p> <p><b>Names (Partial Matches)</b> (Displaying 5 Results)<table><tr> <td valign="top"><a href="/name/nm0091443/" onClick="(new Image()).src='/rg/photo-find/name-tiny/images/b.gif?link=/name/nm0091443/';"><img src="http://ia.media-imdb.com/images/M/MV5BMjAzMzY0MDYzNV5BMl5BanBnXkFtZTcwOTA3NzUxMQ@@._V1._SX23_SY30_.jpg" width="23" height="32" border="0"></a>&nbsp;</td><td align="right" valign="top"><img src="/images/b.gif" width="1" height="6"><br>1.</td><td valign="top"><img src="/images/b.gif" width="1" height="6"><br><a href="/name/nm0091443/">Christian Boeving</a>  <small>(Actor, <a href="/title/tt0118688/">Batman &#38; Robin</a> (1997))</small><br>&#160;aka <em>"John Matrix"</em></td></tr><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">2.</td><td valign="top"><a href="/name/nm2238633/">Maarten Lensink</a>  <small>(Miscellaneous Crew, <a href="/title/tt0432495/">Civilization III: Conquests</a> (2003) (VG))</small><br>&#160;aka <em>"Maarten 'Matrix' Lensink"</em></td></tr><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">3.</td><td valign="top"><a href="/name/nm2824796/">Cherie Matrix</a>  <small>(Self, <a href="/title/tt1133192/">&#34;Right to Reply: Red Light Zone Special&#34;</a> (1995))</small></td></tr><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">4.</td><td valign="top"><a href="/name/nm2007893/">Scott Matrix</a>  <small>(Self, <a href="/title/tt0476211/">EWR's Bad Obsession: Sudden Death 3</a> (2004) (V))</small></td></tr><tr> <td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">5.</td><td valign="top"><a href="/name/nm2930488/">Matrix Springer</a>  <small>(Actress, <a href="/title/tt0529183/">&#34;The Bold and the Beautiful: (#1.4205)&#34;</a> (2004))</small></td></tr></table> </p> <p><b>Characters (Partial Matches)</b> (Displaying 6 Results)<table><tr>  <td valign="top"><img src="http://i.media-imdb.com/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">1.</td><td valign="top"><a href="/character/ch0033967/">Dot Matrix</a> <small>(<a href="/title/tt0108903/">&#34;ReBoot&#34;</a> (1994), <a href="/name/nm0056532/">Kathleen Barr</a>)</small></td></tr><tr>  <td valign="top"><img src="http://i.media-imdb.com/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">2.</td><td valign="top"><a href="/character/ch0041897/">Dot Matrix</a> <small>(<a href="/title/tt0094012/">Spaceballs</a> (1987), <a href="/name/nm0001672/">Joan Rivers</a>)</small></td></tr><tr>  <td valign="top"><img src="http://i.media-imdb.com/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">3.</td><td valign="top"><a href="/character/ch0071034/">Steven Matrix</a> <small>(<a href="/title/tt0106062/">&#34;Matrix&#34;</a> (1993), <a href="/name/nm0541576/">Nick Mancuso</a>)</small></td></tr><tr>  <td valign="top"><img src="http://i.media-imdb.com/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">4.</td><td valign="top"><a href="/character/ch0096813/">The Keeper of the Matrix</a> <small>(<a href="/title/tt0056751/">&#34;Doctor Who&#34;</a> (1963), <a href="/name/nm0106657/">James Bree</a>)</small></td></tr><tr>  <td valign="top"><a href="/character/ch0011680/" onClick="(new Image()).src='/rg/photo-find/char-tiny/images/b.gif?link=/character/ch0011680/';"><img src="http://ia.media-imdb.com/images/M/MV5BMTk3NTM4ODY2OF5BMl5BanBnXkFtZTYwOTI1NzA3._V1._SX23_SY30_.jpg" width="20" height="30" border="0"></a>&nbsp;</td><td align="right" valign="top"><img src="http://i.media-imdb.com/images/b.gif" width="1" height="6"><br>5.</td><td valign="top"><img src="http://i.media-imdb.com/images/b.gif" width="1" height="6"><br><a href="/character/ch0011680/">John Matrix</a> <small>(<a href="/title/tt0088944/">Commando</a> (1985), <a href="/name/nm0000216/">Arnold Schwarzenegger</a>)</small></td></tr><tr>  <td valign="top"><img src="http://i.media-imdb.com/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">6.</td><td valign="top"><a href="/character/ch0011681/">Jenny Matrix</a> <small>(<a href="/title/tt0088944/">Commando</a> (1985), <a href="/name/nm0000192/">Alyssa Milano</a>)</small></td></tr></table> </p> <p><b>Companies (Partial Matches)</b> (Displaying 36 Results)<table><tr>

<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">1.</td><td valign="top"><a href="/company/co0069706/">Matrix Alliance Inc.</a> [us] (Post Production Services and Facilities)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">2.</td><td valign="top"><a href="/company/co0105929/">Matrix Film Finance</a> [gb] (Miscellaneous)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">3.</td><td valign="top"><a href="/company/co0130731/">Matrix Management</a>  (Manager)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">4.</td><td valign="top"><a href="/company/co0065252/">Cine-Matrix</a>  (Production)</td></tr><tr>

<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">5.</td><td valign="top"><a href="/company/co0122307/">Matrix Group</a> [it] (Production)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">6.</td><td valign="top"><a href="/company/co0146184/">Matrix Content</a> [us] (Distributor)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">7.</td><td valign="top"><a href="/company/co0149542/">Matrix Productions</a> [hk] (Production)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">8.</td><td valign="top"><a href="/company/co0195537/">Film Matrix MovieWorks, The</a> [us] (Production)</td></tr><tr>

<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">9.</td><td valign="top"><a href="/company/co0036903/">Matrix Films</a>  (Production)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">10.</td><td valign="top"><a href="/company/co0064848/">Matrix Sound Studios</a>  (Post Production Services and Facilities)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">11.</td><td valign="top"><a href="/company/co0094199/">Matrix Video</a> [ca] (Post Production Services and Facilities)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">12.</td><td valign="top"><a href="/company/co0124685/">Matrix Software</a> [jp] (Production)</td></tr><tr>

<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">13.</td><td valign="top"><a href="/company/co0157542/">Studio Matrix</a> [jp] (Production)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">14.</td><td valign="top"><a href="/company/co0016979/">Matrix Movies</a> [us] (Production)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">15.</td><td valign="top"><a href="/company/co0017085/">Matrix Film &#38; Television Partnership</a>  (Production)</td></tr><tr>

<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">16.</td><td valign="top"><a href="/company/co0054743/">Matrix Instruments</a>  (Production Equipment and Services)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">17.</td><td valign="top"><a href="/company/co0056590/">Matrix Television Services</a> [us] (Post Production Services and Facilities)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">18.</td><td valign="top"><a href="/company/co0070645/">Matrix EGI</a>  (Production)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">19.</td><td valign="top"><a href="/company/co0071421/">Matrix Inc.</a>  (Post Production Services and Facilities)</td></tr><tr>

<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">20.</td><td valign="top"><a href="/company/co0125199/">Matrix Games</a> [us] (Distributor)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">21.</td><td valign="top"><a href="/company/co0134858/">EMC Matrix</a>  (Legal Representative)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">22.</td><td valign="top"><a href="/company/co0189858/">Motion Matrix</a> [us] (Distributor)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">23.</td><td valign="top"><a href="/company/co0196099/">Matrix Models</a> [us] (Special Thanks)</td></tr><tr>

<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">24.</td><td valign="top"><a href="/company/co0197452/">Matrix One</a> [us] (Special Thanks)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">25.</td><td valign="top"><a href="/company/co0205854/">Matrix-PV</a> [cz] (Distributor)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">26.</td><td valign="top"><a href="/company/co0212241/">JOT Matrix</a> [jp] (Miscellaneous)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">27.</td><td valign="top"><a href="/company/co0215021/">Matrix Architecture &#38; Design</a> [in] (Art Department Services)</td></tr><tr>

<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">28.</td><td valign="top"><a href="/company/co0221739/">Creation Matrix</a> [us] (Production)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">29.</td><td valign="top"><a href="/company/co0228145/">Matrix Fitness System</a> [gb] (Special Thanks)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">30.</td><td valign="top"><a href="/company/co0236313/">Matrix New Professionals Partnership</a> [gb] (Production)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">31.</td><td valign="top"><a href="/company/co0238439/">Matrix Capital Entertainment</a> [cn] (Production)</td></tr><tr>

<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">32.</td><td valign="top"><a href="/company/co0238533/">Matrix Film</a> [it] (Production)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">33.</td><td valign="top"><a href="/company/co0095053/">Matrix Entertainments Ltd.</a>  (Miscellaneous)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">34.</td><td valign="top"><a href="/company/co0174113/">Matrix Productions Company</a> [hk] (Miscellaneous)</td></tr><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">35.</td><td valign="top"><a href="/company/co0202930/">Matrix Entertainment Management</a> [us] (Miscellaneous)</td></tr><tr>

<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">36.</td><td valign="top"><a href="/company/co0226577/">Active Matrix Networks</a> [us] (Miscellaneous)</td></tr></table> </p> <p><b>Keywords (Partial Matches)</b> (Displaying 1 Result)<table><tr>
<td valign="top"><img src="/images/b.gif" alt="" width="23" height="1"></td><td align="right" valign="top">1.</td><td valign="top"><a href="/keyword/the-matrix/">the-matrix</a> (17 titles - <a href="/title/tt0133093/">The Matrix</a> (1999), ...)</td></tr></table> </p>

<script type="text/javascript">
var afsStrings_displaying = new Array();
afsStrings_displaying[1] = "Displaying 1 Result";
afsStrings_displaying[2] = "Displaying 2 Results";
afsStrings_displaying[3] = "Displaying 3 Results";
afsStrings_displaying[4] = "Displaying 4 Results";
afsStrings_displaying[5] = "Displaying 5 Results";
var afsStrings = new Array();
afsStrings["sponsored_links"] = "Sponsored links";
afsStrings["whats_this"] = "(What's this?)";
afsStrings["query"] = "matrix";

function get_afs_div() {
  return document.getElementById('afs_sponsored_links');
}
</script>
<div id="afs_sponsored_links" name="afs_sponsored_links"></div>



<!-- begin MIDDLE_CENTER -->
<div id="middle_center_wrapper">
<script language="JavaScript" type="text/javascript">

//<![CDATA[
document.write('<iframe src="/images/a/ifb/doubleclick/expand.html#imdb.consumer.main/find;tile=4;sz=1x1;p=mc;ord=' + ord + '?" id="middle_center" name="middle_center" width="0" height="0" marginwidth="0" marginheight="0" frameborder="0" scrolling="no" allowtransparency="true" onload="ad_utils.resize_iframe(this)">');
if (navigator.userAgent.indexOf("Gecko")==-1)
{document.write('<script language="JavaScript" src="http://ad.doubleclick.net/adj/imdb.consumer.main/find;tile=4;sz=1x1;abr=!ie;p=mc;ord=' + ord + '?" type="text/javascript"><\/script>');
}
document.write('</iframe>');

//]]>
</script>
<noscript><a href="http://ad.doubleclick.net/jump/imdb.consumer.main/find;tile=4;sz=1x1;p=mc;ord=584014849113?" target="_blank"><img src="http://ad.doubleclick.net/ad/imdb.consumer.main/find;tile=4;sz=1x1;p=mc;ord=584014849113?"  border="0" alt="advertisement" /></a></noscript>

</div>
<!-- End MIDDLE_CENTER -->
<p>
<b>Suggestions For Improving Your Results</b>

<ul>

<li>
  There may be additional title matches amongst all the alternative
titles we have for various regions and languages.

  <ul>
    <li><a href="/find?q=matrix;s=tt;site=aka">AKA Title Search for "<b>matrix</b>"</a>.</li>
  </ul>
  <br>
</li>

<li>
  If you are searching for a particular episode of a TV Series, you should search for the title of the TV series, not the episode.  Or you can use the following link to search all Episode Titles.
  <ul>
    <li><a href="/find?q=matrix;s=tt;ttype=ep">Episode Title Search for "<b>matrix</b>"</a>.</li>
  </ul>
  <br>
</li>

<li>
  There may be additional matches in special interest areas that are
only available to users choosing to see them.

  <ul>
    <li><a href="/find/preferences?_adult=1">Enable</a> adult titles/names in the search.</li>
  </ul>
  <br>
</li>

</ul>
</p>

<p>
<b>More Searches For: matrix</b>

<ul>
  <li class="other">
    
      <a href="/find?q=matrix;more=tt;ttype=df">Titles</a>
      &nbsp;|&nbsp;&nbsp;<a href="/find?q=matrix;more=nm">Names</a>
      &nbsp;|&nbsp;&nbsp;<a href="/find?q=matrix;more=co">Companies</a>

      
        &nbsp;|&nbsp;&nbsp;<a href="/find?q=matrix;more=kw">Plot&nbsp;Keywords</a>
        &nbsp;|&nbsp;&nbsp;<a href="/find?q=matrix;more=ft">IMDb&nbsp;Site&nbsp;Features</a>
      
    
    &nbsp;|&nbsp;
    <a href="/find?s=char;q=matrix" onClick="(new Image()).src='/rg/GOOGLE_FIND_othersearches/TOP_RHS/images/b.gif?link=/find?s=char;q=matrix';">Characters</a>

    
      &nbsp;&nbsp;|&nbsp;
      <a href="/SearchPlots?matrix" onClick="(new Image()).src='/rg/GOOGLE_FIND_othersearches/TOP_RHS/images/b.gif?link=/SearchPlots?matrix';">Plot&nbsp;Summaries</a>&nbsp;&nbsp;|&nbsp;
      <a href="/SearchBios?matrix" onClick="(new Image()).src='/rg/GOOGLE_FIND_othersearches/TOP_RHS/images/b.gif?link=/SearchBios?matrix';">Biographies</a>&nbsp;&nbsp;|&nbsp;
      <a href="/SearchQuotes?matrix" onClick="(new Image()).src='/rg/GOOGLE_FIND_othersearches/TOP_RHS/images/b.gif?link=/SearchQuotes?matrix';">Quotes</a>&nbsp;&nbsp;|&nbsp;
      <a href="/SearchAll?matrix">more&#160;&#187;</a>

    
    <br><br>
  </li>
</ul>
</p>

<p>
<b>Update your</b> <a href="/find/preferences" title="Set your Search Preferences">search preferences</a>.
</p>

<!-- [Elapsed Time: 0.010398s (cache hit)] -->

</td>

</tr>
</table>
</p>

</td>
      </tr>
      <tr>
        <td>
          <br style="clear: left"/>
          <div style="clear: left; width: 450px">
            



          </div>

          <br style="clear: both"/>
        </td>
      </tr>
    </table>
  </td>
  <td valign=top>
    <table>
      <tr>
        <td>

          <table>
            <tr>
              <td>


<!-- begin TOP_RHS -->
<div id="top_rhs_wrapper">
<script language="JavaScript" type="text/javascript">

//<![CDATA[
document.write('<iframe src="/images/a/ifb/doubleclick/expand.html#imdb.consumer.main/find;tile=5;sz=300x250,300x600,160x600,171x600;p=tr;ord=' + ord + '?" id="top_rhs" name="top_rhs" width="0" height="0" marginwidth="0" marginheight="0" frameborder="0" scrolling="no" allowtransparency="true" onload="ad_utils.resize_iframe(this)">');
if (navigator.userAgent.indexOf("Gecko")==-1)
{document.write('<script language="JavaScript" src="http://ad.doubleclick.net/adj/imdb.consumer.main/find;tile=5;sz=300x250,300x600,160x600,171x600;abr=!ie;p=tr;ord=' + ord + '?" type="text/javascript"><\/script>');
}
document.write('</iframe>');

//]]>
</script>
<noscript><a href="http://ad.doubleclick.net/jump/imdb.consumer.main/find;tile=5;sz=300x250,300x600,160x600,171x600;p=tr;ord=584014849113?" target="_blank"><img src="http://ad.doubleclick.net/ad/imdb.consumer.main/find;tile=5;sz=300x250,300x600,160x600,171x600;p=tr;ord=584014849113?"  border="0" alt="advertisement" /></a></noscript>

</div>
<!-- End TOP_RHS --></td>

            </tr>
          </table>
        </td>
      </tr>
    </table>
  </td>
</table>
  </td>
 </tr>

</table>
<br style="clear:left;" />
</div>

<div id="footer" class="ft">
<hr width="100%" size=1>
<p class="footer" align="center">
<a href="/">Home</a>&nbsp;
  | <a href="/search">Search</A>&nbsp;
  | <a href="/NowPlaying/">Now Playing</a>&nbsp;

  | <a href="/News/">News</A>&nbsp;
  | <a href="/register/?why=mymovies_footer">My Movies</A>&nbsp;
  | <a href="/Games/">Games</A>&nbsp;
  | <a href="/boards/">Boards</A>&nbsp;
| <a href="/help/">Help</a>&nbsp;

  | <A HREF="/Showtimes">US&nbsp;Movie&nbsp;Showtimes</A>&nbsp;
| <A HREF="/top_250_films">Top 250</A>&nbsp;
| <a href="/register/?why=footer">Register</a>&nbsp;
  | <A HREF="/recommends/">Recommendations</A>&nbsp;
  | <A HREF="/widgets/">Widgets</A><br>

  <A HREF="/Charts/">Box&nbsp;Office</A> 
  | <A HREF="/a2z">Index</A> 
  | <A HREF="/Sections/Trailers/">Trailers</A> 
  
  | <a href="/jobs"><b>Jobs</b></a>&nbsp;
  | <a href="https://secure.imdb.com/register/subscribe?c=a394d4442664f6f6475627" onClick="(new Image()).src='/rg/PRO_FOOT/FOOTER/images/b.gif?link=https://secure.imdb.com/register/subscribe?c=a394d4442664f6f6475627';">
    <span style="color:#cc3333"><b>IMDbPro.com&nbsp;-&nbsp;Free&nbsp;Trial</b></span></a> 
  | <a href="http://resume.imdb.com" onClick="(new Image()).src='/rg/resume-footer/footer/images/b.gif?link=http://resume.imdb.com';"><span style="color:#cc3333"><b>IMDb Resume</b></span></a>

<br><br>
<a href="/help/show_article?conditions">Copyright &copy;</a> 1990-2008 
<a href="/help/">IMDb.com, Inc.</a><br>
<a href="/help/show_article?conditions">Terms</a> and <a href="/privacy">Privacy Policy</a> under which this service is provided to you.<br>
An <a href="http://www.amazon.com/exec/obidos/redirect-home/internetmoviedat"><img align="middle" width="86" height="18" border="0" src="http://i.media-imdb.com/images/icons/amazon_logo.gif" alt="Amazon.com"></a> company.&nbsp;

<a href="/advertising/">Advertise</a> on IMDb.&nbsp;
<a href="/tiger_redirect?FT_LIC&/licensing/">License</a> our content.
</p>
<p class="footer" align="center">IMDb is powered by Perl and <b><a href="/rg/jobs/footer-pbp//help/show_leaf?jobatimdb">we are hiring</a></b>!</p>
</div>

</layer>
</div>


<!-- begin BOTTOM_AD -->
<div id="bottom_ad_wrapper">
<script language="JavaScript" type="text/javascript">

//<![CDATA[
document.write('<iframe src="/images/a/ifb/doubleclick/expand.html#imdb.consumer.main/find;tile=6;sz=728x90;p=b;ord=' + ord + '?" id="bottom_ad" name="bottom_ad" width="0" height="0" marginwidth="0" marginheight="0" frameborder="0" scrolling="no" allowtransparency="true" onload="ad_utils.resize_iframe(this)">');
if (navigator.userAgent.indexOf("Gecko")==-1)
{document.write('<script language="JavaScript" src="http://ad.doubleclick.net/adj/imdb.consumer.main/find;tile=6;sz=728x90;abr=!ie;p=b;ord=' + ord + '?" type="text/javascript"><\/script>');
}
document.write('</iframe>');

//]]>
</script>
<noscript><a href="http://ad.doubleclick.net/jump/imdb.consumer.main/find;tile=6;sz=728x90;p=b;ord=584014849113?" target="_blank"><img src="http://ad.doubleclick.net/ad/imdb.consumer.main/find;tile=6;sz=728x90;p=b;ord=584014849113?"  border="0" alt="advertisement" /></a></noscript>

</div>
<!-- End BOTTOM_AD -->





<!-- sid : 78242 : BOTTOM_SCRIPT -->

<SCRIPT language='JavaScript'>
var rnd = Math.round(Math.random()*10000000);
var https = false; try { https = document.location.href.indexOf('https')==0 } catch(e) {}
document.writeln('<IFRAME src="http'+(https?'s':'')+'://media.adrevolver.com/adrevolver/trace?sip=78&cpy='+rnd+'" width="1" height="1" frameborder="0" marginheight="0" marginwidth="0"></IFRAME>');
</SCRIPT>



<img src="/rd/?q=50403000000030a090f29616f226e276966600000010c6a0412303038313130393c21323837373c273832343230000001037a040379646370000001047&cb=122627737126150" width="1" height="1" alt="" border="0">
</div> <!-- id="wrapper" -->

</body>
</html>"""
        
        return result
    
    def getPosterPage(self, url):
        
        result = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">

<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=7" />
<meta http-equiv="content-type" content="text/html; charset=iso-8859-1">
<title>The Matrix (1999) - Posters</title>
<meta name="title" content="The Matrix (1999) - Posters">
<meta name="description" content="The Matrix on IMDb: Movies, TV, Celebs, and more...">

<meta name="keywords" content="Reviews, Showtimes, DVDs, Photos, Message Boards, User Ratings, Synopsis, Trailers, Credits">
<link rel="stylesheet" type="text/css" media="screen" href="http://i.media-imdb.com/images/SF06e7dce069189b1d2d32527382dfcebb/css2/consumersite.css" />
<script type="text/javascript" src="http://i.media-imdb.com/images/SFa66621e6aaaa5f4883e0a05f1530eef2/a/js/ads.js"></script>
<link rel="icon" href="http://i.imdb.com/favicon.ico" />

<link rel="apple-touch-icon" href="http://i.media-imdb.com/apple-touch-icon.png" />
<link rel="stylesheet" type="text/css" href="http://i.media-imdb.com/images/SFca2cd0a5ab9db43ff9d7f7af6cc6f361/tn15/tn15.css" />




<link rel="stylesheet" type="text/css" media="screen" href="http://i.media-imdb.com/images/SF2c798c76034e2cd9e0b278a275ee3096/wheel/base.css" />

<link rel="stylesheet" type="text/css" media="screen" href="http://i.media-imdb.com/images/SF2db9d72d9c300f0b307f0a3ae3ac0ef9/wheel/widgets.css" />
<link rel="stylesheet" type="text/css" media="screen" href="http://i.media-imdb.com/images/SFb72d7f17aa6a7c4db68966d02a8587d3/wheel/layout.css" />

<!--[if IE]>
<link rel="stylesheet" type="text/css" media="screen" href="http://i.media-imdb.com/images/SF6f54b7612c95a3ca71b33f74bb197e49/wheel/ie.css" />
<![endif]-->
<link rel="stylesheet" type="text/css" href="http://i.media-imdb.com/images/SFf4998318a26e5a6e8304e5bbbef6581a/wheel/fixed.css" />

</head>
<!-- h=iop505 i=2008-11-09 s=legacy(default) t='Sun Nov  9 18:30:40 2008' -->

<body bgcolor="#ffffff" text="#000000" id="styleguide-v2" class="fixed">
<div id="wrapper">



<script language="JavaScript" type="text/javascript">ord = ((this.ad_utils) && (this.ad_utils.ord)) ? this.ad_utils.ord : Math.random()*10000000000000000; </script><!-- begin FLOATING1 -->
<div id="floating1_wrapper">
<script language="JavaScript" type="text/javascript">

//<![CDATA[
document.write('<iframe src="/images/a/ifb/doubleclick/expand.html#imdb.consumer.title/;tile=1;sz=1x1;p=f1;dcopt=ist;g=th;g=ad;k=m;g=ac;m=R;g=sf;tt=f;k=r;k=p;id=tt0133093;coo=usa;k=c;g=baa;ord=' + ord + '?" id="floating1" name="floating1" width="0" height="0" marginwidth="0" marginheight="0" frameborder="0" scrolling="no" allowtransparency="true" onload="ad_utils.resize_iframe(this)">');
if (navigator.userAgent.indexOf("Gecko")==-1)
{document.write('<script language="JavaScript" src="http://ad.doubleclick.net/adj/imdb.consumer.title/;tile=1;sz=1x1;abr=!ie;p=f1;dcopt=ist;g=th;g=ad;k=m;g=ac;m=R;g=sf;tt=f;k=r;k=p;id=tt0133093;coo=usa;k=c;g=baa;ord=' + ord + '?" type="text/javascript"><\/script>');
}
document.write('</iframe>');

//]]>
</script>
<noscript><a href="http://ad.doubleclick.net/jump/imdb.consumer.title/;tile=1;sz=1x1;p=f1;dcopt=ist;g=th;g=ad;k=m;g=ac;m=R;g=sf;tt=f;k=r;k=p;id=tt0133093;coo=usa;k=c;g=baa;ord=129034736832?" target="_blank"><img src="http://ad.doubleclick.net/ad/imdb.consumer.title/;tile=1;sz=1x1;p=f1;dcopt=ist;g=th;g=ad;k=m;g=ac;m=R;g=sf;tt=f;k=r;k=p;id=tt0133093;coo=usa;k=c;g=baa;ord=129034736832?"  border="0" alt="advertisement" /></a></noscript>

</div>
<!-- End FLOATING1 -->


<div id="root">
<layer name="root">

<div id="nb15">
 <div id="nb15supertab">


<!-- begin TOP_AD -->
<div id="top_ad_wrapper">
<script language="JavaScript" type="text/javascript">

//<![CDATA[
document.write('<iframe src="/images/a/ifb/doubleclick/expand.html#imdb.consumer.title/;tile=2;sz=468x60,728x90,1008x150;p=t;g=th;g=ad;k=m;g=ac;m=R;g=sf;tt=f;k=r;k=p;id=tt0133093;coo=usa;k=c;g=baa;ord=' + ord + '?" id="top_ad" name="top_ad" width="0" height="80" marginwidth="0" marginheight="0" frameborder="0" scrolling="no" allowtransparency="true" onload="ad_utils.resize_iframe(this)">');
if (navigator.userAgent.indexOf("Gecko")==-1)
{document.write('<script language="JavaScript" src="http://ad.doubleclick.net/adj/imdb.consumer.title/;tile=2;sz=468x60,728x90,1008x150;abr=!ie;p=t;g=th;g=ad;k=m;g=ac;m=R;g=sf;tt=f;k=r;k=p;id=tt0133093;coo=usa;k=c;g=baa;ord=' + ord + '?" type="text/javascript"><\/script>');
}
document.write('</iframe>');

//]]>
</script>
<noscript><a href="http://ad.doubleclick.net/jump/imdb.consumer.title/;tile=2;sz=468x60,728x90,1008x150;p=t;g=th;g=ad;k=m;g=ac;m=R;g=sf;tt=f;k=r;k=p;id=tt0133093;coo=usa;k=c;g=baa;ord=129034736832?" target="_blank"><img src="http://ad.doubleclick.net/ad/imdb.consumer.title/;tile=2;sz=468x60,728x90,1008x150;p=t;g=th;g=ad;k=m;g=ac;m=R;g=sf;tt=f;k=r;k=p;id=tt0133093;coo=usa;k=c;g=baa;ord=129034736832?"  border="0" alt="advertisement" /></a></noscript>

</div>

<!-- End TOP_AD --></div>
  <div id="nb15home">
   <a href="/" onClick="(new Image()).src='/rg/nav-home/navbar/images/b.gif?link=/';"><img src="http://i.media-imdb.com/images/nb15/logo2.gif" alt="Home" 
   title="The Internet Movie Database" border="0" width="177" height="78"></a>
  </div>
 <div id="nb15botbg">
 
  <div id="nb15tabs">
   <a id="nb15nowplaying" href="/nowplaying/" onClick="(new Image()).src='/rg/nav-nowplaying/navbar/images/b.gif?link=/nowplaying/';"><i>Now Playing</i></a>
   <a id="nb15news" href="/news/" onClick="(new Image()).src='/rg/nav-news/navbar/images/b.gif?link=/news/';"><i>Movie/TV News</i></a>

   <a id="nb15mm" href="/mymovies/list" onClick="(new Image()).src='/rg/nav-mymovies/navbar/images/b.gif?link=/mymovies/list';"><i>My Movies</i></a>
   <a id="nb15dvd" href="/sections/dvd/" onClick="(new Image()).src='/rg/nav-video/navbar/images/b.gif?link=/sections/dvd/';"><i>DVD New Releases</i></a>
   <a id="nb15imdbtv" href="/sections/tv/" onClick="(new Image()).src='/rg/nav-imdbtv/navbar/images/b.gif?link=/sections/tv/';"><i>IMDbTV</i></a>
   <a id="nb15boards" href="/boards/" onClick="(new Image()).src='/rg/nav-boards/navbar/images/b.gif?link=/boards/';"><i>Message Boards</i></a>
   <a id="nb15showtimes" href="/showtimes/" onClick="(new Image()).src='/rg/nav-showtimes/navbar/images/b.gif?link=/showtimes/';"><i>Showtimes &amp; Tickets</i></a>

   <a id="nb15pro" href="http://pro.imdb.com/r/imdb-nav/" onClick="(new Image()).src='/rg/nav-pro/navbar/images/b.gif?link=http://pro.imdb.com/r/imdb-nav/';"><i>IMDbPro</i></a>
   <a id="nb15resume" href="http://resume.imdb.com/" onClick="(new Image()).src='/rg/nav-resume/navbar/images/b.gif?link=http://resume.imdb.com/';"><i>IMDb Resume</i></a>
  </div>
 
  <div id="nb15topbg">
   <div id="nb15iesux">
    <div id="nb15personal">

     &nbsp;<span><a href="/register/login" onClick="(new Image()).src='/rg/sub-login/navbar/images/b.gif?link=/register/login';">Login</a> | 
     <a href="/register/?why=personalize" onClick="(new Image()).src='/rg/sub-register/navbar/images/b.gif?link=/register/?why=personalize';">Register</a></span>

    </div>
   </div>
  </div>
  <div id="nb15sub">
   <div>
   <a href="/" onClick="(new Image()).src='/rg/sub-home/navbar/images/b.gif?link=/';">Home</a> |
   
    <a href="/chart/" onClick="(new Image()).src='/rg/sub-top/navbar/images/b.gif?link=/chart/';">Top&nbsp;Movies</a> |
    <a href="/sections/gallery/" onClick="(new Image()).src='/rg/sub-gallery/navbar/images/b.gif?link=/sections/gallery/';">Photos</a> |
    <a href="/indie/" onClick="(new Image()).src='/rg/sub-indie/navbar/images/b.gif?link=/indie/';">Independent&nbsp;Film</a> |
    <a href="/sections/games/" onClick="(new Image()).src='/rg/sub-gamebase/navbar/images/b.gif?link=/sections/games/';">GameBase</a> |
    <a href="/Browse/" onClick="(new Image()).src='/rg/sub-browse/navbar/images/b.gif?link=/Browse/';">Browse</a> |
   
   <a href="/help/" onClick="(new Image()).src='/rg/sub-help/navbar/images/b.gif?link=/help/';">Help</a>

   </div>
  </div>
  <div id="nb15search"> 
   <span class=search><a href="/search" onClick="(new Image()).src='/rg/search-img/navbar/images/b.gif?link=/search';">search</a></span>
   <form method="get" action="/find" name="find">
    <select name="s">
     <option value="all" selected>All</option>
     <option value="tt">Titles</option>

     <option value="ep">TV Episodes</option>
     
      <option>My Movies</option>
     
     <option value="nm">Names</option>
     <option value="co">Companies</option>
     
      <option value="kw">Keywords</option>
     
     
     <option value="char">Characters</option>

     
      <option>Quotes</option>
      <option>Bios</option>
      <option>Plots</option>
    
    </select>
   <input name="q" size="28" value="">
    
    
    <input type="image"  id="nb15go_image"  src="http://i.media-imdb.com/images/intl/en/go.gif" alt="go" value="go" title="go">
    
    
    <span id="nb15searchlinks">

    
     <a href="/search" onClick="(new Image()).src='/rg/search-more/navbar/images/b.gif?link=/search';">more</a> | 
     <a href="/help/show_leaf?searchtips" onClick="(new Image()).src='/rg/search-tips/navbar/images/b.gif?link=/help/show_leaf?searchtips';">tips</a>
    
    </span>
   </form>
  </div>
 </div>
</div>


<!-- begin NAVSTRIP -->
<div id="navstrip_wrapper">
<script language="JavaScript" type="text/javascript">

//<![CDATA[
document.write('<iframe src="/images/a/ifb/doubleclick/expand.html#imdb.consumer.title/;tile=3;sz=1008x40;p=ns;g=th;g=ad;k=m;g=ac;m=R;g=sf;tt=f;k=r;k=p;id=tt0133093;coo=usa;k=c;g=baa;ord=' + ord + '?" id="navstrip" name="navstrip" width="0" height="0" marginwidth="0" marginheight="0" frameborder="0" scrolling="no" allowtransparency="true" onload="ad_utils.resize_iframe(this)">');
if (navigator.userAgent.indexOf("Gecko")==-1)
{document.write('<script language="JavaScript" src="http://ad.doubleclick.net/adj/imdb.consumer.title/;tile=3;sz=1008x40;abr=!ie;p=ns;g=th;g=ad;k=m;g=ac;m=R;g=sf;tt=f;k=r;k=p;id=tt0133093;coo=usa;k=c;g=baa;ord=' + ord + '?" type="text/javascript"><\/script>');
}
document.write('</iframe>');

//]]>
</script>
<noscript><a href="http://ad.doubleclick.net/jump/imdb.consumer.title/;tile=3;sz=1008x40;p=ns;g=th;g=ad;k=m;g=ac;m=R;g=sf;tt=f;k=r;k=p;id=tt0133093;coo=usa;k=c;g=baa;ord=129034736832?" target="_blank"><img src="http://ad.doubleclick.net/ad/imdb.consumer.title/;tile=3;sz=1008x40;p=ns;g=th;g=ad;k=m;g=ac;m=R;g=sf;tt=f;k=r;k=p;id=tt0133093;coo=usa;k=c;g=baa;ord=129034736832?"  border="0" alt="advertisement" /></a></noscript>

</div>
<!-- End NAVSTRIP -->
<div id="pagecontent">

<div id="tn15" class="posters">
<div id="tn15crumbs">
<a href="/">IMDb</a> &gt;

<a href="/title/tt0133093/">The Matrix (1999)</a> &gt; <b>Posters</b>
</div>
<div id="tn15lhs">

<div class="photo">
<a name="poster" href="/rg/action-box-title/primary-photo/media/rm3412696576/tt0133093" title="The Matrix"><img border="0" alt="The Matrix" title="The Matrix" src="http://ia.media-imdb.com/images/M/MV5BMjEzNjg1NTg2NV5BMl5BanBnXkFtZTYwNjY3MzQ5._V1._SX99_SY140_.jpg" /></a>
</div>

<div id="action-box" class="action-box">
<a class="linkasbutton-primary disabled" >Watch It</a>

<p><a href="/rg/action-box-title/watch-at-amazon/r/50403000000050a0904747031333330393330000001036a08046f677e6c6f6164600000010d6a02064940000001037a0104700000010f5a0403786f6070000001047">Watch it at Amazon</a></p>

<p><img src="/images/wheel/or-graphic.png" /></p>

<a class="linkasbutton-secondary" href="/rg/action-box-title/buy-at-amazon/r/50403000000050a0904747031333330393330000001036a03016c6c600000010d6a02064940000001037a0104700000010f5a0403786f6070000001047">Buy it at Amazon</a>
<hr />
<a class="linkasbutton-secondary" href="/rg/action-box-title/pro-link/http://pro.imdb.com/title/tt0133093/">More at IMDb Pro</a>

<a class="linkasbutton-secondary" href="/rg/action-box-title/boards-link/title/tt0133093/board">Discuss in Boards</a>

<a class="linkasbutton-secondary" href="/rg/action-box-title/add-to-my-movies/mymovies/list?pending&amp;add=0133093">Add to My Movies</a>
<a class="linkasbutton-secondary" href="/rg/action-box-title/update-data/updates?auto=legacy/title/tt0133093/">Update Data</a>
</div>

<h6 style="margin-top: 4px">Quicklinks</h6><form><select id="quicklinks_select" onchange="document.location = this.options[this.selectedIndex].value">
<option value="maindetails">main details</option><option value="combined">combined details</option><option value="fullcredits">full cast and crew</option><option value="companycredits">company credits</option><option value="tvschedule">tv schedule</option><option value="usercomments">user comments</option><option value="externalreviews">external reviews</option><option value="newsgroupreviews">newsgroup reviews</option><option value="awards">awards</option><option value="ratings">user ratings</option><option value="parentalguide">parents guide</option><option value="recommendations">recommendations</option><option value="board">message board</option><option value="plotsummary">plot summary</option><option value="synopsis">plot synopsis</option><option value="keywords">plot keywords</option><option value="amazon">Amazon.com summary</option><option value="quotes">memorable quotes</option><option value="trivia">trivia</option><option value="goofs">goofs</option><option value="soundtrack">soundtrack listing</option><option value="crazycredits">crazy credits</option><option value="alternateversions">alternate versions</option><option value="movieconnections">movie connections</option><option value="faq">FAQ</option><option value="sales">merchandising links</option><option value="business">box office/business</option><option value="releaseinfo">release dates</option><option value="locations">filming locations</option><option value="technical">technical specs</option><option value="laserdisc">laserdisc details</option><option value="dvd">DVD details</option><option value="literature">literature listings</option><option value="news">NewsDesk</option><option value="taglines">taglines</option><option value="trailers">trailers and videos</option><option value="posters" selected>posters</option><option value="photogallery">photo gallery</option><option value="officialsites">official sites</option><option value="miscsites">miscellaneous</option><option value="photosites">photographs</option><option value="soundsites">sound clips</option><option value="videosites">video clips</option>

</select></form>
<h6>Top Links</h6>
<a onClick="(new Image()).src='/rg/title-top-links/trailers/images/b.gif?link=/title/tt0133093/trailers';" href="/title/tt0133093/trailers" class="link">trailers and videos</a><a onClick="(new Image()).src='/rg/title-top-links/fullcredits/images/b.gif?link=/title/tt0133093/fullcredits';" href="/title/tt0133093/fullcredits" class="link">full cast and crew</a><a onClick="(new Image()).src='/rg/title-top-links/trivia/images/b.gif?link=/title/tt0133093/trivia';" href="/title/tt0133093/trivia" class="link">trivia</a><a onClick="(new Image()).src='/rg/title-top-links/officialsites/images/b.gif?link=/title/tt0133093/officialsites';" href="/title/tt0133093/officialsites" class="link">official sites</a><a onClick="(new Image()).src='/rg/title-top-links/quotes/images/b.gif?link=/title/tt0133093/quotes';" href="/title/tt0133093/quotes" class="link">memorable quotes</a>
<h6>Overview</h6>
<a href="maindetails" class="link">main details</a><a href="combined" class="link">combined details</a><a href="fullcredits" class="link">full cast and crew</a><a href="companycredits" class="link">company credits</a><a href="tvschedule" class="link">tv schedule</a>

<h6>Awards & Reviews</h6>
<a href="usercomments" class="link">user comments</a><a href="externalreviews" class="link">external reviews</a><a href="newsgroupreviews" class="link">newsgroup reviews</a><a href="awards" class="link">awards</a><a href="ratings" class="link">user ratings</a><a href="parentalguide" class="link">parents guide</a><a href="recommendations" class="link">recommendations</a><a href="board" class="link">message board</a>
<h6>Plot & Quotes</h6>
<a href="plotsummary" class="link">plot summary</a><a href="synopsis" class="link">plot synopsis</a><a href="keywords" class="link">plot keywords</a><a href="amazon" class="link">Amazon.com summary</a><a href="quotes" class="link">memorable quotes</a>

<h6>Fun Stuff</h6>
<a href="trivia" class="link">trivia</a><a href="goofs" class="link">goofs</a><a href="soundtrack" class="link">soundtrack listing</a><a href="crazycredits" class="link">crazy credits</a><a href="alternateversions" class="link">alternate versions</a><a href="movieconnections" class="link">movie connections</a><a href="faq" class="link">FAQ</a>
<h6>Other Info</h6>

  <a href="sales" class="link">merchandising links</a><a href="business" class="link">box office/business</a><a href="releaseinfo" class="link">release dates</a><a href="locations" class="link">filming locations</a><a href="technical" class="link">technical specs</a><a href="laserdisc" class="link">laserdisc details</a><a href="dvd" class="link">DVD details</a><a href="literature" class="link">literature listings</a><a href="news" class="link">NewsDesk</a>

  <h6>Promotional</h6>
  <a href="taglines" class="link">taglines</a>
  <a href="trailers" class="link">trailers and videos</a>
  <a href="posters" class="link selected">posters</a>
  <a href="photogallery" class="link">photo gallery</a>
  

<h6>External Links</h6>

<a href="cinemashowtimes" class="link empty">showtimes</a><a href="officialsites" class="link">official sites</a><a href="miscsites" class="link">miscellaneous</a><a href="photosites" class="link">photographs</a><a href="soundsites" class="link">sound clips</a><a href="videosites" class="link">video clips</a>



</div>
<div id="tn15main">

<div id="tn15title">
<h1><small>Posters for<br></small><a class="main" href="/title/tt0133093/">The Matrix</a> <span>(<a href="/Sections/Years/1999/">1999</a>) <span class="pro-link"><a href="http://pro.imdb.com/rg/posters-title/tconst-pro-header-link/title/tt0133093/">More at IMDb Pro &raquo;</a></span></span></h1>

</div>

<div id="tn15content">

<div id="tn15adrhs">



<!-- begin TOP_RHS -->
<div id="top_rhs_wrapper">
<script language="JavaScript" type="text/javascript">

//<![CDATA[
document.write('<iframe src="/images/a/ifb/doubleclick/expand.html#imdb.consumer.title/;tile=4;sz=300x250,300x600,160x600,171x600;p=tr;g=th;g=ad;k=m;g=ac;m=R;g=sf;tt=f;k=r;k=p;id=tt0133093;coo=usa;k=c;g=baa;ord=' + ord + '?" id="top_rhs" name="top_rhs" width="0" height="0" marginwidth="0" marginheight="0" frameborder="0" scrolling="no" allowtransparency="true" onload="ad_utils.resize_iframe(this)">');
if (navigator.userAgent.indexOf("Gecko")==-1)
{document.write('<script language="JavaScript" src="http://ad.doubleclick.net/adj/imdb.consumer.title/;tile=4;sz=300x250,300x600,160x600,171x600;abr=!ie;p=tr;g=th;g=ad;k=m;g=ac;m=R;g=sf;tt=f;k=r;k=p;id=tt0133093;coo=usa;k=c;g=baa;ord=' + ord + '?" type="text/javascript"><\/script>');
}
document.write('</iframe>');

//]]>
</script>
<noscript><a href="http://ad.doubleclick.net/jump/imdb.consumer.title/;tile=4;sz=300x250,300x600,160x600,171x600;p=tr;g=th;g=ad;k=m;g=ac;m=R;g=sf;tt=f;k=r;k=p;id=tt0133093;coo=usa;k=c;g=baa;ord=129034736832?" target="_blank"><img src="http://ad.doubleclick.net/ad/imdb.consumer.title/;tile=4;sz=300x250,300x600,160x600,171x600;p=tr;g=th;g=ad;k=m;g=ac;m=R;g=sf;tt=f;k=r;k=p;id=tt0133093;coo=usa;k=c;g=baa;ord=129034736832?"  border="0" alt="advertisement" /></a></noscript>

</div>
<!-- End TOP_RHS --><div id="top_rhs_after" class="after_ad hidden">advertisement</div>



</div>
 

<p>
Poster images shown are from 
<a href="http://www.nostalgia.com/">The Nostalgia Factory</a>.  
Duplication for use elsewhere is prohibited without express permission.
</p>
<table valign="center" border="0" cellspacing="10" cellpadding="0">

 <tr>
  <td valign="top">
   <table border="0" cellpadding="0" cellspacing="0" background="http://posters.imdb.com/posters/m/matrix1.jpg"><td><td><a href="http://www.nostalgia.com/"><img src="http://i.imdb.com/Icons/poster_under_licence.gif" border="0" width="144" height="221" alt="Image courtesy nostalgia.com"></a></td></tr></table>

   
  </td>
  <td><b>us<br>1 sheet<br><br>&#34;On April 2nd, the fight for the future begins.&#34;<br></b></td>
 </tr>

 <tr>
  <td valign="top">
   <table border="0" cellpadding="0" cellspacing="0" background="http://posters.imdb.com/posters/m/matrix1999_54226.jpg"><td><td><a href="http://www.nostalgia.com/nf_moreinfo.html?sku=54226"><img src="http://i.imdb.com/Icons/poster_under_licence.gif" border="0" width="216" height="323" alt="Buy this from nostalgia.com"></a></td></tr></table>
   <br><center><small><a href="http://www.nostalgia.com/nf_moreinfo.html?sku=54226">buy this from nostalgia.com</a></small></center>

  </td>
  <td><b>pl<br>1 sheet movie poster app. 27&#34; x 40&#34;<br><br><br></b></td>
 </tr>

 <tr>
  <td valign="top">
   <table border="0" cellpadding="0" cellspacing="0" background="http://posters.imdb.com/posters/m/matrix1999_47005.jpg"><td><td><a href="http://www.nostalgia.com/"><img src="http://i.imdb.com/Icons/poster_under_licence.gif" border="0" width="216" height="329" alt="Image courtesy nostalgia.com"></a></td></tr></table>

   
  </td>
  <td><b>us<br>1 sheet movie poster app. 27&#34; x 40&#34;<br><br>Poster for video release<br></b></td>
 </tr>

 <tr>
  <td valign="top">
   <table border="0" cellpadding="0" cellspacing="0" background="http://posters.imdb.com/posters/m/matrixge39848.jpg"><td><td><a href="http://www.nostalgia.com/"><img src="http://i.imdb.com/Icons/poster_under_licence.gif" border="0" width="216" height="305" alt="Image courtesy nostalgia.com"></a></td></tr></table>

   
  </td>
  <td><b>de<br>A0 movie poster - 84 x 118 cm or 33 x 46 inches<br><br><br></b></td>
 </tr>

 <tr>
  <td valign="top">
   <table border="0" cellpadding="0" cellspacing="0" background="http://posters.imdb.com/posters/m/matrix39848.jpg"><td><td><a href="http://www.nostalgia.com/"><img src="http://i.imdb.com/Icons/poster_under_licence.gif" border="0" width="216" height="317" alt="Image courtesy nostalgia.com"></a></td></tr></table>
   
  </td>

  <td><b>de<br>A0, 33 x 47 Movie Poster<br><br><br></b></td>
 </tr>

 <tr>
  <td valign="top">
   <table border="0" cellpadding="0" cellspacing="0" background="http://posters.imdb.com/posters/m/matrix40503.jpg"><td><td><a href="http://www.nostalgia.com/"><img src="http://i.imdb.com/Icons/poster_under_licence.gif" border="0" width="216" height="297" alt="Image courtesy nostalgia.com"></a></td></tr></table>
   
  </td>
  <td><b>fr<br>Grande Movie Poster, 47 x 63<br><br><br></b></td>

 </tr>

 <tr>
  <td valign="top">
   <table border="0" cellpadding="0" cellspacing="0" background="http://posters.imdb.com/posters/m/matrix1999_49262.jpg"><td><td><a href="http://www.nostalgia.com/nf_moreinfo.html?sku=49262"><img src="http://i.imdb.com/Icons/poster_under_licence.gif" border="0" width="216" height="459" alt="Buy this from nostalgia.com"></a></td></tr></table>
   <br><center><small><a href="http://www.nostalgia.com/nf_moreinfo.html?sku=49262">buy this from nostalgia.com</a></small></center>
  </td>
  <td><b>it<br>Locandina 13&#34; x 27&#34;<br><br><br></b></td>

 </tr>

 <tr>
  <td valign="top">
   <table border="0" cellpadding="0" cellspacing="0" background="http://posters.imdb.com/posters/m/matrixmini.jpg"><td><td><a href="http://www.nostalgia.com/"><img src="http://i.imdb.com/Icons/poster_under_licence.gif" border="0" width="216" height="326" alt="Image courtesy nostalgia.com"></a></td></tr></table>
   
  </td>
  <td><b>us<br>Mini, 17 X 25<br><br>On March 31st, the fight for the future begins.,&#34;<br></b></td>
 </tr>

 <tr>
  <td valign="top">
   <table border="0" cellpadding="0" cellspacing="0" background="http://posters.imdb.com/posters/m/matrixq.jpg"><td><td><a href="http://www.nostalgia.com/"><img src="http://i.imdb.com/Icons/poster_under_licence.gif" border="0" width="216" height="326" alt="Image courtesy nostalgia.com"></a></td></tr></table>
   
  </td>
  <td><b>us<br>Mini, 17 X 25<br><br>On March 31st, the fight for the future begins.<br></b></td>
 </tr>

 <tr>
  <td valign="top">
   <table border="0" cellpadding="0" cellspacing="0" background="http://posters.imdb.com/posters/m/matrixquad.jpg"><td><td><a href="http://www.nostalgia.com/"><img src="http://i.imdb.com/Icons/poster_under_licence.gif" border="0" width="293" height="216" alt="Image courtesy nostalgia.com"></a></td></tr></table>
   
  </td>
  <td><b>uk<br>Quad<br><br><br></b></td>
 </tr>

</table>
<hr/>

<p><h2>Posters on other sites</h2></p>
<ul>
<li><a href="http://carteles.metropoliglobal.com/4planti.php?id=1859">(carteles.metropoliglobal.com)</a></li><li><a href="http://filmbyen.net/film_poster.php?film=253">(Filmbyen.net - Poster)</a></li><li><a href="http://online.prevezanos.com/skf/poster/poster.php3?id=621">(Schr&#246;ders kleine Filmseiten [de] (english))</a></li><li><a href="http://online.prevezanos.com/skf/poster/poster.php3?id=693">(Schr&#246;ders kleine Filmseiten [de] (german))</a></li><li><a href="http://posters.motechnet.com/title/tt0133093/">(MoTechPosters)</a></li><li><a href="http://www.impawards.com/1999/matrix_ver4.html">(Theatrical Movie Posters)</a></li><li><a href="http://www.movieposterdb.com/movie/0133093/The_Matrix.htm">(MoviePosterDB.com)</a></li><li><a href="http://www.sms.cz/film/matrix/fotogaleriex">(SMS.cz - Hi resolution movie posters/covers (Czech))</a></li><li><a href="http://www.trailerfan.com/movie/the_matrix/posters">(Trailerfan.com - Posters)</a></li><li><a href="http://www.zoomavant.com/dossier/03/matrix/matrix1.htm">(zoomavant.com poster)</a></li>
</ul>

<p>
For further information on original movie posters, please visit 
<a href="http://www.nostalgia.com">The Nostalgia Factory</a>
</p>
<hr/><h3>Related Links</h3><table>
<tr><td width="33%" style="width: 400px"> <a href="/title/tt0133093/trailers" onClick="(new Image()).src='/rg/title-related/posters-trailers/images/b.gif?link=/title/tt0133093/trailers';">Trailers</a></td><td width="33%" style="width: 400px"> <a href="/title/tt0133093/photogallery" onClick="(new Image()).src='/rg/title-related/posters-photogallery/images/b.gif?link=/title/tt0133093/photogallery';">Photo gallery</a></td><td width="33%" style="width: 400px"> <a href="/title/tt0133093/photosites" onClick="(new Image()).src='/rg/title-related/posters-photosites/images/b.gif?link=/title/tt0133093/photosites';">Photo links</a></td></tr><tr><td width="33%" style="width: 400px"> <a href="/title/tt0133093/officialsites" onClick="(new Image()).src='/rg/title-related/posters-officialsites/images/b.gif?link=/title/tt0133093/officialsites';">Official site</a></td><td width="33%" style="width: 400px"> <a href="/title/tt0133093/maindetails" onClick="(new Image()).src='/rg/title-related/posters-maindetails/images/b.gif?link=/title/tt0133093/maindetails';">Main details</a></td><td width="33%" style="width: 400px"> <a href="/Sections/Posters/" onClick="(new Image()).src='/rg/title-related/posters-sections/images/b.gif?link=/Sections/Posters/';">IMDb posters section</a></td></tr><tr><td colspan="3" style="padding-top: 4px">Browse titles with posters by letter<br/>&nbsp;&nbsp;&nbsp;<a href="/Sections/Posters/A" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/A';">A</a> <a href="/Sections/Posters/B" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/B';">B</a> <a href="/Sections/Posters/C" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/C';">C</a> <a href="/Sections/Posters/D" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/D';">D</a> <a href="/Sections/Posters/E" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/E';">E</a> <a href="/Sections/Posters/F" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/F';">F</a> <a href="/Sections/Posters/G" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/G';">G</a> <a href="/Sections/Posters/H" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/H';">H</a> <a href="/Sections/Posters/I" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/I';">I</a> <a href="/Sections/Posters/J" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/J';">J</a> <a href="/Sections/Posters/K" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/K';">K</a> <a href="/Sections/Posters/L" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/L';">L</a> <a href="/Sections/Posters/M" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/M';">M</a> <a href="/Sections/Posters/N" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/N';">N</a> <a href="/Sections/Posters/O" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/O';">O</a> <a href="/Sections/Posters/P" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/P';">P</a> <a href="/Sections/Posters/Q" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/Q';">Q</a> <a href="/Sections/Posters/R" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/R';">R</a> <a href="/Sections/Posters/S" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/S';">S</a> <a href="/Sections/Posters/T" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/T';">T</a> <a href="/Sections/Posters/U" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/U';">U</a> <a href="/Sections/Posters/V" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/V';">V</a> <a href="/Sections/Posters/W" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/W';">W</a> <a href="/Sections/Posters/X" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/X';">X</a> <a href="/Sections/Posters/Y" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/Y';">Y</a> <a href="/Sections/Posters/Z" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/Z';">Z</a> <a href="/Sections/Posters/Other" onClick="(new Image()).src='/rg/title-related/posters-browse/images/b.gif?link=/Sections/Posters/Other';">Other</a> </td></tr>

</table>
<hr/>
<div align="center">


</div>
<p class="disclaimer">The Internet Movie Database accepts no responsibility for the content of the external sites linked from this page or for products offered or purchased from participating companies.</p>

</div>
</div> 
</div> 
<br style="clear:left;" />
</div>

<div id="footer" class="ft">
<hr width="100%" size=1>

<p class="footer" align="center">
<a href="/">Home</a>&nbsp;
  | <a href="/search">Search</A>&nbsp;
  | <a href="/NowPlaying/">Now Playing</a>&nbsp;
  | <a href="/News/">News</A>&nbsp;
  | <a href="/register/?why=mymovies_footer">My Movies</A>&nbsp;

  | <a href="/Games/">Games</A>&nbsp;
  | <a href="/boards/">Boards</A>&nbsp;
| <a href="/help/">Help</a>&nbsp;
  | <A HREF="/Showtimes">US&nbsp;Movie&nbsp;Showtimes</A>&nbsp;

| <A HREF="/top_250_films">Top 250</A>&nbsp;
| <a href="/register/?why=footer">Register</a>&nbsp;
  | <A HREF="/recommends/">Recommendations</A>&nbsp;
  | <A HREF="/widgets/">Widgets</A><br>
  <A HREF="/Charts/">Box&nbsp;Office</A> 
  | <A HREF="/a2z">Index</A> 
  | <A HREF="/Sections/Trailers/">Trailers</A> 
  
  | <a href="/jobs"><b>Jobs</b></a>&nbsp;

  | <a href="https://secure.imdb.com/register/subscribe?c=a394d4442664f6f6475627" onClick="(new Image()).src='/rg/PRO_FOOT/FOOTER/images/b.gif?link=https://secure.imdb.com/register/subscribe?c=a394d4442664f6f6475627';">
    <span style="color:#cc3333"><b>IMDbPro.com&nbsp;-&nbsp;Free&nbsp;Trial</b></span></a> 
  | <a href="http://resume.imdb.com" onClick="(new Image()).src='/rg/resume-footer/footer/images/b.gif?link=http://resume.imdb.com';"><span style="color:#cc3333"><b>IMDb Resume</b></span></a>
<br><br>
<a href="/help/show_article?conditions">Copyright &copy;</a> 1990-2008 
<a href="/help/">IMDb.com, Inc.</a><br>

<a href="/help/show_article?conditions">Terms</a> and <a href="/privacy">Privacy Policy</a> under which this service is provided to you.<br>
An <a href="http://www.amazon.com/exec/obidos/redirect-home/internetmoviedat"><img align="middle" width="86" height="18" border="0" src="http://i.media-imdb.com/images/icons/amazon_logo.gif" alt="Amazon.com"></a> company.&nbsp;
<a href="/advertising/">Advertise</a> on IMDb.&nbsp;
<a href="/tiger_redirect?FT_LIC&/licensing/">License</a> our content.

</p>
<p class="footer" align="center">IMDb is powered by Perl and <b><a href="/rg/jobs/footer-pbp//help/show_leaf?jobatimdb">we are hiring</a></b>!</p>
</div>

</layer>
</div>



<!-- begin BOTTOM_AD -->
<div id="bottom_ad_wrapper">
<script language="JavaScript" type="text/javascript">

//<![CDATA[
document.write('<iframe src="/images/a/ifb/doubleclick/expand.html#imdb.consumer.title/;tile=5;sz=728x90;p=b;g=th;g=ad;k=m;g=ac;m=R;g=sf;tt=f;k=r;k=p;id=tt0133093;coo=usa;k=c;g=baa;ord=' + ord + '?" id="bottom_ad" name="bottom_ad" width="0" height="0" marginwidth="0" marginheight="0" frameborder="0" scrolling="no" allowtransparency="true" onload="ad_utils.resize_iframe(this)">');
if (navigator.userAgent.indexOf("Gecko")==-1)
{document.write('<script language="JavaScript" src="http://ad.doubleclick.net/adj/imdb.consumer.title/;tile=5;sz=728x90;abr=!ie;p=b;g=th;g=ad;k=m;g=ac;m=R;g=sf;tt=f;k=r;k=p;id=tt0133093;coo=usa;k=c;g=baa;ord=' + ord + '?" type="text/javascript"><\/script>');
}
document.write('</iframe>');

//]]>
</script>
<noscript><a href="http://ad.doubleclick.net/jump/imdb.consumer.title/;tile=5;sz=728x90;p=b;g=th;g=ad;k=m;g=ac;m=R;g=sf;tt=f;k=r;k=p;id=tt0133093;coo=usa;k=c;g=baa;ord=129034736832?" target="_blank"><img src="http://ad.doubleclick.net/ad/imdb.consumer.title/;tile=5;sz=728x90;p=b;g=th;g=ad;k=m;g=ac;m=R;g=sf;tt=f;k=r;k=p;id=tt0133093;coo=usa;k=c;g=baa;ord=129034736832?"  border="0" alt="advertisement" /></a></noscript>

</div>
<!-- End BOTTOM_AD -->





<!-- sid : 78242 : BOTTOM_SCRIPT -->
<SCRIPT language='JavaScript'>
var rnd = Math.round(Math.random()*10000000);
var https = false; try { https = document.location.href.indexOf('https')==0 } catch(e) {}
document.writeln('<IFRAME src="http'+(https?'s':'')+'://media.adrevolver.com/adrevolver/trace?sip=78&cpy='+rnd+'" width="1" height="1" frameborder="0" marginheight="0" marginwidth="0"></IFRAME>');
</SCRIPT>



<img src="/rd/?q=50403000000030a090f29616f226e276966600000010c6a0e02303038313130393c273832343230000001037a040379646370000001047&cb=122628424029244" width="1" height="1" alt="" border="0">
</div> <!-- id="wrapper" -->

</body>
</html>"""

        return result