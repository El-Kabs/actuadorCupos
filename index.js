const fetch = require('node-fetch');
var sleep = require('system-sleep');

while(1===1){
  fetch('https://cuposuniandes.herokuapp.com/escribir')
              .then(function(response) {
                return response.json();
              });
  sleep(300000);
}
