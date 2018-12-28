// Allows us to use ES6 in our migrations and tests.
//require('babel-register')
var HDWalletProvider = require("truffle-hdwallet-provider");
var mnemonic = "unable motion select clerk reduce add reform whisper weird unfold oblige doctor";

module.exports = {
  networks: {
    development: {
      host: '172.22.0.2',
      port: 8545,
      network_id: '*', // Match any network id
	  gas: 3000000,
//gasPrice: 10000000
    },
	  
    ropsten: {
      provider: function() {
        return new HDWalletProvider(mnemonic, "https://ropsten.infura.io/hr1s0JoyZSF1c0aA2FoT", 4)
      },
      network_id: 3,
		  gas: 4712388
//gasPrice: 10000000
    }
  }
}
