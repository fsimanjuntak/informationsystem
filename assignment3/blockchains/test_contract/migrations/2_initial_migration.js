var Coin = artifacts.require("./Survey.sol");

module.exports = function(deployer) {
  deployer.deploy(Coin);
};
