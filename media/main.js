var 
	URL = 'https://spreadsheets.google.com/feeds/list/0Amo7uI8Dglg1dDhsNXhtVEZ4dzZDNWt2SldrYU9LRlE/od6/public/basic?alt=json-in-script';
	
function parseData(data) {
	var 
		entrys = data.feed.entry, i = entrys.length, html = '';

	while (i--) {
		var 
			title = entrys[i].title.$t, 
			author = entrys[i].content.$t,
			add = '';
		if (author !== '') {
			add += ' &mdash; <small>' + author +'</small>';
		}
		if (author.indexOf('date') !== -1) {
			html += '<span class="dagger">&Dagger;</span>'
		}			
		html += '<p>' + title + add + '</p>';
	}
	document.getElementById('bookshelf').innerHTML = html;	
}

function getJson() {
  var 
  	script = document.createElement('script');
  	script.setAttribute('src', URL + '&callback=parseData');
  	script.setAttribute('id', 'jsonScript');
  	script.setAttribute('type', 'text/javascript');
  
  document.documentElement.firstChild.appendChild(script);
}