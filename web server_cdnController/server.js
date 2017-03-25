var express = require('express');
var bodyParser = require('body-parser');
var request = require('request');

var app = express();

app.use( bodyParser.json() );       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
  extended: true
})); 

app.get('/', function (req, res) {
  	res.send('Hello World!');
});

app.get('/cdn', function (req, res) {
  	res.send('cdn');
});

app.post('/addOrigin', function (req, res) {
	var ipOrigin = req.body.ipOrigin;
	var portOrigin = req.body.portOrigin;
	var transport = req.body.transport;
	var options = {
		uri: 'http://192.168.56.101:8080/addOrigin',
		method: 'POST',
		json: {
			"ipOrigin": ipOrigin,
			"portOrigin": portOrigin,
			"transport": transport
		}
	};
	request(options, function (error, response, body) {
		if (!error && response.statusCode == 200) {
			console.log(body);
		}
	});
	res.sendStatus(200);
});

app.post('/deleteOrigin', function (req, res) {
	var ipOrigin = req.body.ipOrigin;
	var portOrigin = req.body.portOrigin;
	var transport = req.body.transport;
	res.sendStatus(200);
});

app.post('/addSurrogate', function (req, res) {
	var ipOrigin = req.body.ipOrigin;
	var portOrigin = req.body.portOrigin;
	var transport = req.body.transport;
	var ipSurrogate = req.body.ipSurrogate;
	var portSurrogate = req.body.portSurrogate;
	res.sendStatus(200);
});

app.post('/deleteSurrogate', function (req, res) {
	var transport = req.body.transport;
	var ipSurrogate = req.body.ipSurrogate;
	var portSurrogate = req.body.portSurrogate;
	res.sendStatus(200);
});

app.listen(3000, function () {
	console.log('Example app listening on port 3000!');
});
