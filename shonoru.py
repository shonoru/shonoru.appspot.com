import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write("""
          <!DOCTYPE HTML>
          <html lang="en-US">
          <head>
              <meta charset="UTF-8">
              <title>Andrey Bodoev &mdash; I'm currently working on something awesome</title>
              <link rel="shortcut icon" href="/media/favicon.ico">
              <link type="text/css" rel="stylesheet" href="/media/main.css" />
              <script src="/media/main.js"></script>
              <script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-20044548-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
          </head>
          <body>
              <div class="wrap">
                  <div class="qr-code">
                    <img src="http://chart.apis.google.com/chart?chs=141x141&cht=qr&chl=Andrey%20Bodoev,%20shonoru@gmail.com%2015210424654&choe=UTF-8" alt="">            
                </div>
                <div class="toc">
                    <h6>Table of Contents</h6>
                    <span>about</span><br>
                    <span>travel</span><br>            
                    <a href="#bookshelf">bookshelf</a><br>
                    <span>portfolio</span>
                </div>
                  <div>
                    <h1><span class="indent">&sect;</span>bookshelf</h1>
                    <div id="bookshelf" style="padding-bottom: 1em;"></div>
                </div>
                <div class="footer">
                    <img src="http://code.google.com/appengine/images/appengine-noborder-120x30.gif" alt="Powered by Google App Engine">
                </div>    
              </div>
              <script type="text/javascript">
                  (function () {
                      getJson();
                  })()
              </script>
              <!-- Yandex.Metrika -->
<div style="display:none;"><script type="text/javascript">
(function(w, c) {
    (w[c] = w[c] || []).push(function() {
        try {
            w.yaCounter2154601 = new Ya.Metrika(2154601);
             yaCounter2154601.clickmap(true);
             yaCounter2154601.trackLinks(true);
        
        } catch(e) {}
    });
})(window, 'yandex_metrika_callbacks');
</script></div>
<script src="//mc.yandex.ru/metrika/watch.js" type="text/javascript" defer="defer"></script>
<noscript><div style="position:absolute"><img src="//mc.yandex.ru/watch/2154601" alt="" /></div></noscript>
<!-- /Yandex.Metrika -->              
          </body>
          </html>""")


application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()