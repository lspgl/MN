pragma solidity >0.4.24;

import "../node_modules/openzeppelin-solidity/contracts/token/ERC721/ERC721.sol";
import "../node_modules/openzeppelin-solidity/contracts/token/ERC721/ERC721Metadata.sol";


contract estate is ERC721Metadata{
    constructor(string memory _name, string memory _symbol) public ERC721Metadata(_name, _symbol){}

    function mintUniqueTokenTo(
      address _to,
      uint256 _tokenID,
      string memory _tokenURI
    ) public
    {
      super._mint(_to, _tokenID);
      super._setTokenURI(_tokenID, _tokenURI);
    }
}
