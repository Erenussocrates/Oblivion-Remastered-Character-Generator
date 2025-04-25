import random

class Race:
    def __init__(self):
        self.name=""
        self.origin = False

# Creating race instances
Argonian = Race()
Argonian.name="Argonian"

Breton = Race()
Breton.name="Breton"

Dark_Elf = Race()
Dark_Elf.name="Dark Elf"

High_Elf = Race()
High_Elf.name="High Elf"

Imperial = Race()
Imperial.name="Imperial"

Khajiit = Race()
Khajiit.name="Khajiit"

Nord = Race()
Nord.name="Nord"

Orc = Race()
Orc.name="Orc"

Redguard = Race()
Redguard.name="Redguard"

Wood_Elf = Race()
Wood_Elf.name="Wood Elf"

# Origin names mapped by race
race_origins = {
    "Argonian": ("Arnesia", "Thornmarsh"),
    "Breton": ("Systres", "High Rock"),
    "Dark Elf": ("Vvardenfell", "Mainland"),
    "High Elf": ("Auridon", "Summerset Isle"),
    "Imperial": ("Nibenay", "Colovia"),
    "Khajiit": ("Anequina", "Pellitine"),
    "Nord": ("Western", "Eastern"),
    "Orc": ("Stronghold", "Orsinium"),
    "Redguard": ("Dragontail Mountains", "Alik'r Desert"),
    "Wood Elf": ("Grahtwood", "Reaper's March")
}

all_races=[Argonian,Breton,Dark_Elf,High_Elf,Imperial,Khajiit,Nord,Orc,Redguard,Wood_Elf]

birth_signs = [
    "The Warrior", "The Mage", "The Thief", "The Steed",
    "The Apprentice", "The Shadow", "The Ritual", "The Atronach",
    "The Tower", "The Lord", "The Lady", "The Lover", "The Serpent"
]

# Determine valid birth signs based on class specialization and major skills
valid_birth_signs = birth_signs.copy()

specialization = ["Combat", "Magic", "Stealth"]

all_skills = [
    "Blade", "Blunt", "Hand to Hand", "Armorer", "Block", "Heavy Armor",
    "Athletics", "Acrobatics", "Light Armor", "Security", "Sneak", "Marksman",
    "Mercantile", "Speechcraft", "Illusion", "Alchemy", "Conjuration",
    "Mysticism", "Alteration", "Destruction", "Restoration"
]

magic_skills = ["Destruction", "Restoration", "Alteration", "Illusion", "Conjuration", "Mysticism"]

all_weapons = ["Hand to Hand","Claymores","Longswords","Shortswords","Daggers","Bows","Waraxes","Maces","Warhammers","Battleaxes","Spellcasting"]

blade_str_weapons=["Claymores","Longswords"]

blunt_str_weapons=["Waraxes","Maces","Warhammers","Battleaxes"]

blade_agi_weapons=["Shortswords","Daggers"]

two_handed_blade_weapons=["Claymores"]

two_handed_blunt_weapons=["Warhammers","Battleaxes"]

# Initialize the eligible_weapons list for the character
eligible_weapons = []

chosen_weapon = ""

allowed_weapons = []

allowed_spells = []

armors = ["Heavy Armor","Light Armor","Robes or Clothing"]

Horse = False
Staves = False
Potions = False
Repair = False
Snooping = False
Lockpick = False
Persuasion = False
Scroll = False
Haggle = False

questlines = [
    "Main Questline", "Arena", "Dark Brotherhood", "Fighters Guild",
    "Mages Guild", "Thieves Guild", "All Daedric Quests",
    "Knights of the Nine", "Shivering Isles"
]

download_quests = [
    "Battlehorn Castle", "Deepscorn Hollow", "Dunbarrow Cove",
    "Frostcrag Spire", "Repairing the Orrery", "Unearthing Mehrunes Razor"
]

# Start with all questlines and download quests combined
all_possible_quests = questlines + download_quests

class CharClass:
    def __init__(self):
        self.name = ""
        self.class_specialization = ""
        self.favored_attributes = []
        self.major_skills = []

#Combat Specialization

Warrior = CharClass()
Warrior.name = "Warrior"
Warrior.class_specialization = "Combat"
Warrior.favored_attributes = ["Strength", "Endurance"]
Warrior.major_skills = [
    "Armorer", "Athletics", "Blade", "Block",
    "Blunt", "Hand to Hand", "Heavy Armor"
]

Barbarian = CharClass()
Barbarian.name="Barbarian"
Barbarian.class_specialization = "Combat"
Barbarian.favored_attributes=["Strength", "Speed"]
Barbarian.major_skills=["Armorer", "Athletics", "Blade", "Block", "Blunt", "Hand to Hand", "Light Armor"]

Crusader = CharClass()
Crusader.name="Crusader"
Crusader.class_specialization="Combat"
Crusader.favored_attributes=["Strength", "Willpower"]
Crusader.major_skills=["Athletics","Blade","Blunt","Destruction","Hand to Hand","Heavy Armor","Restoration"]

Knight = CharClass()
Knight.name="Knight"
Knight.class_specialization="Combat"
Knight.favored_attributes=["Strength","Personality"]
Knight.major_skills=["Blade","Block","Blunt","Hand to Hand","Heavy Armor","Illusion","Speechcraft"]

Archer=CharClass()
Archer.name="Archer"
Archer.class_specialization="Combat"
Archer.favored_attributes=["Agility","Strength"]
Archer.major_skills=["Armorer","Blade","Blunt","Hand to Hand","Light Armor","Marksman","Sneak"]

Scout=CharClass()
Scout.name="Scout"
Scout.class_specialization="Combat"
Scout.favored_attributes=["Speed","Endurance"]
Scout.major_skills=["Acrobatics","Alchemy","Armorer","Athletics","Blade","Block","Light Armor"]

Rogue=CharClass()
Rogue.name="Rogue"
Rogue.class_specialization="Combat"
Rogue.favored_attributes=["Speed","Personality"]
Rogue.major_skills=["Alchemy","Athletics","Blade","Block","Illusion","Light Armor","Mercantile"]

#Magic Specialization

Mage=CharClass()
Mage.name="Mage"
Mage.class_specialization="Magic"
Mage.favored_attributes=["Intelligence","Willpower"]
Mage.major_skills=["Alchemy","Alteration","Conjuration","Destruction","Illusion","Mysticism","Restoration"]

Sorcerer=CharClass()
Sorcerer.name="Sorcerer"
Sorcerer.class_specialization="Magic"
Sorcerer.favored_attributes=["Intelligence","Endurance"]
Sorcerer.major_skills=["Alchemy","Alteration","Conjuration","Destruction","Heavy Armor","Mysticism","Restoration"]

Battlemage=CharClass()
Battlemage.name="Battlemage"
Battlemage.class_specialization="Magic"
Battlemage.favored_attributes=["Strength","Intelligence"]
Battlemage.major_skills=["Alchemy","Alteration","Blade","Blunt","Conjuration","Destruction","Mysticism"]

Healer=CharClass()
Healer.name="Healer"
Healer.class_specialization="Magic"
Healer.favored_attributes=["Personality","Willpower"]
Healer.major_skills=["Alchemy","Alteration","Destruction","Illusion","Mercantile","Restoration","Speechcraft"]

Spellsword=CharClass()
Spellsword.name="Spellsword"
Spellsword.class_specialization="Magic"
Spellsword.favored_attributes=["Willpower","Endurance"]
Spellsword.major_skills=["Alteration","Blade","Block","Destruction","Heavy Armor","Illusion","Restoration"]

Witchhunter=CharClass()
Witchhunter.name="Witchhunter"
Witchhunter.class_specialization="Magic"
Witchhunter.favored_attributes=["Intelligence","Agility"]
Witchhunter.major_skills=["Alchemy","Athletics","Conjuration","Destruction","Marksman","Mysticism","Security"]

Nightblade=CharClass()
Nightblade.name="Nightblade"
Nightblade.class_specialization="Magic"
Nightblade.favored_attributes=["Willpower","Speed"]
Nightblade.major_skills=["Acrobatics","Alteration","Athletics","Blade","Destruction","Light Armor","Restoration"]

#Stealth Specialization

Thief=CharClass()
Thief.name="Thief"
Thief.class_specialization="Stealth"
Thief.favored_attributes=["Speed","Agility"]
Thief.major_skills=["Acrobatics","Light Armor","Marksman","Mercantile","Security","Sneak","Speechcraft"]

Agent=CharClass()
Agent.name="Agent"
Agent.class_specialization="Stealth"
Agent.favored_attributes=["Personality","Agility"]
Agent.major_skills=["Acrobatics","Illusion","Marksman","Mercantile","Security","Sneak","Speechcraft"]

Acrobat=CharClass()
Acrobat.name="Acrobat"
Acrobat.class_specialization="Stealth"
Acrobat.favored_attributes=["Agility","Endurance"]
Acrobat.major_skills=["Acrobatics","Blade","Block","Marksman","Security","Sneak","Speechcraft"]

Assassin=CharClass()
Assassin.name="Assassin"
Assassin.class_specialization="Stealth"
Assassin.favored_attributes=["Speed","Intelligence"]
Assassin.major_skills=["Acrobatics","Alchemy","Blade","Light Armor","Marksman","Security","Sneak"]

Monk=CharClass()
Monk.name="Monk"
Monk.class_specialization="Stealth"
Monk.favored_attributes=["Agility","Willpower"]
Monk.major_skills=["Acrobatics","Alteration","Athletics","Hand to Hand","Marksman","Security","Sneak"]

Pilgrim=CharClass()
Pilgrim.name="Pilgrim"
Pilgrim.class_specialization="Stealth"
Pilgrim.favored_attributes=["Personality","Endurance"]
Pilgrim.major_skills=["Armorer","Block","Blunt","Light Armor","Mercantile","Security","Speechcraft"]

Bard=CharClass()
Bard.name="Bard"
Bard.class_specialization="Stealth"
Bard.favored_attributes=["Personality","Intelligence"]
Bard.major_skills=["Alchemy","Blade","Block","Illusion","Light Armor","Mercantile","Speechcraft"]

# Custom classes

Mercenary=CharClass()
Mercenary.name="Mercenary (Custom Class!)"
Mercenary.class_specialization="Combat"
Mercenary.favored_attributes=["Strength","Endurance"]
Mercenary.major_skills=["Armorer","Mercantile","Block","blade-or-blunt","heavy-or-light-armor","Alchemy","Speechcraft"]

Paladin=CharClass()
Paladin.name="Paladin (Custom Class!)"
Paladin.class_specialization="Combat"
Paladin.favored_attributes=["Strength","Willpower"]
Paladin.major_skills=["Athletics","blade-or-blunt","Destruction","heavy-or-light-armor","Restoration","Alteration","Speechcraft"]

Infiltrator=CharClass()
Infiltrator.name="Infiltrator (Custom Class!)"
Infiltrator.class_specialization="Combat"
Infiltrator.favored_attributes=["Strength","Personality"]
Infiltrator.major_skills=["blade-or-blunt","Block","heavy-or-light-armor","Illusion","Speechcraft","Sneak","Conjuration"]

Hunter=CharClass()
Hunter.name="Hunter (Custom Class!)"
Hunter.class_specialization="Combat"
Hunter.favored_attributes=["Agility","Speed"]
Hunter.major_skills=["Armorer","heavy-or-light-armor","Marksman","Sneak","Athletics","Alchemy","Mysticism"]

Shaman=CharClass()
Shaman.name="Shaman (Custom Class!)"
Shaman.class_specialization="Magic"
Shaman.favored_attributes=["Strength","Intelligence"]
Shaman.major_skills=["Alchemy","Alteration","blade-or-blunt","Conjuration","Destruction","Mysticism","Restoration"]

Warlock=CharClass()
Warlock.name="Warlock (Custom Class!)"
Warlock.class_specialization="Magic"
Warlock.favored_attributes=["Intelligence","Endurance"]
Warlock.major_skills=["Alchemy","Alteration","Conjuration","Destruction","heavy-or-light-armor","Mysticism","Illusion"]

Summoner=CharClass()
Summoner.name="Summoner (Custom Class!)"
Summoner.class_specialization="Stealth"
Summoner.favored_attributes=["Agility","Intelligence"]
Summoner.major_skills=["Marksman","Conjuration","Sneak","Alchemy","heavy-or-light-armor","Restoration","Security"]


normal_classes=[Warrior,Barbarian,Crusader,Knight,Archer,Scout,Rogue,Mage,Sorcerer,Battlemage,Healer,Spellsword,Witchhunter,Nightblade,Thief,Agent,Acrobat,Assassin,Monk,Pilgrim,Bard]

custom_classes=[Mercenary,Paladin,Infiltrator,Hunter,Shaman,Warlock,Summoner]

# Randomly select a race
random_race = random.choice(all_races)

# Generate a random integer between 0 and 21 (inclusive)
class_roll = random.randint(0, 21)

# Determine if the class is from normal or custom classes
if class_roll <= 20:
    random_class = random.choice(normal_classes)
else:
    random_class = random.choice(custom_classes)

# Determine the origin logic
if random_race.name in ["Orc", "Argonian"]:
    # If any magic skill is present, origin can be True or False
    if any(skill in random_class.major_skills for skill in magic_skills):
        random_race.origin = random.choice([True, False])
    else:
        random_race.origin = False
else:
    random_race.origin = random.choice([True, False])

# Get origin string
origin_str = race_origins[random_race.name][1 if random_race.origin else 0]

# If none of the major skills are magic, remove magic-specific birth signs
if not any(skill in magic_skills for skill in random_class.major_skills):
    for sign in ["The Mage", "The Apprentice", "The Atronach"]:
        if sign in valid_birth_signs:
            valid_birth_signs.remove(sign)
            
# Remove "The Shadow" if "Sneak" is not a major skill
if "Sneak" not in random_class.major_skills:
    if "The Shadow" in valid_birth_signs:
        valid_birth_signs.remove("The Shadow")
            
# Filter based on class specialization
if random_class.class_specialization != "Combat":
    if "The Warrior" in valid_birth_signs:
        valid_birth_signs.remove("The Warrior")

if random_class.class_specialization != "Magic":
    if "The Mage" in valid_birth_signs:
        valid_birth_signs.remove("The Mage")

if random_class.class_specialization != "Stealth":
    if "The Thief" in valid_birth_signs:
        valid_birth_signs.remove("The Thief")

# Randomly select a birth sign from the filtered list
random_birth_sign = random.choice(valid_birth_signs)

# Handle 'heavy-or-light-armor' replacement
if "heavy-or-light-armor" in random_class.major_skills:
    chosen_armor_skill = random.choice(["Heavy Armor", "Light Armor"])
    # Replace placeholder with actual skill
    random_class.major_skills = [
        chosen_armor_skill if skill == "heavy-or-light-armor" else skill
        for skill in random_class.major_skills
    ]
else:
    # If not present, set default to None
    chosen_armor_skill = None

# Handle 'blade-or-blunt' replacement
if "blade-or-blunt" in random_class.major_skills:
    chosen_weapon_skill = random.choice(["Blade", "Blunt"])
    random_class.major_skills = [
        chosen_weapon_skill if skill == "blade-or-blunt" else skill
        for skill in random_class.major_skills
    ]
else:
    chosen_weapon_skill = None

magic_skill_count = sum(skill in random_class.major_skills for skill in magic_skills)

# Filtering logic

# "Dark Brotherhood" requires "Sneak"
if "Sneak" not in random_class.major_skills and "Dark Brotherhood" in all_possible_quests:
    all_possible_quests.remove("Dark Brotherhood")

# "Thieves Guild" requires BOTH "Sneak" and "Security"
if not ("Sneak" in random_class.major_skills and "Security" in random_class.major_skills):
    if "Thieves Guild" in all_possible_quests:
        all_possible_quests.remove("Thieves Guild")

# "Fighters Guild" requires Combat specialization
if random_class.class_specialization != "Combat" and (
        ("Blade" not in random_class.major_skills and "Blunt" not in random_class.major_skills) or
        ("Heavy Armor" not in random_class.major_skills and "Light Armor" not in random_class.major_skills) or
        ("Sneak" in random_class.major_skills)
    ) and random_class.name != "Summoner (Custom Class!)":
    if "Fighters Guild" in all_possible_quests:
        all_possible_quests.remove("Fighters Guild")
    if "Battlehorn Castle" in all_possible_quests:
        all_possible_quests.remove("Battlehorn Castle")

# "Mages Guild" requires Magic specialization
if random_class.class_specialization != "Magic" and magic_skill_count < 3 and random_class.name != "Summoner (Custom Class!)":
    if "Mages Guild" in all_possible_quests:
        all_possible_quests.remove("Mages Guild")
    for quest in ["Frostcrag Spire", "Repairing the Orrery"]:
        if quest in all_possible_quests:
            all_possible_quests.remove(quest)
            
# Remove "Arena" if neither Heavy Armor nor Light Armor is a major skill
if "Heavy Armor" not in random_class.major_skills and "Light Armor" not in random_class.major_skills:
    if "Arena" in all_possible_quests:
        all_possible_quests.remove("Arena")

# Stealth specialization required for Deepscorn and Dunbarrow
if random_class.class_specialization != "Stealth":
    for quest in ["Deepscorn Hollow", "Dunbarrow Cove"]:
        if quest in all_possible_quests:
            all_possible_quests.remove(quest)

# Determine eligible armor type
if "Heavy Armor" in random_class.major_skills:
    selected_armor = "Heavy Armor"
elif "Light Armor" in random_class.major_skills:
    selected_armor = "Light Armor"
else:
    selected_armor = "Robes or Clothing"

# If "Hand to Hand" is in the major skills, add "Hand to Hand" to eligible_weapons
if "Hand to Hand" in random_class.major_skills:
    eligible_weapons.append("Hand to Hand")

if "Blade" in random_class.major_skills and "Block" in random_class.major_skills:
    eligible_weapons.extend(
        [w for w in blade_str_weapons if w not in two_handed_blade_weapons]
    )

if "Blunt" in random_class.major_skills and "Block" in random_class.major_skills:
    eligible_weapons.extend(
        [w for w in blunt_str_weapons if w not in two_handed_blunt_weapons]
    )

if ("Blade" in random_class.major_skills and "Block" not in random_class.major_skills) or (("Blade" in random_class.major_skills and "Block" in random_class.major_skills) and ("Heavy Armor" not in random_class.major_skills and "Light Armor" not in random_class.major_skills)):
        eligible_weapons.extend(two_handed_blade_weapons)

if ("Blunt" in random_class.major_skills and "Block" not in random_class.major_skills) or (("Blunt" in random_class.major_skills and "Block" in random_class.major_skills) and ("Heavy Armor" not in random_class.major_skills and "Light Armor" not in random_class.major_skills)):
        eligible_weapons.extend(two_handed_blunt_weapons)

if (("Agility" in random_class.favored_attributes) or ("Strength" not in random_class.favored_attributes)) and ("Blade" in random_class.major_skills):
        eligible_weapons.extend(blade_agi_weapons)

# After populating eligible_weapons, pick a random weapon from it
if eligible_weapons:
    chosen_weapon = random.choice(eligible_weapons)
    
    # Check for Shield logic
    has_shield_skills = (
        ("Blade" in random_class.major_skills or "Blunt" in random_class.major_skills)
        and "Block" in random_class.major_skills
        and ("Heavy Armor" in random_class.major_skills or "Light Armor" in random_class.major_skills)
        and (chosen_weapon != "Hand to Hand")
    )
    
    is_one_handed = chosen_weapon not in two_handed_blade_weapons and chosen_weapon not in two_handed_blunt_weapons

    if has_shield_skills and is_one_handed:
        chosen_weapon += " and Shields"
    
    allowed_weapons.append(chosen_weapon)

# Check whether raw weapon is "Daggers" before modifying it
is_daggers = chosen_weapon == "Daggers"

# If not using Daggers, remove quest
if not is_daggers and "Unearthing Mehrunes Razor" in all_possible_quests:
    all_possible_quests.remove("Unearthing Mehrunes Razor")
    
# If "Marksman" is in the major skills, add "Bows" to Allowed Weapons
if "Marksman" in random_class.major_skills:
    allowed_weapons.append("Bows")
    
# Find all magic skills present in the class
magic_skills_in_class = [skill for skill in random_class.major_skills if skill in magic_skills]

if magic_skills_in_class:
    allowed_weapons.append("Spellcasting")
    allowed_spells.extend(magic_skills_in_class)
    
# Randomly select 3 questlines from the filtered list
selected_quests = random.sample(all_possible_quests, 3)

if "Sneak" in random_class.major_skills:
    Snooping = True
    
if "Security" in random_class.major_skills:
    Lockpick = True
    
if "Armorer" in random_class.major_skills:
    Repair = True
    
if "Alchemy" in random_class.major_skills:
    Potions = True
    
if "Speechcraft" in random_class.major_skills:
    Persuasion = True

if "Mercantile" in random_class.major_skills:
    Haggle = True

# === HORSE LOGIC ===
if "Athletics" in random_class.major_skills:
    Horse = False
elif random_class.name == "Knight":
    Horse = True
else:
    Horse = random.choice([True, False])

# === STAVES LOGIC ===
has_magic_skills = any(skill in magic_skills for skill in random_class.major_skills)
in_mages_guild = "Mages Guild" in selected_quests

if in_mages_guild:
    Staves = True
elif has_magic_skills:
    Staves = random.choice([True, False])
    Scroll = random.choice([True, False])
else:
    Staves = False
    Scroll = False
    
# === LUCKY DRAW ===
Lucky_Draw = random.random() < 0.01
    
# Collect output in a list
output_lines = []

output_lines.append("====YOUR GENERATED CHARACTER====\n")
output_lines.append(f"RACE = {random_race.name}")
output_lines.append(f"ORIGIN = {origin_str}")
output_lines.append(f"BIRTHSIGN = {random_birth_sign}")
output_lines.append(f"CLASS = {random_class.name}")
output_lines.append(f"\nAllowed Weapons: {', '.join(allowed_weapons)}")
if allowed_spells:
    output_lines.append(f"Allowed Schools of Magic: {', '.join(allowed_spells)}")
else:
    output_lines.append("Allowed Schools of Magic: None")
output_lines.append(f"Allowed Armor Type: {selected_armor}")

if random_class in custom_classes:
    output_lines.append("\n====CUSTOM CLASS DETAILS========")
    output_lines.append(f"SPECIALIZATION = {random_class.class_specialization}")
    output_lines.append(f"FAVORED ATTRIBUTES = {', '.join(random_class.favored_attributes)}")
    output_lines.append(f"MAJOR SKILLS = {', '.join(random_class.major_skills)}")

output_lines.append("")  # Empty line

output_lines.append("\n====MANDATORY QUESTLINES========")
for quest in selected_quests:
    output_lines.append(f"- {quest}")
    
if Lucky_Draw:
    output_lines.append("\n====LUCKY DRAW!=================")
    output_lines.append("You are allowed to Load once if you die!")

output_lines.append("================================")

if Snooping:
    output_lines.append("\nYour character IS allowed to sneak!")
else:
    output_lines.append("\nYour character is NOT allowed to sneak!")
    
if Lockpick:
    output_lines.append("Your character IS allowed to use Lockpicks!")
else:
    output_lines.append("Your character is NOT allowed to use Lockpicks! But you can still use auto-attempt.")
    
if Repair:
    output_lines.append("Your character IS allowed to use Repair Hammers!")
else:
    output_lines.append("Your character is NOT allowed to use Repair Hammers!")

if Potions:
    output_lines.append("Your character IS allowed to use Mortar and Pestle!")
else:
    output_lines.append("Your character is NOT allowed to use Mortar and Pestle!")

if Persuasion:
    output_lines.append("Your character IS allowed to use the Persuasion minigame!")
else:
    output_lines.append("Your character is NOT allowed to use the Persuasion minigame! But you can still bribe people.")

if Haggle:
    output_lines.append("Your character IS allowed to haggle!")
else:
    output_lines.append("Your character is NOT allowed to haggle!")

if Horse:
    output_lines.append("Your character IS allowed to ride a horse!")
else:
    output_lines.append("Your character is NOT allowed to ride a horse!")

if Staves:
    output_lines.append("Your character IS allowed to use staves!")
else:
    output_lines.append("Your character is NOT allowed to use staves!")
    
if Scroll:
    output_lines.append("Your character IS allowed to use scrolls!")
else:
    output_lines.append("Your character is NOT allowed to use scrolls!")

# Join everything and print
full_output = "\n".join(output_lines)
print(full_output)

# Write to file (overwrite each run)
with open("Char Gen Output.txt", "w", encoding="utf-8") as f:
    f.write(full_output)
