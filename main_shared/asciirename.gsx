init() {
	setDvar("b3_asciirename", "");
	while(1) {
		if(getDvar("b3_asciirename") != "") thread asciirenamer();
		wait 0.5;
	}
}

asciirenamer() {
	player = getentbynum(getDvarInt("b3_asciirename"));
	setDvar("b3_asciirename", "");
	if(isDefined(player)) {
		playeruid = player getEntityNumber();
		oldname = player.name;
		player.name = "CID" + inttostr(playeruid);
		iprintLn(oldname  + " was renamed to " + player.name);
	}
}

inttostr(integer) {
	setDvar("inttostr", integer);
	return getDvar("inttostr");
}
