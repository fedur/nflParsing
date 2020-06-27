
// Express Stuff
var express = require('express');
var bodyParser = require('body-parser');
var mongoose   = require('mongoose');
var morgan = require('morgan');


var app = express()

// Our Stuff
var ErrorHandler = require('./util/ErrorMiddleware');
app.use(ErrorHandler.handleDefaultError);
app.use(morgan('dev'));
//Routing
var router = require('./routes/router');
app.use('/', router);

// START THE SERVER
// =============================================================================
var port = process.env.PORT || 8080;	// set our port
app.listen(port);
console.log('current port: ' + port);