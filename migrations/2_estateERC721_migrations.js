const MyERC721 = artifacts.require("./estateERC721.sol");

module.exports = async function(deployer) {
  await deployer.deploy(MyERC721, "MNEstateToken", "MNET")
  const erc721 = await MyERC721.deployed()
};
