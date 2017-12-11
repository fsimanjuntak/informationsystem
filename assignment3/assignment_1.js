var previous_value =0;
var sumof_10vals = 0;
var prev_avg = 0;
var index = 0;

function getRandomArbitrary(min, max) {
  return Math.random() * (max - min) + min;
}

function generateRandomForSingleNumber() {
  var randomnumber = getRandomArbitrary(0,5);
  delta = randomnumber - previous_value;
  if (delta < -0.1){
    delta = delta * -1;
  }
 
  console.log("random number: "+randomnumber+" delta:"+delta);
  if (delta > 0.1){
    processReadingOnIoTDevice(randomnumber);
  }
  previous_value = randomnumber;
}

function generateRandomBulk() { 
 var randomnumber = getRandomArbitrary(0,5); 
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
    
   if (delta > 0.5){
    processReadingOnIoTDevice(current_avg_sma);
   }
  index = 0;
  sumof_10vals = 0;
  prev_avg = current_avg_sma;
 }
}

function processReadingOnIoTDevice(val){
  sendToEdgeNode(val);
}

function sendToEdgeNode(data){
  console.log("sendToEdgeNode");
  var ThingSpeakClient = require('thingspeakclient');
  var client = new ThingSpeakClient({server:'https://api.thingspeak.com'});
  
  client.attachChannel(382541, {writeKey:'P7TPFYL97U3GM5UE'});
  client.updateChannel(382541, {field1: data}, function(err, resp) {
    if (!err && resp > 0) {
        console.log('update successfully. Entry number was: ' + resp);
    }
  });
 
}

/*setInterval(generateRandomForSingleNumber, 1000);*/
setInterval(generateRandomBulk, 1000);
