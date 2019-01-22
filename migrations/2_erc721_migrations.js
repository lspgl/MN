const estate = artifacts.require("./estate.sol");

module.exports = async function(deployer) {
  await deployer.deploy(estate, "estate", "estate")
  const erc721 = await estate.deployed()
};
