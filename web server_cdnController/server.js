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

var __projectRoot = 'public/src';

app.use(express.static(__projectRoot));
app.use('/node_modules', express.static('public/node_modules'));

app.get('/', function (req, res) {
    res.sendFile(path.join(__projectRoot + '/index.html'));
});

app.get('/cdn', function (req, res) {
	var resultCDN = {};
  	var findDocument = function(db, callback) {
		db.collection('origins').find().toArray(function(err, result) {
			assert.equal(err, null);
			console.log(result)
			resultCDN = result;
			callback();
		});
	};
	MongoClient.connect(url, function(err, db) {
		assert.equal(null, err);
		findDocument(db, function() {
			db.close();
			res.writeHead(200, {"Content-Type": "application/json"});
			res.end(JSON.stringify(resultCDN));
		});
	});
});

app.post('/addOrigin', function (req, res) {
	var ipOrigin = req.body.ipOrigin;
	var portOrigin = req.body.portOrigin;
	var transport = req.body.transport;
	console.log("datos: " + ipOrigin + " " + portOrigin + " " + transport);
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
	var options = {
		uri: 'http://192.168.56.101:8080/deleteOrigin',
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
				var removeDocument = function(db, callback) {
					db.collection('origins').remove( {
						"ip": ipOrigin,
						"port": portOrigin,
						"transport": transport
					}, function(err, result) {
						assert.equal(err, null);
						console.log("Inserted a document into the origins collection.");
						callback();
					});
				};

				MongoClient.connect(url, function(err, db) {
					assert.equal(null, err);
					removeDocument(db, function() {
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
});

app.post('/addSurrogate', function (req, res) {
	var ipOrigin = req.body.ipOrigin;
	var portOrigin = req.body.portOrigin;
	var transport = req.body.transport;
	var ipSurrogate = req.body.ipSurrogate;
	var portSurrogate = req.body.portSurrogate;
	var options = {
		uri: 'http://192.168.56.101:8080/addSurrogate',
		method: 'POST',
		json: {
			"ipOrigin": ipOrigin,
			"portOrigin": portOrigin,
			"transport": transport,
			"ipSurrogate": ipSurrogate,
			"portSurrogate": portSurrogate
		}
	};
	request(options, function (error, response, body) {
		if (!error && response.statusCode == 200) {
			console.log(body);
			res.writeHead(200, {"Content-Type": "application/json"});
			if (body.Result == true) {
				var surrogates = [];
				var findDocument = function(db, callback) {
					db.collection('origins').findOne( {
						"ip": ipOrigin,
						"port": portOrigin,
						"transport": transport	
					}, function(err, result) {
						assert.equal(err, null);
						surrogates = result.surrogates;
						callback();
					});
				};
				var updateDocument = function(db, callback) {
					db.collection('origins').update( {
						"ip": ipOrigin,
						"port": portOrigin,
						"transport": transport
					},{$set: {"surrogates":surrogates}	
					}, function(err, result) {
						assert.equal(err, null);
						console.log("Inserted a document into the origins collection.");
						callback();
					});
				};

				MongoClient.connect(url, function(err, db) {
					assert.equal(null, err);
					findDocument(db, function() {
						surrogates.push({"ip": ipSurrogate, "port": portSurrogate});
						console.log(surrogates);
						updateDocument(db, function() {
							db.close();
						});
					});
				});
			}
			res.end(JSON.stringify(body));
		}
		else {
			res.sendStatus(500);
		}
	});		
});

app.post('/deleteSurrogate', function (req, res) {
	var ipOrigin = req.body.ipOrigin;
	var portOrigin = req.body.portOrigin;
	var transport = req.body.transport;
	var ipSurrogate = req.body.ipSurrogate;
	var portSurrogate = req.body.portSurrogate;
	var options = {
		uri: 'http://192.168.56.101:8080/deleteSurrogate',
		method: 'POST',
		json: {
			"ipOrigin": ipOrigin,
			"portOrigin": portOrigin,
			"transport": transport,
			"ipSurrogate": ipSurrogate,
			"portSurrogate": portSurrogate
		}
	};
	request(options, function (error, response, body) {
		if (!error && response.statusCode == 200) {
			console.log(body);
			res.writeHead(200, {"Content-Type": "application/json"});
			if (body.Result == true) {
				var surrogates = [];
				var findDocument = function(db, callback) {
					db.collection('origins').findOne( {
						"ip": ipOrigin,
						"port": portOrigin,
						"transport": transport	
					}, function(err, result) {
						assert.equal(err, null);
						surrogates = result.surrogates;
						callback();
					});
				};
				var updateDocument = function(db, callback) {
					db.collection('origins').update( {
						"ip": ipOrigin,
						"port": portOrigin,
						"transport": transport
					},{$set: {"surrogates":surrogates}	
					}, function(err, result) {
						assert.equal(err, null);
						console.log("Inserted a document into the origins collection.");
						callback();
					});
				};

				MongoClient.connect(url, function(err, db) {
					assert.equal(null, err);
					findDocument(db, function() {
						//surrogates.push({"ip": ipSurrogate, "port": portSurrogate});
						for (index = 0; index < surrogates.length; ++index) {
    							//console.log(a[index]);
							if ((surrogates[index].port == portSurrogate) && (surrogates[index].ip == ipSurrogate)) {
								surrogates.splice(index, 1);
								break;
							}
						}
						console.log(surrogates);
						updateDocument(db, function() {
							db.close();
						});
					});
				});
			}
			res.end(JSON.stringify(body));
		}
		else {
			res.sendStatus(500);
		}
	});
});

app.listen(3000, function () {
	console.log('Example app listening on port 3000!');
});
