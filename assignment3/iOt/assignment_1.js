var previous_value =0;
var sumof_10vals = 0;
var prev_avg = 0;
var index = 0;
var http = require('http');

function getRandomArbitrary(min, max) {
  return Math.random() * (max - min) + min;
}

function generateRandomForSingleNumber() {
  var randomnumber = getRandomArbitrary(0,5);
  processReadingOnIoTDeviceSingleMeasurement(randomnumber);
}

function generateRandomBulk() { 
 var randomnumber = getRandomArbitrary(0,5); 
 processReadingOnIoTDeviceBulk(randomnumber);
}

function processReadingOnIoTDeviceSingleMeasurement(randomnumber){
  var dateFormat = require('dateformat');
  var now=dateFormat(new Date(), "yyyy-mm-dd HH:MM:ss");
	
  delta = randomnumber - previous_value;
  if (delta < -0.1){
    delta = delta * -1;
  }
 
  console.log("random number: "+randomnumber+" delta:"+delta);
  // if delta > 0.1, then send to edge node
  if (delta > 0.1){
    sendToEdgeNode(randomnumber,now);
	console.log(randomnumber);
  }
  previous_value = randomnumber;
}

function processReadingOnIoTDeviceBulk(randomnumber){
  var dateFormat = require('dateformat');
  var now=dateFormat(new Date(), "yyyy-mm-dd HH:MM:ss");
	
 console.log("Random number: "+randomnumber+" iteration:"+(index+1));
 if (index <9){
	sumof_10vals = sumof_10vals + randomnumber;
	index ++;
  }
 else {
   sumof_10vals = sumof_10vals + randomnumber;
   current_avg_sma = sumof_10vals/10;
   delta = current_avg_sma - prev_avg;


   if (delta < -0.5){
	  delta = delta * -1;
   }
   console.log("current avg: "+current_avg_sma+" previous avg:"+(prev_avg)+" delta:"+delta);

   // if delta > 0.1, then send to edge node
   if (delta > 0.5){
	 sendToEdgeNode(current_avg_sma,now);
	 console.log(current_avg_sma);
   }
  index = 0;
  sumof_10vals = 0;
  prev_avg = current_avg_sma;
 }
}

function sendToEdgeNode(sma,dt){
  console.log("sendToEdgeNode: "+dt);
  var ThingSpeakClient = require('thingspeakclient');
  var client = new ThingSpeakClient({server:'https://api.thingspeak.com'});
  
  client.attachChannel(383403, {writeKey:'XIZ8L2QV95FZLKZD'});
  client.updateChannel(383403, {field1: sma, field2:dt}, function(err, resp) {
    if (!err && resp > 0) {
        console.log('update successfully. Entry number was: ' + resp);
    }
     else {
      console.log(err);
    }
  });
}

setInterval(generateRandomForSingleNumber, 1000);
//setInterval(generateRandomBulk, 1000);
