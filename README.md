# CashCats_filter
This is a simple script to search CashCatsNFT with their traits.

## USAGE:

1. Open and edit the file criteria.json to specify searching criteria;
2. run "python search_cats.py" in command line, python3 is needed;
3. ID of all CashCats that meet the searching criteria will be printed.



## About settings in criteria.json:

- "search_range": set the searching range according to ID. The default range is [0,10000], all CashCats will be searched.
- "alltraits": when it is 1, search CashCats that have complete six traits: Background, Body, Eyes, Mouth, Collar, and Accessory.
- "chk_xxx": when it is 1, search CashCats according to the setting given in "interested_xxx"; when it is 0, the corresponding "interested_xxx" will take no effect.
- "interested_xxx": specify target traits to 1 to search it. it only take effect when the corresponding "chk_xxx" is 1.



## Tips:
- Check rarity at https://oasis.cash/assets/cats/rarity.html.
- You can check any CashCat #ID at https://oasis.cash/token/0xE765026Cad648785b080E78700cBF6fa1C050d7C/#ID. for example, for CashCats #1234, check it at https://oasis.cash/token/0xE765026Cad648785b080E78700cBF6fa1C050d7C/1234
- In the default criteria.json, all traits that with Weight <= 50 is set to 1.



#### If you find it helpful, welcome to buy me a coffee as below:
SmartBCH: 0x1EECcD52a48100d64Be1B9eb28Ce22ad2a5f8685

