import * as Express from 'express';
import * as Web3 from 'web3';
import * as bodyParser from 'body-parser';

import App from './app';

const port = 3001;
const express = Express();

const app = new App();


// parse application/x-www-form-urlencoded
express.use(bodyParser.urlencoded({ extended: true })); //enable post request

// parse application/json
express.use(bodyParser.json());


express.get('/', (req, res) => {
    res.json({msg: "Hello World!"});
});

express.get('/accounts', (req, res) => {
  app.accounts((res2) => {
    res.json(res2);
  });
});

express.get('/accountInfo', (req, res) => {
  app.accountInfo(req.query.a, (res2) => {
    res.json(res2);
  });
});

express.get('/sendValue', (req, res) => {
  app.sendValue(req.query.f, req.query.p, req.query.t, req.query.a, (res2) => {
    res.json(res2);
  });
});

express.post('/sendValue', (req, res) => {
  console.log(req.body);
  app.sendValue(req.body.f, req.body.p, req.body.t, req.body.a, (res2) => {
    res.json(res2);
  });
});


// exp.use('/article', article);
// exp.use('/auth', auth);
// exp.use('/user', user);

express.listen(port, () => {
    console.log('Listen started at port ' + port);

    // if (Web3.givenProvider) {
    //     console.log("=======Log1");
    //   console.warn("Using web3 detected from external source. If you find that your accounts don't appear or you have 0 MetaCoin, ensure you've configured that source properly. If using MetaMask, see the following link. Feel free to delete this warning. :) http://truffleframework.com/tutorials/truffle-and-metamask")
    //
    //   app.web3 = new Web3(Web3.givenProvider);
    // }
    // else {
     console.log("=======Log2");
     console.warn("No web3 detected. Falling back to http://127.0.0.1:8545. You should remove this fallback when you deploy live, as it's inherently insecure. Consider switching to Metamask for development. More info here: http://truffleframework.com/tutorials/truffle-and-metamask");
     //fallback - use your fallback strategy (local node / hosted node + in-dapp id mgmt / fail)
     //web3 1.0.0 does not support HttpProvider (https://ethereum.stackexchange.com/questions/39890/which-version-of-web3-js-should-i-use)
     //app.web3 = new Web3(new Web3.providers.WebsocketProvider("ws://localhost:8545"));
     //app.web3 = new Web3(new Web3.providers.WebsocketProvider("wss://ropsten.infura.io/hr1s0JoyZSF1c0aA2FoT")); //doesnt work
     app.web3 = new Web3(new Web3.providers.HttpProvider("http://172.23.0.3:8545"));
     //appClass.web3 = new Web3(new Web3.providers.HttpProvider("https://ropsten.infura.io/hr1s0JoyZSF1c0aA2FoT"));

    // }
});

export default express;
