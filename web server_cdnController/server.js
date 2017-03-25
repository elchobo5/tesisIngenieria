var express = require('express');
var bodyParser = require('body-parser');
var request = require('request');

var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');
var ObjectId = require('mongodb').ObjectID;
var url = 'mongodb://localhost:27017/test';

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
			res.writeHead(200, {"Content-Type": "application/json"});
			if (body.Result == true) {
				var insertDocument = function(db, callback) {
					db.collection('origins').insertOne( {
						"ip": ipOrigin,
						"port": portOrigin,
						"transport": transport,
						"surrogates": []
					}, function(err, result) {
						assert.equal(err, null);
						console.log("Inserted a document into the origins collection.");
						callback();
					});
				};

				MongoClient.connect(url, function(err, db) {
					assert.equal(null, err);
					insertDocument(db, function() {
					db.close();
					});
				});
			}
			res.end(JSON.stringify(body));
		}
		else {
			res.sendStatus(500);
		}
	});		
	//res.sendStatus(200);
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
