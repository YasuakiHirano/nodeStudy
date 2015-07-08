console.log("--- ejs test start ---");

var http = require('http');
var fs = require('fs');
var ejs = require('ejs');
var li_port= 3000;

var test = fs.readFileSync('./test.ejs', 'utf-8');
var server = http.createServer();
server.on('request', req);
server.listen(li_port);

function req(req, res){
	var output = ejs.render(test ,{title: "!!TITLE!!", content: "this is content"});
	res.writeHead(200, {'Content-Type': 'text/html'});
	res.write(output);
	res.end();
}

console.log("please access is : " + li_port);
console.log("--- ejs test  end  ---");
