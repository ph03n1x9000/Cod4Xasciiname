# Cod4Xasciiname
B3 plugin that works with CoD4X to change player name if it is Unicode (or unrecognizable by B3).

This plugin was designed to address the problem of player with Unicode names being unable to be banned/tempbanned due to empty name.

Installation:
1) Put the file named "cod4xasciiname.py" into your b3\extplugins folder.
2) In the b3.ini under the [plugins] section, enter the following:
  > cod4xasciiname: none

3) Put the contents of the main_shared folder into your CoD4X root\main_shared
4) Add the follwing line into the "_callbacksetup.gsx"_ file 
