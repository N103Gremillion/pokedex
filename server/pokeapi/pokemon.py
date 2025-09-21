import time
from typing import List, Optional
from flask import json
from app_types import DetailedPokemonTypeKeys, ErrorResponse, LearnMethod, MoveData, MoveKeys, PokedexKeys, PokemonData, PokemonEvolution, PokemonEvolutionKeys, PokemonType, SuccessResponse, ErrorResponseKeys, PokemonKeys, SuccessResponseKeys
from mongo.db_utils import DatabaseCollections, clean_for_mongo
from utils import hectogramsToPounds, isValidType, print_pretty_json
from pokeapi.general import baseApiUrl, fetchData
from enum import Enum
import requests
from pymongo.collection import Collection
from bson import json_util

POKEMON_NAMES : List[str] = [
  "bulbasaur", "ivysaur", "venusaur", "charmander", "charmeleon", "charizard",
  "squirtle", "wartortle", "blastoise", "caterpie", "metapod", "butterfree",
  "weedle", "kakuna", "beedrill", "pidgey", "pidgeotto", "pidgeot", "rattata",
  "raticate", "spearow", "fearow", "ekans", "arbok", "pikachu", "raichu",
  "sandshrew", "sandslash", "nidoran-f", "nidorina", "nidoqueen", "nidoran-m",
  "nidorino", "nidoking", "clefairy", "clefable", "vulpix", "ninetales",
  "jigglypuff", "wigglytuff", "zubat", "golbat", "oddish", "gloom", "vileplume",
  "paras", "parasect", "venonat", "venomoth", "diglett", "dugtrio", "meowth",
  "persian", "psyduck", "golduck", "mankey", "primeape", "growlithe", "arcanine",
  "poliwag", "poliwhirl", "poliwrath", "abra", "kadabra", "alakazam", "machop",
  "machoke", "machamp", "bellsprout", "weepinbell", "victreebel", "tentacool",
  "tentacruel", "geodude", "graveler", "golem", "ponyta", "rapidash", "slowpoke",
  "slowbro", "magnemite", "magneton", "farfetchd", "doduo", "dodrio", "seel",
  "dewgong", "grimer", "muk", "shellder", "cloyster", "gastly", "haunter",
  "gengar", "onix", "drowzee", "hypno", "krabby", "kingler", "voltorb", "electrode",
  "exeggcute", "exeggutor", "cubone", "marowak", "hitmonlee", "hitmonchan",
  "lickitung", "koffing", "weezing", "rhyhorn", "rhydon", "chansey", "tangela",
  "kangaskhan", "horsea", "seadra", "goldeen", "seaking", "staryu", "starmie",
  "mr-mime", "scyther", "jynx", "electabuzz", "magmar", "pinsir", "tauros",
  "magikarp", "gyarados", "lapras", "ditto", "eevee", "vaporeon", "jolteon",
  "flareon", "porygon", "omanyte", "omastar", "kabuto", "kabutops", "aerodactyl",
  "snorlax", "articuno", "zapdos", "moltres", "dratini", "dragonair", "dragonite",
  "mewtwo", "mew", "chikorita", "bayleef", "meganium", "cyndaquil", "quilava",
  "typhlosion", "totodile", "croconaw", "feraligatr", "sentret", "furret",
  "hoothoot", "noctowl", "ledyba", "ledian", "spinarak", "ariados", "crobat",
  "chinchou", "lanturn", "pichu", "cleffa", "igglybuff", "togepi", "togetic",
  "natu", "xatu", "mareep", "flaaffy", "ampharos", "bellossom", "marill",
  "azumarill", "sudowoodo", "politoed", "hoppip", "skiploom", "jumpluff",
  "aipom", "sunkern", "sunflora", "yanma", "wooper", "quagsire", "espeon",
  "umbreon", "murkrow", "slowking", "misdreavus", "unown", "wobbuffet", "girafarig",
  "pineco", "forretress", "dunsparce", "gligar", "steelix", "snubbull", "granbull",
  "qwilfish", "scizor", "shuckle", "heracross", "sneasel", "teddiursa", "ursaring",
  "slugma", "magcargo", "swinub", "piloswine", "corsola", "remoraid", "octillery",
  "delibird", "mantine", "skarmory", "houndour", "houndoom", "kingdra", "phanpy",
  "donphan", "porygon2", "stantler", "smeargle", "tyrogue", "hitmontop", "smoochum",
  "elekid", "magby", "miltank", "blissey", "raikou", "entei", "suicune", "larvitar",
  "pupitar", "tyranitar", "lugia", "ho-oh", "celebi", "sableye", "mawile", "aron", "lairon", "aggron", 
  "meditite", "medicham", "electrike", "manectric", "plusle", "minun", "volbeat", "illumise", "roselia", 
  "gulpin", "swalot", "carvanha", "sharpedo", "wailmer", "wailord", "numel", "camerupt", "torkoal", "spoink", 
  "grumpig", "spinda", "trapinch", "vibrava", "flygon", "cacnea", "cacturne", "swablu", "altaria", "zangoose", 
  "seviper", "lunatone", "solrock", "barboach", "whiscash", "corphish", "crawdaunt", "baltoy", "claydol", "lileep", 
  "cradily", "anorith", "armaldo", "feebas", "milotic", "castform", "kecleon", "shuppet", "banette", "duskull",
  "dusclops", "tropius", "chimecho", "absol", "wynaut", "snorunt", "glalie", "spheal", "sealeo",
  "walrein", "clamperl", "huntail", "gorebyss", "relicanth", "luvdisc", "bagon", "shelgon", "salamence",
  "beldum", "metang", "metagross", "regirock", "regice", "registeel", "latias", "latios", "kyogre",
  "groudon", "rayquaza", "jirachi", "deoxys-normal", "turtwig", "grotle", "torterra", "chimchar",
  "monferno", "infernape", "piplup", "prinplup", "empoleon", "starly", "staravia", "staraptor", "bidoof",
  "bibarel", "kricketot", "kricketune", "shinx", "luxio", "luxray", "budew", "roserade", "cranidos",
  "rampardos", "shieldon", "bastiodon", "burmy", "wormadam-plant", "mothim", "combee", "vespiquen",
  "pachirisu", "buizel", "floatzel", "cherubi", "cherrim", "shellos", "gastrodon", "ambipom", "drifloon",
  "drifblim", "buneary", "lopunny", "mismagius", "honchkrow", "glameow", "purugly", "chingling", "stunky",
  "skuntank", "bronzor", "bronzong", "bonsly", "mime-jr", "happiny", "chatot", "spiritomb", "gible",
  "gabite", "garchomp", "munchlax", "riolu", "lucario", "hippopotas", "hippowdon", "skorupi", "drapion",
  "croagunk", "toxicroak", "carnivine", "finneon", "lumineon", "mantyke", "snover", "abomasnow", "weavile",
  "magnezone", "lickilicky", "rhyperior", "tangrowth", "electivire", "magmortar", "togekiss", "yanmega",
  "leafeon", "glaceon", "gliscor", "mamoswine", "porygon-z", "gallade", "probopass", "dusknoir", "froslass",
  "rotom", "uxie", "mesprit", "azelf", "dialga", "palkia", "heatran", "regigigas", "giratina-altered",
  "cresselia", "phione", "manaphy", "darkrai", "shaymin-land", "arceus", "victini", "snivy", "servine",
  "serperior", "tepig", "pignite", "emboar", "oshawott", "dewott", "samurott", "patrat", "watchog",
  "lillipup", "herdier", "stoutland", "purrloin", "liepard", "pansage", "simisage", "pansear", "simisear",
  "panpour", "simipour", "munna", "musharna", "pidove", "tranquill", "unfezant", "blitzle", "zebstrika",
  "roggenrola", "boldore", "gigalith", "woobat", "swoobat", "drilbur", "excadrill", "audino", "timburr",
  "gurdurr", "conkeldurr", "tympole", "palpitoad", "seismitoad", "throh", "sawk", "sewaddle", "swadloon",
  "leavanny", "venipede", "whirlipede", "scolipede", "cottonee", "whimsicott", "petilil", "lilligant",
  "basculin-red-striped", "sandile", "krokorok", "krookodile", "darumaka", "darmanitan-standard", "maractus",
  "dwebble", "crustle", "scraggy", "scrafty", "sigilyph", "yamask", "cofagrigus", "tirtouga", "carracosta",
  "archen", "archeops", "trubbish", "garbodor", "zorua", "zoroark", "minccino", "cinccino", "gothita",
  "gothorita", "gothitelle", "solosis", "duosion", "reuniclus", "ducklett", "swanna", "vanillite",
  "vanillish", "vanilluxe", "deerling", "sawsbuck", "emolga", "karrablast", "escavalier", "foongus",
  "amoonguss", "frillish", "jellicent", "alomomola", "joltik", "galvantula", "ferroseed", "ferrothorn",
  "klink", "klang", "klinklang", "tynamo", "eelektrik", "eelektross", "elgyem", "beheeyem", "litwick",
  "lampent", "chandelure", "axew", "fraxure", "haxorus", "cubchoo", "beartic", "cryogonal", "shelmet",
  "accelgor", "stunfisk", "mienfoo", "mienshao", "druddigon", "golett", "golurk", "pawniard", "bisharp",
  "bouffalant", "rufflet", "braviary", "vullaby", "mandibuzz", "heatmor", "durant", "deino", "zweilous",
  "hydreigon", "larvesta", "volcarona", "cobalion", "terrakion", "virizion", "tornadus-incarnate",
  "thundurus-incarnate", "reshiram", "zekrom", "landorus-incarnate", "kyurem", "keldeo-ordinary",
  "meloetta-aria", "genesect", "chespin", "quilladin", "chesnaught", "fennekin", "braixen", "delphox",
  "froakie", "frogadier", "greninja", "bunnelby", "diggersby", "fletchling", "fletchinder", "talonflame",
  "scatterbug", "spewpa", "vivillon", "litleo", "pyroar", "flabebe", "floette", "florges", "skiddo",
  "gogoat", "pancham", "pangoro", "furfrou", "espurr", "meowstic-male", "honedge", "doublade",
  "aegislash-shield", "spritzee", "aromatisse", "swirlix", "slurpuff", "inkay", "malamar", "binacle",
  "barbaracle", "skrelp", "dragalge", "clauncher", "clawitzer", "helioptile", "heliolisk", "tyrunt",
  "tyrantrum", "amaura", "aurorus", "sylveon", "hawlucha", "dedenne", "carbink", "goomy", "sliggoo",
  "goodra", "klefki", "phantump", "trevenant", "pumpkaboo-average", "gourgeist-average", "bergmite",
  "avalugg", "noibat", "noivern", "xerneas", "yveltal", "zygarde-50", "diancie", "hoopa", "volcanion",
  "rowlet", "dartrix", "decidueye", "litten", "torracat", "incineroar", "popplio", "brionne", "primarina",
  "pikipek", "trumbeak", "toucannon", "yungoos", "gumshoos", "grubbin", "charjabug", "vikavolt",
  "crabrawler", "crabominable", "oricorio-baile", "cutiefly", "ribombee", "rockruff", "lycanroc-midday",
  "wishiwashi-solo", "mareanie", "toxapex", "mudbray", "mudsdale", "dewpider", "araquanid", "fomantis",
  "lurantis", "morelull", "shiinotic", "salandit", "salazzle", "stufful", "bewear", "bounsweet", "steenee",
  "tsareena", "comfey", "oranguru", "passimian", "wimpod", "golisopod", "sandygast", "palossand",
  "pyukumuku", "type-null", "silvally", "minior-red-meteor", "komala", "turtonator", "togedemaru",
  "mimikyu-disguised", "bruxish", "drampa", "dhelmise", "jangmo-o", "hakamo-o", "kommo-o", "tapu-koko",
  "tapu-lele", "tapu-bulu", "tapu-fini", "cosmog", "cosmoem", "solgaleo", "lunala", "nihilego", "buzzwole",
  "pheromosa", "xurkitree", "celesteela", "kartana", "guzzlord", "necrozma", "magearna",
  "marshadow", "poipole", "naganadel", "stakataka", "blacephalon", "zeraora", "meltan", "melmetal", "grookey", "thwackey",
  "rillaboom", "scorbunny", "raboot", "cinderace", "sobble", "drizzile", "inteleon", "skwovet", "greedent", "rookidee",
  "corvisquire", "corviknight", "blipbug", "dottler", "orbeetle", "nickit", "thievul", "gossifleur", "eldegoss", "wooloo",
  "dubwool", "chewtle", "drednaw", "yamper", "boltund", "rolycoly", "carkol", "coalossal", "applin", "flapple",
  "appletun", "silicobra", "sandaconda", "cramorant", "arrokuda", "barraskewda", "toxel", "toxtricity-amped", "sizzlipede", "centiskorch",
  "clobbopus", "grapploct", "sinistea", "polteageist", "hatenna", "hattrem", "hatterene", "impidimp", "morgrem", "grimmsnarl",
  "obstagoon", "perrserker", "cursola", "sirfetchd", "mr-rime", "runerigus", "milcery", "alcremie", "falinks", "pincurchin",
  "snom", "frosmoth", "stonjourner", "eiscue-ice", "indeedee-male", "morpeko-full-belly", "cufant", "copperajah", "dracozolt", "arctozolt",
  "dracovish", "arctovish", "duraludon", "dreepy", "drakloak", "dragapult", "zacian", "zamazenta", "eternatus", "kubfu",
  "urshifu-single-strike", "zarude", "regieleki", "regidrago", "glastrier", "spectrier", "calyrex", "wyrdeer", "kleavor", "ursaluna",
  "basculegion-male", "sneasler", "overqwil", "enamorus-incarnate", "sprigatito", "floragato", "meowscarada", "fuecoco", "crocalor", "skeledirge",
  "quaxly", "quaxwell", "quaquaval", "lechonk", "oinkologne-male", "tarountula", "spidops", "nymble", "lokix", "pawmi",
  "pawmo", "pawmot", "tandemaus", "maushold-family-of-four", "fidough", "dachsbun", "smoliv", "dolliv", "arboliva", "squawkabilly-green-plumage",
  "nacli", "naclstack", "garganacl", "charcadet", "armarouge", "ceruledge", "tadbulb", "bellibolt", "wattrel", "kilowattrel",
  "maschiff", "mabosstiff", "shroodle", "grafaiai", "bramblin", "brambleghast", "toedscool", "toedscruel", "klawf", "capsakid",
  "scovillain", "rellor", "rabsca", "flittle", "espathra", "tinkatink", "tinkatuff", "tinkaton", "wiglett", "wugtrio",
  "bombirdier", "finizen", "palafin-zero", "varoom", "revavroom", "cyclizar", "orthworm", "glimmet", "glimmora", "greavard",
  "houndstone", "flamigo", "cetoddle", "cetitan", "veluza", "dondozo", "tatsugiri-curly", "annihilape", "clodsire", "farigiraf",
  "dudunsparce-two-segment", "kingambit", "great-tusk", "scream-tail", "brute-bonnet", "flutter-mane", "slither-wing", "sandy-shocks", "iron-treads", "iron-bundle",
  "iron-hands", "iron-jugulis", "iron-moth", "iron-thorns", "frigibax", "arctibax", "baxcalibur", "gimmighoul", "gholdengo",
  "great-tusk", "scream-tail", "brute-bonnet", "flutter-mane", "slither-wing", "sandy-shocks", "iron-treads", "iron-bundle",
  "iron-hands", "iron-jugulis", "iron-moth", "iron-thorns", "frigibax", "arctibax", "baxcalibur", "gimmighoul", "gholdengo",
  "wo-chien", "chien-pao", "ting-lu", "chi-yu", "roaring-moon", "iron-valiant", "koraidon", "miraidon",
  "walking-wake", "iron-leaves", "dipplin", "poltchageist", "sinistcha", "okidogi", "munkidori", "fezandipiti",
  "ogerpon", "archaludon", "hydrapple", "gouging-fire", "raging-bolt", "iron-boulder", "iron-crown", "terapagos",
  "pecharunt", "deoxys-attack", "deoxys-defense", "deoxys-speed", "wormadam-sandy", "wormadam-trash", "shaymin-sky",
  "giratina-origin", "rotom-heat", "rotom-wash", "rotom-frost", "rotom-fan", "rotom-mow", "castform-sunny",
  "castform-rainy", "castform-snowy", "basculin-blue-striped", "darmanitan-zen", "meloetta-pirouette", "tornadus-therian",
  "thundurus-therian", "landorus-therian", "kyurem-black", "kyurem-white", "keldeo-resolute", "meowstic-female",
  "aegislash-blade", "pumpkaboo-small", "pumpkaboo-large", "pumpkaboo-super", "gourgeist-small", "gourgeist-large",
  "gourgeist-super", "venusaur-mega", "charizard-mega-x", "charizard-mega-y", "blastoise-mega", "alakazam-mega",
  "gengar-mega", "kangaskhan-mega", "pinsir-mega", "gyarados-mega", "aerodactyl-mega", "mewtwo-mega-x", "mewtwo-mega-y",
  "ampharos-mega", "scizor-mega", "heracross-mega", "houndoom-mega", "tyranitar-mega", "blaziken-mega", "gardevoir-mega",
  "mawile-mega", "aggron-mega", "medicham-mega", "manectric-mega", "banette-mega", "absol-mega", "garchomp-mega",
  "lucario-mega", "abomasnow-mega", "floette-eternal", "latias-mega", "latios-mega", "swampert-mega", "sceptile-mega",
  "sableye-mega", "altaria-mega", "gallade-mega", "audino-mega", "sharpedo-mega", "slowbro-mega", "steelix-mega",
  "pidgeot-mega", "glalie-mega", "diancie-mega", "metagross-mega", "kyogre-primal", "groudon-primal", "rayquaza-mega",
  "pikachu-rock-star", "pikachu-belle", "pikachu-pop-star", "pikachu-phd", "pikachu-libre", "pikachu-cosplay",
  "hoopa-unbound", "camerupt-mega", "lopunny-mega", "salamence-mega", "beedrill-mega", "rattata-alola", "raticate-alola",
  "raticate-totem-alola", "pikachu-original-cap", "pikachu-hoenn-cap", "pikachu-sinnoh-cap", "pikachu-unova-cap",
  "pikachu-kalos-cap", "pikachu-alola-cap", "raichu-alola", "sandshrew-alola", "sandslash-alola", "vulpix-alola",
  "ninetales-alola", "diglett-alola", "dugtrio-alola", "meowth-alola", "persian-alola", "geodude-alola", "graveler-alola",
  "golem-alola", "grimer-alola", "muk-alola", "exeggutor-alola", "marowak-alola", "greninja-battle-bond", "greninja-ash",
  "zygarde-10-power-construct", "zygarde-50-power-construct", "zygarde-complete", "gumshoos-totem", "vikavolt-totem",
  "oricorio-pom-pom", "oricorio-pau", "oricorio-sensu", "lycanroc-midnight", "wishiwashi-school", "lurantis-totem",
  "salazzle-totem", "minior-orange-meteor", "minior-yellow-meteor", "minior-green-meteor", "minior-blue-meteor",
  "minior-indigo-meteor", "minior-violet-meteor", "minior-red", "minior-orange", "minior-yellow", "minior-green",
  "minior-blue", "minior-indigo", "minior-violet", "mimikyu-busted", "mimikyu-totem-disguised", "mimikyu-totem-busted",
  "kommo-o-totem", "magearna-original", "pikachu-partner-cap", "marowak-totem", "ribombee-totem", "rockruff-own-tempo",
  "lycanroc-dusk", "araquanid-totem", "togedemaru-totem", "necrozma-dusk", "necrozma-dawn", "necrozma-ultra", "pikachu-starter",
  "eevee-starter", "pikachu-world-cap", "meowth-galar", "ponyta-galar", "rapidash-galar", "slowpoke-galar", "slowbro-galar",
  "farfetchd-galar", "weezing-galar", "mr-mime-galar", "articuno-galar", "zapdos-galar", "moltres-galar", "slowking-galar",
  "corsola-galar", "zigzagoon-galar", "linoone-galar", "darumaka-galar", "darmanitan-galar-standard", "darmanitan-galar-zen",
  "yamask-galar", "stunfisk-galar", "zygarde-10", "cramorant-gulping", "cramorant-gorging", "toxtricity-low-key",
  "eiscue-noice", "indeedee-female", "morpeko-hangry", "zacian-crowned", "zamazenta-crowned", "eternatus-eternamax",
  "urshifu-rapid-strike", "zarude-dada", "calyrex-ice", "calyrex-shadow", "venusaur-gmax", "charizard-gmax", "blastoise-gmax",
  "butterfree-gmax", "pikachu-gmax", "meowth-gmax", "machamp-gmax", "gengar-gmax", "kingler-gmax", "lapras-gmax",
  "eevee-gmax", "snorlax-gmax", "garbodor-gmax", "melmetal-gmax", "rillaboom-gmax", "cinderace-gmax", "inteleon-gmax",
  "corviknight-gmax", "orbeetle-gmax", "drednaw-gmax", "coalossal-gmax", "flapple-gmax", "appletun-gmax", "sandaconda-gmax",
  "toxtricity-amped-gmax", "centiskorch-gmax", "hatterene-gmax", "grimmsnarl-gmax", "alcremie-gmax", "copperajah-gmax",
  "duraludon-gmax", "urshifu-single-strike-gmax", "urshifu-rapid-strike-gmax", "toxtricity-low-key-gmax", "growlithe-hisui",
  "arcanine-hisui", "voltorb-hisui", "electrode-hisui", "typhlosion-hisui", "qwilfish-hisui", "sneasel-hisui", "samurott-hisui",
  "lilligant-hisui", "zorua-hisui", "zoroark-hisui", "braviary-hisui", "sliggoo-hisui", "goodra-hisui", "avalugg-hisui",
  "decidueye-hisui", "dialga-origin", "palkia-origin", "basculin-white-striped", "basculegion-female", "enamorus-therian",
  "tauros-paldea-combat-breed", "tauros-paldea-blaze-breed", "tauros-paldea-aqua-breed", "wooper-paldea", "oinkologne-female",
  "dudunsparce-three-segment", "palafin-hero", "maushold-family-of-three", "tatsugiri-droopy", "tatsugiri-stretchy",
  "squawkabilly-blue-plumage", "squawkabilly-yellow-plumage", "squawkabilly-white-plumage", "gimmighoul-roaming",
  "koraidon-limited-build", "koraidon-sprinting-build", "koraidon-swimming-build", "koraidon-gliding-build",
  "miraidon-low-power-mode", "miraidon-drive-mode", "miraidon-aquatic-mode", "miraidon-glide-mode", "ursaluna-bloodmoon",
  "ogerpon-wellspring-mask", "ogerpon-hearthflame-mask", "ogerpon-cornerstone-mask", "terapagos-terastal", "terapagos-stellar"
]

POKEMON_SET = set(POKEMON_NAMES)

class PokeApiEndpoints(Enum):
  GET_POKEMON = f"{baseApiUrl}/pokemon"
  GET_TYPE = f"{baseApiUrl}/type"
  GET_MOVE = f"{baseApiUrl}/move"
  GET_ITEM = f"{baseApiUrl}/item"
  GET_GENERATION = f"{baseApiUrl}/generation"
      
# less data for this one since it is not used on the in depth pokemon pages
def fetchPokemonDataByIdentifier(pokemon_identifier : int | str) -> PokemonData:
  url : str = f"{PokeApiEndpoints.GET_POKEMON.value}/{pokemon_identifier}"
  response : SuccessResponse | ErrorResponse = fetchData(url)
  
  if (not response[ErrorResponseKeys.SUCCESS]):
    print(f"Error fetching data for pokemon identifier: {pokemon_identifier}. Error: {response['error']}")
    return {
      PokemonKeys.ID : -1,
      PokemonKeys.NAME : "Unknown",
      PokemonKeys.IMAGE_URL : ""
    }
  
  data = response[SuccessResponseKeys.DATA]
  
  # add type information
  type_info = data.get("types")
  types : list[PokemonType] = []
  
  for entry in type_info:
    type_data = entry.get("type")
    if (type_data):
      type_name = type_data.get("name")
      if isValidType(type_name.capitalize()):
        types.append(PokemonType(type_name.capitalize()))
  
  sprites = data.get("sprites") or {}
  front_default = sprites.get("front_default")

  if not front_default:
    other = sprites.get("other") or {}
    official = other.get("official-artwork") or {}
    front_default = official.get("front_default") or ""
  
  # map the data onto the PokemonData to ensure you have these on the frontend
  pokemonData : PokemonData = {
    PokemonKeys.ID : data.get("id"),
    PokemonKeys.NAME : data.get("name"),
    PokemonKeys.IMAGE_URL : front_default,
    PokemonKeys.TYPES : types
  }
  
  return pokemonData

# this is used to extract all data necessary for the in depth pokemon page
def fetchDetailedPokemonDataByIdentifier(pokemon_identifier : str) -> PokemonData:
  from pokeapi.move import fetchPokemonMove
  from entry import globalDb
  
  print(f"STARTED SEARCHING FOR {pokemon_identifier}")
  
  # check if it is already cached in the database
  detailedPokemonCollection : Collection = globalDb[DatabaseCollections.DETAILED_POKEMON.value.name]
  
  cached_doc = detailedPokemonCollection.find_one({DatabaseCollections.DETAILED_POKEMON.value.key: pokemon_identifier})
  
  if (cached_doc):
    json_str = json_util.dumps(cached_doc)
    clean_dict = json.loads(json_str)
    return clean_dict
  
  url : str = f"{PokeApiEndpoints.GET_POKEMON.value}/{pokemon_identifier}"
  response : SuccessResponse | ErrorResponse = fetchData(url)
  
  if (not response[ErrorResponseKeys.SUCCESS]):
    print(f"Error fetching data for pokemon identifier: {pokemon_identifier}. Error: {response['error']}")
    return {
      PokemonKeys.ID : -1,
      PokemonKeys.NAME : "Unknown",
      PokemonKeys.IMAGE_URL : ""
    }
  
  data = response[SuccessResponseKeys.DATA]
  
  # add type information
  type_info = data.get("types")
  types : list[PokemonType] = []
  
  for entry in type_info:
    type_data = entry.get("type")
    if (type_data):
      type_name = type_data.get("name")
      if isValidType(type_name.capitalize()):
        types.append(PokemonType(type_name.capitalize()))
  
  # evolution chain
  species_url = data.get("species").get("url")
  species_response : SuccessResponse | ErrorResponse = fetchData(species_url)
  species_data = species_response[SuccessResponseKeys.DATA]
  evolution_chain : List[PokemonEvolution] = []
  
  if species_data:
    evolution_chain_url = species_data.get("evolution_chain", {}).get("url")
    if evolution_chain_url:
      evolution_chain = fetchEvolutionChainById(evolution_chain_url)
  
  # stats
  hp = attack = defense = sp_attack = sp_defense = speed = -1
  
  for entry in data.get("stats", []):
    name : str | None = entry.get("stat").get("name")
    base : int = entry.get("base_stat", -1)
    match name:
      case "hp":
        hp = base
      case "attack":
        attack = base
      case "defense":
        defense = base
      case "special-attack":
        sp_attack = base
      case "special-defense":
        sp_defense = base
      case "speed":
        speed = base
  
  # moves
  api_moves_data  = data.get("moves")
  moves : List[MoveData]  = []
  
  for entry in api_moves_data:
    move_data = entry.get("move")
    move_name = move_data.get("name")

    if not move_name: continue

    move : MoveData = fetchPokemonMove(move_name)
    level_learned : int = -1
    
    version_details = entry.get("version_group_details") # list of move info from different games
    
    if (version_details and len(version_details) > 0):
      last_entry = version_details[-1]
      level_learned = last_entry.get("level_learned_at", -1)
      learn_method = last_entry.get("move_learn_method", {}).get("name")
      
      match learn_method:
        case "level-up":
          move[MoveKeys.LEARN_METHOD] = LearnMethod.LEVEL_UP
        case "machine":
          move[MoveKeys.LEARN_METHOD] = LearnMethod.MACHINE
        case "egg":
          move[MoveKeys.LEARN_METHOD] = LearnMethod.EGG
        case "tutor":
          move[MoveKeys.LEARN_METHOD] = LearnMethod.TUTOR
        case _:
          move[MoveKeys.LEARN_METHOD] = LearnMethod.OTHER
    
    move[MoveKeys.LEVEL_LEARNED] = level_learned
    moves.append(move)
  
  # map the data onto the PokemonData to ensure you have these on the frontend
  pokemonData : PokemonData = {
    PokemonKeys.ID : data.get("id"),
    PokemonKeys.NAME : data.get("name"),
    PokemonKeys.IMAGE_URL : data.get("sprites").get("front_default"),
    PokemonKeys.TYPES : types,
    PokemonKeys.HEIGHT : data.get("height"),
    PokemonKeys.WEIGHT : hectogramsToPounds(data.get("weight")),
    PokemonKeys.SHINY_IMAGE_URL : data.get("sprites").get("front_shiny"),
    PokemonKeys.HP : hp,
    PokemonKeys.ATTACK : attack,
    PokemonKeys.DEFENSE : defense,
    PokemonKeys.SP_ATTACK : sp_attack,
    PokemonKeys.SP_DEFENSE : sp_defense,
    PokemonKeys.SPEED : speed,
    PokemonKeys.EVOLUTION_CHAIN : evolution_chain,
    PokemonKeys.MOVES_LEARNED : moves,
  }
  
  document = {
    DatabaseCollections.DETAILED_POKEMON.value.key: pokemon_identifier,
    PokemonKeys.ID: data.get("id"),
    PokemonKeys.NAME: data.get("name"),
    PokemonKeys.IMAGE_URL: data.get("sprites", {}).get("front_default"),
    PokemonKeys.TYPES: types,
    PokemonKeys.HEIGHT: data.get("height"),
    PokemonKeys.WEIGHT: hectogramsToPounds(data.get("weight")),
    PokemonKeys.SHINY_IMAGE_URL: data.get("sprites", {}).get("front_shiny"),
    PokemonKeys.HP: hp,
    PokemonKeys.ATTACK: attack,
    PokemonKeys.DEFENSE: defense,
    PokemonKeys.SP_ATTACK: sp_attack,
    PokemonKeys.SP_DEFENSE: sp_defense,
    PokemonKeys.SPEED: speed,
    PokemonKeys.EVOLUTION_CHAIN: evolution_chain,
    PokemonKeys.MOVES_LEARNED: moves,
  }
  
  clean_document = clean_for_mongo(document)
  
  # add to cache pages to prevent unecessary fetches in the future
  detailedPokemonCollection.insert_one(clean_document)
  
  return pokemonData

  
def fetchAllPokemonOfType(pokemon_type : PokemonType) -> List[PokemonData]:
  from entry import globalDb 
  

  pokemOfTypeCollection : Collection = globalDb[DatabaseCollections.POKEMON_OF_TYPE.value.name]
  pokemonOfTypeDoc = pokemOfTypeCollection.find_one({ DetailedPokemonTypeKeys.TYPE_NAME : pokemon_type })
  
  if pokemonOfTypeDoc:
    return pokemonOfTypeDoc[PokedexKeys.POKEMON]
  
  url : str = f"{PokeApiEndpoints.GET_TYPE.value}/{pokemon_type.lower()}"
  response : SuccessResponse | ErrorResponse = fetchData(url)
  
  if (not response[ErrorResponseKeys.SUCCESS]):
    print(f"Error fetching data for pokemon by type: {pokemon_type}. Error: {response['error']}")
    return []
  
  data = response[SuccessResponseKeys.DATA]
  
  if not data.get("pokemon"):
    print(f"Could not pull of pokemon from data when fetching pokemon of type {pokemon_type}.")
    return []
  
  pokemon : List[PokemonData] = []
  
  for entry in data.get("pokemon"):
    pokemon_entry = entry.get("pokemon", {})
    name: str | None = pokemon_entry.get("name")
    if not name:
      continue
    pokemon.append(fetchPokemonDataByIdentifier(name))
  
  pokemOfTypeCollection.insert_one({
    DetailedPokemonTypeKeys.TYPE_NAME : pokemon_type,
    PokedexKeys.POKEMON : pokemon
  })
  
  return pokemon

def fetchAllPokemonNames() -> List[str]:
  url : str = f"{PokeApiEndpoints.GET_POKEMON}?limit=100000&offset=0"
  response : SuccessResponse | ErrorResponse = fetchData(url)
  
  if (not response[ErrorResponseKeys.SUCCESS]):
    print(f"Error fetching all pokemon. Error: {response['error']}")
    return []
  
  data = response[SuccessResponseKeys.DATA]
  pokemon_names : List[str] = []
  
  for pokemon in data:
    if pokemon:
      name = pokemon["name"]
      if name:
        pokemon_names.append(name)
  
  return pokemon_names

# should fetch from the evolution-chain endpoint from the api
def fetchEvolutionChainById(evolution_chain_url : str | None) -> List[PokemonEvolution]:
  if not evolution_chain_url:
    return []
  
  res : SuccessResponse | ErrorResponse = fetchData(evolution_chain_url)
  if not res[SuccessResponseKeys.SUCCESS]:
    return []
  
  data = res[SuccessResponseKeys.DATA]
  chain = data.get("chain")  
  result : List[PokemonEvolution] = []
  
  def traverse(node):
    species : str = node.get("species", {})
    
    # general info about the pokemon
    pokemon_name: str = species.get("name", "Unknown")
    pokemon_data : PokemonData = fetchPokemonDataByIdentifier(pokemon_name)
    
    # evolution details
    evolution_details  = node.get("evolution_details", [])

    if evolution_details:
      methods : List[str] = []
      for detail in evolution_details:
        methods.append(getEvolutionMethod(detail))
      method_str = ", ".join(methods)
    else:
      method_str = "none"
    
    result.append({
      PokemonEvolutionKeys.POKEMON : pokemon_data,
      PokemonEvolutionKeys.METHOD : method_str
    })
      
    # traverse all evolutions
    for next_node in node.get("evolves_to", []):
      traverse(next_node)
  
  traverse(chain)
  return result

# constructs a string about the evolution method from the details dict defined in the pokeapi(Type EvolutionDetail)
def getEvolutionMethod(details: dict) -> str:
    res = []

    if details.get("min_level"):
        res.append(f"level-up {details['min_level']}")
    if details.get("min_happiness"):
        res.append(f"happiness ≥ {details['min_happiness']}")
    if details.get("min_beauty"):
        res.append(f"beauty ≥ {details['min_beauty']}")
    if details.get("min_affection"):
        res.append(f"affection ≥ {details['min_affection']}")
    if details.get("item"):
        res.append(f"using {details['item']['name']}")
    if details.get("gender"):
        res.append(f"gender: {details['gender']}")
    if details.get("held_item"):
        res.append(f"holding {details['held_item']['name']}")
    if details.get("known_move"):
        res.append(f"knows move {details['known_move']['name']}")
    if details.get("known_move_type"):
        res.append(f"knows move type {details['known_move_type']['name']}")
    if details.get("location"):
        res.append(f"at {details['location']['name']}")
    if details.get("needs_overworld_rain"):
        res.append("while raining")
    if details.get("relative_physical_stats") is not None:
        val = details['relative_physical_stats']
        match val:
            case 1:
                res.append("Attack > Defense")
            case 0:
                res.append("Attack = Defense")
            case -1:
                res.append("Attack < Defense")
    if details.get("time_of_day"):
        res.append(details["time_of_day"])
    if details.get("trade_species"):
        res.append(f"Trade for {details['trade_species']['name']}")

    if not res:
        return "Other"

    return ", ".join(res)
  