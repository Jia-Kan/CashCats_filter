# CashCats_filter
This is a simple script to search CashCatsNFT with their traits.

## USAGE:

1. Edit [criteria.json](./criteria.json) to specify searching criteria;
2. run "python search_cats.py" in command line, python3 is needed;
3. ID of all CashCats that meet the searching criteria will be printed.



## About settings in criteria.json:

- "search_range": set the searching range according to ID. The default range is \[0,10000\], all CashCats will be searched.
- "alltraits": when it is 1, search CashCats that have complete six traits: Background, Body, Eyes, Mouth, Collar, and Accessory.
- "chk_xxx": when it is 1, search CashCats according to the setting given in "interested_xxx"; when it is 0, the corresponding "interested_xxx" will take no effect.
- "interested_xxx": specify target traits to 1 to search it. it only take effect when the corresponding "chk_xxx" is 1.



## Tips:
- Check rarity at https://oasis.cash/assets/cats/rarity.html.
- You can check any CashCat #ID at https://oasis.cash/token/0xE765026Cad648785b080E78700cBF6fa1C050d7C/#ID. for example, for CashCats #1234, check it at https://oasis.cash/token/0xE765026Cad648785b080E78700cBF6fa1C050d7C/1234
- In the default criteria.json, all traits that with Weight <= 50 is set to 1.



##### If you find it helpful, welcome to buy me a coffee as below:
SmartBCH: 0x1EECcD52a48100d64Be1B9eb28Ce22ad2a5f8685


# CashCats_filter
这是一个用来搜索CashCats NFT的python3脚本。

## 使用方法：

1. 编辑 [criteria.json](./criteria.json)，指定搜索条件;
2. 在命令行运行 "python search_cats.py", 需要安装python3环境;
3. 搜索到的猫头像ID号码会显示出来。



## 关于criteria.json的说明：

- "search_range": 依据ID设置搜索范围。默认的范围是\[0,10000\]，搜索所有CashCats。
- "alltraits": 设置为1，搜索六属性齐全的CashCats: Background背景，Body脸，Eyes眼睛，Mouth嘴，Collar衣领，Accessory配饰。
- "chk_xxx": 设置为1，打开搜索xxx属性的开关。设置为0，对应的“interested_xxx”就不起作用。
- "interested_xxx": 设置为1，指定xxx属性下单个或多个搜索目标。仅在对应的“chk_xxx”为1时起作用。



## 提示：
- 此链接可以查看CashCats稀缺性：https://oasis.cash/assets/cats/rarity.html.
- 通过链接 https://oasis.cash/token/0xE765026Cad648785b080E78700cBF6fa1C050d7C/#ID 可查看任意ID的CashCats. 例如，CashCats #1234 可通过以下链接查看：https://oasis.cash/token/0xE765026Cad648785b080E78700cBF6fa1C050d7C/1234
- 默认的criteria.json文件中, 所有Weight权重小于等于50的特征都已设置为1.



##### 如果你觉得这个脚本有帮助，欢迎打赏：
SmartBCH: 0x1EECcD52a48100d64Be1B9eb28Ce22ad2a5f8685


