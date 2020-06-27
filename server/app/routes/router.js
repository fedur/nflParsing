var express = require('express');
var app = express(); 
var router = express.Router();

router.get('/', function(req,res,next){
	res.set('Content-Type', 'text/html');
	res.send(new Buffer('<h2>Test String</h2>'));
});

module.exports = router;