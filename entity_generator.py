def get_filename():
	filename = raw_input("Enter file name without .txt (default is entity_default): ")
	return filename.strip()

def get_entityname():
	entityname = raw_input("Enter entity name (dwarf is MOUNTAIN): ").strip().upper()
	entitynametag = "[ENTITY:%1]".replace("%1", entityname)
	return entitynametag.strip()
	
def get_species():
	input = "something"
	species = []
	while input:
		input = raw_input("Enter a species for this entity, and nothing to finish (need at least one): ").strip().upper()
		if input:
			speciestag = "[CREATURE:%1]".replace("%1", input)
			species.append(speciestag)
			
	outputstring = ""
	for value in species:
		outputstring += value + "\n"
	
	return outputstring.strip()

def get_symbols():
	input = "something"
	symbols = []
	print("List of symbol groups: ARTIFICE, ASSERTIVE, AQUATIC, COLOR, DEATH, DOMESTIC, EARTH, EVIL, FLOWERY, GOOD, HOLY, LEADER, MAGIC, MYSTERY, MYTHIC, NATURE, NEGATIVE, NEGATOR, NEW, OLD, PEACE, PRIMITIVE, PROTECT, RESTRAIN, ROMANTIC, SUBORDINATE, THOUGHT, UGLY, UNTOWARD, VIOLENT, WILD")
	while input:
		input = raw_input("Enter a symbol group to be used by this species when choosing names for people and places, and enter nothing to finish: ").strip().upper()
		if input:
			symboltag = "[SELECT_SYMBOL:REMAINING:%1]".replace("%1", input)
			symbols.append(symboltag)
			
	outputstring = ""
	for value in symbols:
		outputstring += value + "\n"
	
	return outputstring.strip()

def get_color():
	print "Color is defined with three values: foreground (0-7), background (0-7) and brightness of foreground(0-1)"
	x = raw_input("Enter foreground color (0-7): ").strip()
	y = raw_input("Enter background color (0-7): ").strip()
	z = raw_input("Enter foreground brightness (0-1): ").strip()
	
	tag = "[FRIENDLY_COLOR:%1:%2:%3]".replace("%1", x).replace("%2", y).replace("%3", z)

def get_biomes():
	input = "something"
	biomes = []
	print("List of biomes here: http://dwarffortresswiki.org/index.php/DF2014:Biome_token")
	while input:
		input = raw_input("Enter a starting biome for this species, and enter nothing to finish (need at least one): ").strip().upper()
		if input:
			biometag = "[START_BIOME:%1]".replace("%1", input)
			biomes.append(biometag)
			
	input = "somethingelse"
	while input:
		input = raw_input("Enter a biome to define how likely this species will settle there: ").strip().upper()
		if input:
			input2 = raw_input("Enter the number for this biome: ").strip()
			biometag = "[BIOME_SUPPORT:%1:%2]".replace("%1", input).replace("%2", input2)
			biomes.append(biometag)
			
	outputstring = ""
	for value in biomes:
		outputstring += value + "\n"
	
	return outputstring.strip()
	
def get_treecap():
	print "Should this civilization impose tree cutting quotas? (like elves): "
	input = raw_input("Enter something for yes, nothing for no: ").strip()
	if input:
		return "[TREE_CAP_DIPLOMACY]"
	return "@"
	
def get_progress():
	progress_tags = []
	print "This civilization will trade with the player when their fortress' population reach this level"
	print "0: population trigger disabled"
	print "1: 20 people"
	print "2: 50 people"
	print "3: 80 people"
	print "4: 110 people"
	print "5: 140 people"
	level = raw_input("Enter number from 0 to 5: ").strip()
	trigger_tag = "[PROGRESS_TRIGGER_POPULATION:%1]".replace("%1", level)
	progress_tags.append(trigger_tag)
	
	print "This civilization will trade with the player when their fortress' production reach this level"
	print "0: production trigger disabled"
	print "1: 5000 created wealth"
	print "2: 25000 created wealth"
	print "3: 100000 created wealth"
	print "4: 200000 created wealth"
	print "5: 300000 created wealth"
	level = raw_input("Enter number from 0 to 5: ").strip()
	trigger_tag = "[PROGRESS_TRIGGER_PRODUCTION:%1]".replace("%1", level)
	progress_tags.append(trigger_tag)
	
	print "This civilization will trade with the player when their fortress' exported goods reach this level"
	print "0: trade trigger disabled"
	print "1: 500 exported wealth"
	print "2: 2500 exported wealth"
	print "3: 10000 exported wealth"
	print "4: 20000 exported wealth"
	print "5: 30000 exported wealth"
	level = raw_input("Enter number from 0 to 5: ").strip()
	trigger_tag = "[PROGRESS_TRIGGER_TRADE:%1]".replace("%1", level)
	progress_tags.append(trigger_tag)
	
	print "If hostile, this civilization will begin to send sieges to the player when their fortress' population reaches this level."
	level = raw_input("Enter number from 0 to 5: ").strip()
	trigger_tag = "[PROGRESS_TRIGGER_POP_SIEGE:%1]".replace("%1", level)
	progress_tags.append(trigger_tag)
	
	print "If hostile, this civilization will begin to send sieges to the player when their fortress' production reaches this level."
	level = raw_input("Enter number from 0 to 5: ").strip()
	trigger_tag = "[PROGRESS_TRIGGER_PROD_SIEGE:%1]".replace("%1", level)
	progress_tags.append(trigger_tag)
	
	print "If hostile, this civilization will begin to send sieges to the player when their fortress' exported wealth reaches this level."
	level = raw_input("Enter number from 0 to 5: ").strip()
	trigger_tag = "[PROGRESS_TRIGGER_TRADE_SIEGE:%1]".replace("%1", level)
	progress_tags.append(trigger_tag)
	
	outputstring = ""
	for value in progress_tags:
		outputstring += value + "\n"
	
	return outputstring.strip()
	
def get_season():
	print "Active season for trading: SPRING, SUMMER, AUTUMN or WINTER"
	season = raw_input("Enter season: ").strip().upper()
	seasontag = "[ACTIVE_SEASON:%1]".replace("%1", season)
	return seasontag
	
def get_babysnatcher():
	print "Should this civilization steal babies? If so, they will be hostile to every civilization without this tag: "
	input = raw_input("Enter something for yes, nothing for no: ").strip()
	if input:
		return "[BABYSNATCHER]"
	return "@"
	
def get_ambusher():
	print "Should this civilization ambush?"
	input = raw_input("Enter something for yes, nothing for no: ").strip()
	if input:
		return "[AMBUSHER]"
	return "@"

def get_itemthief():
	print "Should this civilization steal items? If so, they will be hostile to every civilization without this tag"
	input = raw_input("Enter something for yes, nothing for no: ").strip()
	if input:
		return "[ITEM_THIEF]\n[SKULKING]"
	return "@"
	
def get_religion():
	print "For a list of religion spheres, see http://dwarffortresswiki.org/index.php/DF2014:Sphere"
	
	input = "something"
	spheres = []
	while input:
		input = raw_input("Enter a religious sphere for this entity, and nothing to finish (need at least one): ").strip().upper()
		if input:
			tag = "[RELIGION_SPHERE:%1]".replace("%1", input)
			spheres.append(tag)
			
	outputstring = ""
	for value in spheres:
		outputstring += value + "\n"
	
	return outputstring.strip()
	
def get_ethics():
	ethics = ["ASSAULT", "EAT_SAPIENT_KILL", "EAT_SAPIENT_OTHER", "KILL_ANIMAL", "KILL_ENEMY", "KILL_ENTITY_MEMBER", "KILL_NEUTRAL", "KILL_PLANT", "LYING", "MAKE_TROPHY_ANIMAL", "MAKE_TROPHY_SAME_RACE", "MAKE_TROPHY_SAPIENT", "OATH_BREAKING", "SLAVERY", "THEFT", "TORTURE_ANIMALS", "TORTURE_AS_EXAMPLE", "TORTURE_FOR_FUN", "TORTURE_FOR_INFORMATION", "TREASON", "TRESPASSING", "VANDALISM"]
	ethic_values = ["NOT_APPLICABLE", "ACCEPTABLE", "PERSONAL_MATTER", "JUSTIFIED_IF_NO_REPERCUSSIONS", "JUSTIFIED_IF_GOOD_REASON", "JUSTIFIED_IF_EXTREME_REASON", "JUSTIFIED_IF_SELF_DEFENSE", "ONLY_IF_SANCTIONED", "MISGUIDED", "SHUN", "APPALLING", "PUNISH_REPRIMAND", "PUNISH_SERIOUS", "PUNISH_EXILE", "PUNISH_CAPITAL", "UNTHINKABLE", "REQUIRED"]
	
	print "For this part, see http://dwarffortresswiki.org/index.php/DF2014:Ethic"
	values = []
	
	for ethic in ethics:
		value = int(raw_input("Enter value for ethic " + ethic + ": ").strip())
		values.append(value)
		
	outputstring = ""
	for value in values:
		ethic = ethics[value]
		ethic_value = ethic_values[value]
		tag = "[ETHIC:%1:%2]".replace("%1", ethic).replace("%2", ethic_value).strip()
		outputstring += tag + "\n"
	
	return outputstring.strip()
	
def get_values():
	values = ["LAW", "LOYALTY", "FAMILY", "FRIENDSHIP", "POWER", "TRUTH", "CUNNING", "ELOQUENCE", "FAIRNESS", "DECORUM", "TRADITION", "ARTWORK", "COOPERATION", "INDEPENDENCE", "STOICISM", "KNOWLEDGE", "INTROSPECTION", "SELF_CONTROL", "TRANQUILITY", "HARMONY", "MERRIMENT", "CRAFTSMANSHIP", "MARTIAL_PROWESS", "SKILL", "HARD_WORK", "SACRIFICE", "COMPETITION", "PERSEVERANCE", "LEISURE_TIME", "COMMERCE", "ROMANCE", "NATURE", "PEACE"]
	
	print "Values go from -50 to 50, for each value, enter the minimum and maximum random value for this civ"
	outputstring = ""
	
	for value in values:
		min = raw_input("Enter minimum for value " + value + ": ").strip()
		max = raw_input("Enter maximum for value " + value + ": ").strip()
		print ""

		tag = "[VARIABLE_VALUE:%1:%2:%3]".replace("%1", value).replace("%2", min).replace("%3", max)
		outputstring += tag + "\n"
	
	return outputstring.strip()
	
def get_banditry():
	print "Percentage of population that are bandits (humans and elves have 10)"
	banditry = raw_input("Enter number from 0 to 100: ").strip()
	banditerytag = "[BANDITRY:%1]".replace("%1", banditry)
	return banditerytag

	
	
def handletoken(token):
	output = ""
	
	if "filename" in token:
		output = get_filename()
	if "entityname" in token:
		output = get_entityname()
	if "species" in token:
		output = get_species()
	if "symbols" in token:
		output = get_symbols()
	if "color" in token:
		output = get_color()
	if "biomes" in token:
		output = get_biomes()
	if "treecap" in token:
		output = get_treecap()
	if "progress" in token:
		output = get_progress()
	if "season" in token:
		output = get_season()
	if "babysnatcher" in token:
		output = get_babysnatcher()
	if "ambusher" in token:
		output = get_ambusher()
	if "item_thief" in token:
		output = get_itemthief()
	if "religion" in token:
		output = get_religion()
	if "ethics" in token:
		output = get_ethics()
	if "values" in token:
		output = get_values()
	if "banditry" in token:
		output = get_banditry()
		
	return output

def readline(line):
	if "{" in line:
		return handletoken(line.strip())

def main():
	entity_template_file = open("entity_template.txt", "r");
	output_string = ""
	newfilename = ""
	
	for line in entity_template_file:
		tag = readline(line)
		if (tag):
			if "@" in tag:
				continue
				
			if not newfilename:
				newfilename = tag + ".txt"
				
			newline = ""
			
			nbTabs = line.count("\t")
			tabs = ""
			for x in range (0, nbTabs):
				tabs += "\t"
			tabsnewline = "\n" + tabs
			tag = tabsnewline.join(tag.split("\n"))
			newline += tabs + tag + "\n"
			output_string += newline
			print newline
		else:
			output_string += line

	entity_template_file.close()
	
	newfile = open(newfilename, "w")
	newfile.write(output_string)
	newfile.close()

	print "Exported to " + newfilename
	raw_input()
	
main()