#!/usr/bin/env python3
"""Generate all demo JSON data files for 404Stats demo website."""
import json, os, random, time, math

OUT = "/Users/talonachris/Coding/DEMO/demo-data"
os.makedirs(OUT, exist_ok=True)
random.seed(42)

TS_BASE = int(time.time() * 1000) - 90 * 24 * 3600 * 1000  # 90 days ago

def ts(days_ago=0):
    return TS_BASE + int((90 - days_ago) * 24 * 3600 * 1000) + random.randint(-3600000, 3600000)

# ── Players ──────────────────────────────────────────────
PLAYERS = [
    ("Talonachris",       "550e8400-e29b-41d4-a716-446655440001", 1.00),
    ("SirBuildalot",      "550e8400-e29b-41d4-a716-446655440002", 0.75),
    ("xXDragonslayerXx",  "550e8400-e29b-41d4-a716-446655440003", 0.60),
    ("FarmerGreta",       "550e8400-e29b-41d4-a716-446655440004", 0.55),
    ("MinerMax99",        "550e8400-e29b-41d4-a716-446655440005", 0.50),
    ("EnderExplorer",     "550e8400-e29b-41d4-a716-446655440006", 0.48),
    ("NetherKnight_42",   "550e8400-e29b-41d4-a716-446655440007", 0.45),
    ("CraftyBee",         "550e8400-e29b-41d4-a716-446655440008", 0.42),
    ("RedstoneRaven",     "550e8400-e29b-41d4-a716-446655440009", 0.38),
    ("OceanBlade",        "550e8400-e29b-41d4-a716-446655440010", 0.35),
    ("PixelPingu",        "550e8400-e29b-41d4-a716-446655440011", 0.30),
    ("BlockBaron",        "550e8400-e29b-41d4-a716-446655440012", 0.28),
    ("GreenThorn",        "550e8400-e29b-41d4-a716-446655440013", 0.25),
    ("SilverWolf_MC",     "550e8400-e29b-41d4-a716-446655440014", 0.22),
    ("LavaLilly",         "550e8400-e29b-41d4-a716-446655440015", 0.18),
]

WORLDS = [
    ("world", "NORMAL", "DEFAULT", "Overworld"),
    ("world_nether", "NETHER", "DEFAULT", "Nether"),
    ("world_the_end", "THE_END", "DEFAULT", "The End"),
]

WORLD_WEIGHTS = {"world": 0.65, "world_nether": 0.25, "world_the_end": 0.10}

BLOCK_MATERIALS = [
    ("STONE", "Building", "Mined"), ("DEEPSLATE", "Building", "Mined"),
    ("DIRT", "Nature", "Mined"), ("GRASS_BLOCK", "Nature", "Mined"),
    ("OAK_LOG", "Nature", "Mined"), ("BIRCH_LOG", "Nature", "Mined"),
    ("COBBLESTONE", "Building", "Both"), ("STONE_BRICKS", "Building", "Placed"),
    ("OAK_PLANKS", "Building", "Placed"), ("SPRUCE_PLANKS", "Building", "Placed"),
    ("IRON_ORE", "Ores", "Mined"), ("COAL_ORE", "Ores", "Mined"),
    ("DIAMOND_ORE", "Ores", "Mined"), ("COPPER_ORE", "Ores", "Mined"),
    ("GOLD_ORE", "Ores", "Mined"), ("NETHERRACK", "Nether", "Mined"),
    ("NETHER_BRICKS", "Nether", "Both"), ("BLACKSTONE", "Nether", "Both"),
    ("END_STONE", "Other", "Mined"), ("OBSIDIAN", "Other", "Mined"),
    ("SAND", "Nature", "Mined"), ("GRAVEL", "Nature", "Mined"),
    ("GLASS", "Building", "Placed"), ("FURNACE", "Tech", "Placed"),
    ("CHEST", "Tech", "Placed"), ("TORCH", "Tech", "Placed"),
]

ENTITY_TYPES = [
    ("ZOMBIE", "MOB"), ("SKELETON", "MOB"), ("CREEPER", "MOB"),
    ("SPIDER", "MOB"), ("ENDERMAN", "MOB"), ("PIGLIN", "MOB"),
    ("WITHER_SKELETON", "MOB"), ("BLAZE", "MOB"), ("GHAST", "MOB"),
    ("ENDER_DRAGON", "MOB"), ("VILLAGER", "NPC"), ("IRON_GOLEM", "NPC"),
    ("WANDERING_TRADER", "NPC"),
]

MOVEMENT_TYPES = ["WALK","SPRINT","SNEAK","SWIM","WALK_UNDERWATER","WALK_ON_WATER",
    "CLIMB","FALL","ELYTRA","CREATIVE_FLY","BOAT","MINECART","PIG","HORSE",
    "STRIDER","JUMP","TELEPORT"]
MOVE_WEIGHTS = {"WALK":0.40,"SPRINT":0.18,"SNEAK":0.05,"SWIM":0.04,"WALK_UNDERWATER":0.02,
    "WALK_ON_WATER":0.01,"CLIMB":0.02,"FALL":0.02,"ELYTRA":0.05,"CREATIVE_FLY":0.01,
    "BOAT":0.04,"MINECART":0.03,"PIG":0.01,"HORSE":0.03,"STRIDER":0.02,
    "JUMP":0.05,"TELEPORT":0.02}

PRODUCTION_TYPES = ["CRAFTING","SMELTING","SMITHING","STONECUTTING"]
PRODUCTION_ITEMS = {
    "CRAFTING": ["OAK_PLANKS","STICK","CRAFTING_TABLE","CHEST","FURNACE","TORCH","IRON_INGOT","GOLDEN_APPLE"],
    "SMELTING": ["IRON_INGOT","GOLD_INGOT","COPPER_INGOT","GLASS","STONE","SMOOTH_STONE"],
    "SMITHING": ["NETHERITE_INGOT","NETHERITE_SWORD","NETHERITE_PICKAXE"],
    "STONECUTTING": ["STONE_BRICKS","STONE_SLAB","STONE_STAIRS","CHISELED_STONE_BRICKS"],
}
PRODUCTION_STATIONS = {"CRAFTING":"CRAFTING_TABLE","SMELTING":"FURNACE","SMITHING":"SMITHING_TABLE","STONECUTTING":"STONECUTTER"}

INTERACTION_GROUPS = {
    "CONTAINER": {"types":["OPEN_CONTAINER"],"targets":["CHEST","TRAPPED_CHEST","BARREL","SHULKER_BOX","ENDER_CHEST","HOPPER","DISPENSER","DROPPER","BREWING_STAND"]},
    "UTILITY_BLOCK": {"types":["OPEN_UTILITY"],"targets":["CRAFTING_TABLE","FURNACE","BLAST_FURNACE","SMOKER","ANVIL","ENCHANTING_TABLE","GRINDSTONE","LOOM","SMITHING_TABLE","STONECUTTER"]},
    "DOORS_AND_SWITCHES": {"types":["TOGGLE_DOOR","TOGGLE_TRAPDOOR","TOGGLE_FENCE_GATE","PRESS_BUTTON","TOGGLE_LEVER"],"targets":["OAK_DOOR","SPRUCE_DOOR","IRON_DOOR","OAK_TRAPDOOR","SPRUCE_FENCE_GATE","STONE_BUTTON","LEVER"]},
    "SPECIAL_BLOCK": {"types":["RING_BELL","PLAY_NOTE_BLOCK","SLEEP_IN_BED"],"targets":["BELL","NOTE_BLOCK","WHITE_BED"]},
    "ANIMAL": {"types":["SHEAR_ENTITY","FEED_ENTITY","MILK_ENTITY"],"targets":["SHEEP","COW","PIG","CHICKEN","HORSE","MOOSHROOM"]},
    "ENTITY": {"types":["INTERACT_ENTITY"],"targets":["VILLAGER","WANDERING_TRADER","ARMOR_STAND","ITEM_FRAME"]},
    "BUCKET": {"types":["BUCKET_FILL","BUCKET_EMPTY"],"targets":["WATER","LAVA","POWDER_SNOW"]},
}

PROJECTS = [
    {"slug":"stonecastle","name":"Stone Castle","creator_uuid":"550e8400-e29b-41d4-a716-446655440002","creator_name":"SirBuildalot","members":["550e8400-e29b-41d4-a716-446655440001","550e8400-e29b-41d4-a716-446655440002","550e8400-e29b-41d4-a716-446655440005","550e8400-e29b-41d4-a716-446655440012"]},
    {"slug":"wheatfarm","name":"Wheat Farm","creator_uuid":"550e8400-e29b-41d4-a716-446655440004","creator_name":"FarmerGreta","members":["550e8400-e29b-41d4-a716-446655440004","550e8400-e29b-41d4-a716-446655440008","550e8400-e29b-41d4-a716-446655440013","550e8400-e29b-41d4-a716-446655440015"]},
]

GAME_MODES = ["SURVIVAL","CREATIVE"]
MODE_WEIGHTS = {"SURVIVAL":0.88,"CREATIVE":0.12}

def fmt(v):
    if v >= 1_000_000: return f"{v/1_000_000:.1f}M".replace(".0M","M")
    if v >= 1000: return f"{v/1000:.1f}K".replace(".0K","K")
    return str(v)

def pct(part, total):
    return round(part * 1000 / max(1, total)) / 10

def pick_world():
    r = random.random()
    if r < 0.65: return "world"
    if r < 0.90: return "world_nether"
    return "world_the_end"

# ═══════════════════════════════════════════════════════════
# MODULE STATUS
# ═══════════════════════════════════════════════════════════
json.dump({"success":True,"blocks":True,"npc_combat":True,"movement":True,"production":True,"interactions":True,"worlds":True},
    open(f"{OUT}/getModuleStatus.json","w"))

# ═══════════════════════════════════════════════════════════
# BLOCK STATS
# ═══════════════════════════════════════════════════════════
def gen_block_stats(mode_filter="SURVIVAL"):
    total_mined, total_placed = 0, 0
    player_set = set()
    block_types = set()
    top_blocks = {}
    top_miners = {}
    top_builders = {}
    world_mined = {}
    world_placed = {}
    cat_mined = {}
    cat_placed = {}

    for pname, puuid, scale in PLAYERS:
        p_mined = int(random.randint(2000, 80000) * scale)
        p_placed = int(random.randint(1000, 40000) * scale)
        if mode_filter == "CREATIVE":
            p_mined = int(p_mined * 0.03)
            p_placed = int(p_placed * 0.08)
        elif mode_filter == "ALL":
            p_mined += int(p_mined * 0.03)
            p_placed += int(p_placed * 0.08)

        if p_mined + p_placed > 0:
            player_set.add(puuid)

        top_miners[puuid] = top_miners.get(puuid, {"uuid":puuid,"player_name":pname,"mined":0})
        top_miners[puuid]["mined"] += p_mined
        top_builders[puuid] = top_builders.get(puuid, {"uuid":puuid,"player_name":pname,"placed":0})
        top_builders[puuid]["placed"] += p_placed

        for _ in range(random.randint(8, 20)):
            mat, cat, _ = random.choice(BLOCK_MATERIALS)
            w = pick_world()
            m = int(random.random() * p_mined * 0.15)
            pl = int(random.random() * p_placed * 0.15)
            total_mined += m; total_placed += pl
            block_types.add(mat)

            k = (mat, cat)
            top_blocks[k] = top_blocks.get(k, {"material":mat,"category":cat,"mined":0,"placed":0,"players":set()})
            top_blocks[k]["mined"] += m
            top_blocks[k]["placed"] += pl
            top_blocks[k]["players"].add(puuid)

            world_mined[w] = world_mined.get(w, 0) + m
            world_placed[w] = world_placed.get(w, 0) + pl
            cat_mined[cat] = cat_mined.get(cat, 0) + m
            cat_placed[cat] = cat_placed.get(cat, 0) + pl

    all_blocks = [(k, v) for k, v in top_blocks.items()]
    all_blocks.sort(key=lambda x: x[1]["mined"] + x[1]["placed"], reverse=True)
    top_list = []
    total = total_mined + total_placed
    for i, (k, v) in enumerate(all_blocks[:25]):
        top_list.append({"rank":i+1,"material":v["material"],"display_name":v["material"].replace("_"," ").title(),
            "category":v["category"],"mined":v["mined"],"placed":v["placed"],
            "total":v["mined"]+v["placed"],"players":len(v["players"]),
            "percent":pct(v["mined"]+v["placed"], total)})

    miners_sorted = sorted(top_miners.values(), key=lambda x: x["mined"], reverse=True)
    builders_sorted = sorted(top_builders.values(), key=lambda x: x["placed"], reverse=True)
    for i, m in enumerate(miners_sorted[:25]): m["rank"] = i+1
    for i, b in enumerate(builders_sorted[:25]): b["rank"] = i+1

    world_dist = []
    for w, _, _, dn in WORLDS:
        wm = world_mined.get(w, 0)
        wp = world_placed.get(w, 0)
        wt = wm + wp
        world_dist.append({"world_name":w,"display_name":dn,"mined":wm,"placed":wp,"total":wt,"percent":pct(wt,total)})

    cat_dist = []
    for cat in ["Ores","Nature","Tech","Building","Nether","Other"]:
        cm = cat_mined.get(cat, 0)
        cp = cat_placed.get(cat, 0)
        ct = cm + cp
        cat_dist.append({"name":cat,"mined":cm,"placed":cp,"total":ct,"percent":pct(ct,total)})

    days = 30
    trend = []
    for d in range(days, -1, -1):
        m = int(total_mined / days * (0.3 + 0.7 * random.random()))
        p = int(total_placed / days * (0.3 + 0.7 * random.random()))
        trend.append({"date":f"2026-{(6+(d//28))%12+1:02d}-{(d%28)+1:02d}","mined":m,"placed":p})

    fun_facts = [
        f"{fmt(total_mined+total_placed)} blocks tracked across {len(player_set)} players.",
        f"{len(block_types)} unique block types recorded.",
        f"{fmt(total_mined)} blocks mined — that's a lot of pickaxes.",
        f"The most mined block is {all_blocks[0][1]['material'].replace('_',' ').title() if all_blocks else 'Stone'}.",
    ]

    return {
        "success":True,
        "server":{"name":"Demo Server","slug":"demo","mode":mode_filter},
        "summary":{"mined":total_mined,"placed":total_placed,"total":total,
            "players":len(player_set),"block_types":len(block_types),"worlds":3},
        "top_blocks":top_list,"top_miners":miners_sorted[:25],"top_builders":builders_sorted[:25],
        "world_distribution":world_dist,"material_categories":cat_dist,"trend":trend,"fun_facts":fun_facts,
        "assets":{"minecraft_assets_enabled":False,"icon_mode":"emoji"}
    }

for mode in ["SURVIVAL","CREATIVE","ALL"]:
    json.dump(gen_block_stats(mode), open(f"{OUT}/getServerData_{mode.lower()}.json","w"))

# ═══════════════════════════════════════════════════════════
# PLAYER BLOCK DATA (per player)
# ═══════════════════════════════════════════════════════════
for pname, puuid, scale in PLAYERS:
    mined = int(25000 * scale + random.randint(0, 10000))
    placed = int(12000 * scale + random.randint(0, 8000))
    json.dump({
        "success":True,
        "server":{"name":"Demo Server","slug":"demo","mode":"SURVIVAL"},
        "player":{"uuid":puuid,"player_name":pname},
        "summary":{"mined":mined,"placed":placed,"total":mined+placed,"players":1,"block_types":random.randint(8,22)},
        "top_blocks":[{"material":m,"display_name":m.replace("_"," ").title(),"category":c,"mined":int(mined*0.1*r), "placed":int(placed*0.1*r),"total":int((mined+placed)*0.1*r),"percent":r*10} for m,c,_ in random.sample(BLOCK_MATERIALS, min(12,len(BLOCK_MATERIALS))) if (r:=random.random()*0.3+0.05)],
        "world_distribution":[{"world_name":w,"display_name":dn,"mined":int(mined*wt),"placed":int(placed*wt),"total":int((mined+placed)*wt),"percent":wt*100} for w,_,_,dn in WORLDS if (wt:=WORLD_WEIGHTS[w])],
        "material_categories":[{"name":cat,"mined":int(mined*0.2*r),"placed":int(placed*0.1*r),"total":int((mined+placed)*0.15*r),"percent":pct((mined+placed)*0.15*r,mined+placed)} for r in [random.random()*0.5+0.3] for cat in ["Ores","Nature","Building","Nether","Tech","Other"]],
        "trend":[{"date":f"2026-06-{d:02d}","mined":int(mined/30*r),"placed":int(placed/30*r)} for d in range(1,31) if (r:=random.random()*0.5+0.5)],
        "fun_facts":[f"{fmt(mined)} blocks mined.", f"{fmt(placed)} blocks placed.", f"Total: {fmt(mined+placed)} blocks."],
        "assets":{"minecraft_assets_enabled":False,"icon_mode":"emoji"},
        "rankings":{"mined_rank":random.randint(1,15),"placed_rank":random.randint(1,15),"total_rank":random.randint(1,15)}
    }, open(f"{OUT}/getPlayerData_{puuid}.json","w"))

# ═══════════════════════════════════════════════════════════
# ENTITY / NPC COMBAT DATA
# ═══════════════════════════════════════════════════════════
def gen_entity_data(group="ALL", mode="ALL"):
    total_kills, total_deaths = 0, 0
    player_set = set()
    entity_kills, entity_deaths = {}, {}
    top_players_k = {}
    world_k, world_d = {}, {}
    for pname, puuid, scale in PLAYERS:
        k = int(5000 * scale * (0.6+0.4*random.random()))
        d = int(k * random.random() * 0.3)
        if mode == "CREATIVE":
            k = int(k * 0.01); d = 0
        elif mode == "SURVIVAL":
            k = int(k * 0.99); d = int(d * 0.99)
        total_kills += k; total_deaths += d
        if k + d > 0: player_set.add(puuid)
        top_players_k[puuid] = {"uuid":puuid,"player_name":pname,"kills":k,"deaths":d,"total":k+d}
        for _ in range(random.randint(3, 10)):
            et, eg = random.choice(ENTITY_TYPES)
            w = pick_world()
            if group != "ALL" and eg != group: continue
            ek = int(k * random.random() * 0.25)
            ed = int(d * random.random() * 0.25)
            key = (et, eg)
            entity_kills[key] = entity_kills.get(key, {"entity_type":et,"entity_group":eg,"kills":0,"deaths":0,"players":set()})
            entity_kills[key]["kills"] += ek
            entity_kills[key]["deaths"] += ed
            entity_kills[key]["players"].add(puuid)
            world_k[w] = world_k.get(w, 0) + ek
            world_d[w] = world_d.get(w, 0) + ed

    top_entities = sorted(entity_kills.values(), key=lambda x: x["kills"]+x["deaths"], reverse=True)
    total = total_kills + total_deaths
    for i, e in enumerate(top_entities[:50]):
        e["rank"] = i+1
        e["total"] = e["kills"]+e["deaths"]
        e["players"] = len(e["players"])
        e["percent"] = pct(e["total"], total)

    world_dist = []
    for w, _, _, dn in WORLDS:
        wk = world_k.get(w, 0); wd = world_d.get(w, 0); wt = wk+wd
        world_dist.append({"world_name":w,"display_name":dn,"kills":wk,"deaths":wd,"total":wt,"percent":pct(wt,total)})
    mode_dist = [{"display_name":"Survival","total":int(total*0.96),"percent":96.0},{"display_name":"Creative","total":int(total*0.04),"percent":4.0}]
    top_p = sorted(top_players_k.values(), key=lambda x: x["kills"], reverse=True)
    for i, p in enumerate(top_p[:25]): p["rank"] = i+1

    return {
        "success":True,"server":{"name":"Demo Server","slug":"demo","mode":mode},
        "summary":{"kills":total_kills,"deaths":total_deaths,"total":total,"players":len(player_set),"entity_types":len(entity_kills),"worlds":3},
        "top_entities":top_entities[:50],"world_distribution":world_dist,"game_mode_distribution":mode_dist,
        "top_killers":top_p[:25],"top_victims":sorted(top_players_k.values(), key=lambda x: x["deaths"], reverse=True)[:25],
        "assets":{"minecraft_assets_enabled":False,"icon_mode":"emoji"}
    }

json.dump(gen_entity_data("ALL","ALL"), open(f"{OUT}/getEntityData.json","w"))
for pname, puuid, scale in PLAYERS:
    k = int(5000 * scale)
    d = int(k * random.random() * 0.2)
    json.dump({
        "success":True,"server":{"name":"Demo Server","slug":"demo"},
        "player":{"uuid":puuid,"player_name":pname},
        "summary":{"kills":k,"deaths":d,"total":k+d,"entity_types":random.randint(3,12),"worlds":3},
        "top_entities":[{"entity_type":et,"entity_group":eg,"kills":int(k*0.2*r),"deaths":int(d*0.2*r),"total":int((k+d)*0.2*r),"percent":pct((k+d)*0.2*r,k+d),"players":1} for et,eg in random.sample(ENTITY_TYPES,min(8,len(ENTITY_TYPES))) if (r:=random.random()*0.3+0.05)],
        "world_distribution":[{"world_name":w,"display_name":dn,"kills":int(k*wt),"deaths":int(d*wt),"total":int((k+d)*wt),"percent":wt*100} for w,_,_,dn in WORLDS if (wt:=WORLD_WEIGHTS[w])],
        "game_mode_distribution":[{"display_name":"Survival","total":int(k*0.97),"percent":97.0},{"display_name":"Creative","total":int(k*0.03),"percent":3.0}],
        "fun_facts":[f"{fmt(k)} kills recorded.", f"{fmt(d)} deaths."],
        "assets":{"minecraft_assets_enabled":False,"icon_mode":"emoji"}
    }, open(f"{OUT}/getEntityPlayerData_{puuid}.json","w"))

# ═══════════════════════════════════════════════════════════
# MOVEMENT DATA
# ═══════════════════════════════════════════════════════════
def gen_movement_data(mode="ALL"):
    total_cm = 0
    player_set = set()
    type_cm = {}
    world_cm = {}
    top_players = {}
    for pname, puuid, scale in PLAYERS:
        cm = int(800_000_000 * scale * (0.5+0.5*random.random()))
        if mode == "CREATIVE": cm = int(cm * 0.05)
        total_cm += cm
        player_set.add(puuid)
        top_players[puuid] = {"uuid":puuid,"player_name":pname,"distance_cm":cm}
        for _ in range(random.randint(8, 17)):
            mt = random.choice(MOVEMENT_TYPES)
            w = pick_world()
            mc = int(cm * MOVE_WEIGHTS[mt] * (0.5+0.5*random.random()))
            type_cm[mt] = type_cm.get(mt, 0) + mc
            world_cm[w] = world_cm.get(w, 0) + mc

    type_dist = [{"movement_type":mt,"distance_cm":type_cm.get(mt,0),"percent":pct(type_cm.get(mt,0),total_cm)} for mt in MOVEMENT_TYPES]
    world_dist = [{"world_name":w,"display_name":dn,"distance_cm":world_cm.get(w,0),"percent":pct(world_cm.get(w,0),total_cm)} for w,_,_,dn in WORLDS]
    mode_dist = [{"display_name":"Survival","total":int(total_cm*0.94),"percent":94.0},{"display_name":"Creative","total":int(total_cm*0.06),"percent":6.0}]
    top_p = sorted(top_players.values(), key=lambda x: x["distance_cm"], reverse=True)
    for i, p in enumerate(top_p[:25]): p["rank"] = i+1

    # biome grid
    biomes = []
    for b in ["plains","forest","desert","taiga","snowy_plains","swamp","jungle","bamboo_jungle","badlands","savanna","meadow","grove","cherry_grove","dark_forest","flower_forest","old_growth_birch_forest","sunflower_plains","ice_spikes","frozen_peaks","jagged_peaks","stony_peaks","dripstone_caves","lush_caves","deep_dark","mushroom_fields","river","beach","ocean","warm_ocean","lukewarm_ocean","cold_ocean","frozen_ocean","deep_ocean","nether_wastes","crimson_forest","warped_forest","soul_sand_valley","basalt_deltas","end_barrens","end_midlands","end_highlands","small_end_islands","the_end","mangrove_swamp","pale_garden","old_growth_pine_taiga","old_growth_spruce_taiga","windswept_hills","windswept_forest","windswept_savanna","eroded_badlands","wooded_badlands","savanna_plateau","windswept_gravelly_hills","snowy_beach","stony_shore","snowy_slopes","snowy_taiga","frozen_river","cold_ocean_baby","deep_cold_ocean","deep_frozen_ocean","deep_lukewarm_ocean"]:
        biomes.append({"biome_name":b,"unlocked":random.random() < (0.6 if b in ["plains","forest","desert","ocean","river","beach","taiga"] else 0.3)})

    return {
        "success":True,"server":{"name":"Demo Server","slug":"demo","mode":mode},
        "summary":{"distance_cm":total_cm,"players":len(player_set),"movement_types":len(type_cm),"worlds":3,"jumps":int(total_cm/1000000*0.1)},
        "type_distribution":type_dist,"world_distribution":world_dist,"game_mode_distribution":mode_dist,
        "top_travelers":top_p[:25],"biome_grid":biomes,"biome_count":sum(1 for b in biomes if b["unlocked"]),
        "assets":{"minecraft_assets_enabled":False,"icon_mode":"emoji"}
    }

json.dump(gen_movement_data("ALL"), open(f"{OUT}/getMovementData.json","w"))
for pname, puuid, scale in PLAYERS:
    cm = int(800_000_000 * scale)
    json.dump({
        "success":True,"server":{"name":"Demo Server","slug":"demo"},
        "player":{"uuid":puuid,"player_name":pname},
        "summary":{"distance_cm":cm,"jumps":int(cm/1000000*0.1),"movement_types":random.randint(8,17),"worlds":random.randint(1,3)},
        "type_distribution":[{"movement_type":mt,"distance_cm":int(cm*MOVE_WEIGHTS.get(mt,0.02)),"percent":pct(cm*MOVE_WEIGHTS.get(mt,0.02),cm)} for mt in MOVEMENT_TYPES[:10]],
        "world_distribution":[{"world_name":w,"display_name":dn,"distance_cm":int(cm*wt),"percent":wt*100} for w,_,_,dn in WORLDS if (wt:=WORLD_WEIGHTS[w])],
        "game_mode_distribution":[{"display_name":"Survival","total":int(cm*0.96),"percent":96.0},{"display_name":"Creative","total":int(cm*0.04),"percent":4.0}],
        "fun_facts":[f"{fmt(int(cm/100000))} km traveled.", f"{random.randint(100,5000)} jumps."],
        "assets":{"minecraft_assets_enabled":False,"icon_mode":"emoji"}
    }, open(f"{OUT}/getMovementPlayerData_{puuid}.json","w"))

# ═══════════════════════════════════════════════════════════
# PRODUCTION DATA
# ═══════════════════════════════════════════════════════════
def gen_production_data(prod_type="ALL", mode="ALL"):
    total_amt, total_act = 0, 0
    player_set = set()
    type_amt, station_amt = {}, {}
    world_amt = {}
    top_items = {}
    top_players = {}
    for pname, puuid, scale in PLAYERS:
        amt = int(15000 * scale * (0.5+0.5*random.random()))
        act = int(amt * 0.7)
        total_amt += amt; total_act += act
        player_set.add(puuid)
        top_players[puuid] = {"uuid":puuid,"player_name":pname,"total_amount":amt,"total_actions":act}
        for _ in range(random.randint(3, 8)):
            pt = random.choice(PRODUCTION_TYPES)
            if prod_type != "ALL" and pt != prod_type: continue
            st = PRODUCTION_STATIONS[pt]
            mat = random.choice(PRODUCTION_ITEMS[pt])
            w = pick_world()
            a = int(amt * random.random() * 0.2)
            ac = int(act * random.random() * 0.2)
            type_amt[pt] = type_amt.get(pt, 0) + a
            station_amt[st] = station_amt.get(st, 0) + a
            world_amt[w] = world_amt.get(w, 0) + a
            top_items[mat] = top_items.get(mat, {"output_material":mat,"display_name":mat.replace("_"," ").title(),"total_amount":0,"total_actions":0,"players":set()})
            top_items[mat]["total_amount"] += a
            top_items[mat]["total_actions"] += ac
            top_items[mat]["players"].add(puuid)

    t_dist = [{"name":pt,"display_name":pt.title(),"total":type_amt.get(pt,0),"percent":pct(type_amt.get(pt,0),total_amt)} for pt in PRODUCTION_TYPES]
    s_dist = [{"name":st,"display_name":st.replace("_"," ").title(),"total":station_amt.get(st,0),"percent":pct(station_amt.get(st,0),total_amt)} for st in set(PRODUCTION_STATIONS.values())]
    w_dist = [{"world_name":w,"display_name":dn,"total":world_amt.get(w,0),"percent":pct(world_amt.get(w,0),total_amt)} for w,_,_,dn in WORLDS]
    m_dist = [{"display_name":"Survival","total":int(total_amt*0.97),"percent":97.0},{"display_name":"Creative","total":int(total_amt*0.03),"percent":3.0}]
    top_i = sorted(top_items.values(), key=lambda x: x["total_amount"], reverse=True)
    for i, ti in enumerate(top_i[:50]): ti["rank"] = i+1; ti["players"] = len(ti["players"]); ti["percent"] = pct(ti["total_amount"], total_amt)
    top_p = sorted(top_players.values(), key=lambda x: x["total_amount"], reverse=True)
    for i, p in enumerate(top_p[:25]): p["rank"] = i+1

    return {
        "success":True,"server":{"name":"Demo Server","slug":"demo","mode":mode},
        "summary":{"production_type":prod_type,"game_mode":mode,"total_amount":total_amt,"total_actions":total_act,"unique_items":len(top_items),"unique_recipes":len(top_items),"players":len(player_set),"worlds":3},
        "top_items":top_i[:50],"top_players":top_p[:25],
        "type_distribution":t_dist,"station_distribution":s_dist,"world_distribution":w_dist,"game_mode_distribution":m_dist,
        "fun_facts":[f"{fmt(total_amt)} items produced.", f"{len(top_items)} unique items crafted.", f"{fmt(total_act)} production actions."],
        "assets":{"minecraft_assets_enabled":False,"icon_mode":"emoji"}
    }

json.dump(gen_production_data("ALL","ALL"), open(f"{OUT}/getProductionData.json","w"))
for pname, puuid, scale in PLAYERS:
    amt = int(15000 * scale)
    act = int(amt * 0.7)
    json.dump({
        "success":True,"server":{"name":"Demo Server","slug":"demo"},
        "player":{"uuid":puuid,"player_name":pname},
        "summary":{"production_type":"ALL","game_mode":"ALL","total_amount":amt,"total_actions":act,"unique_items":random.randint(4,16),"unique_recipes":random.randint(4,16),"worlds":random.randint(1,3)},
        "top_items":[{"output_material":mat,"display_name":mat.replace("_"," ").title(),"total_amount":int(amt*0.2*r),"total_actions":int(act*0.1*r),"percent":r*20,"rank":i+1} for i,(mat,r) in enumerate([(random.choice(PRODUCTION_ITEMS["CRAFTING"]),random.random()*0.3+0.05) for _ in range(8)])],
        "type_distribution":[{"name":pt,"display_name":pt.title(),"total":int(amt*w),"percent":w*100} for pt,w in [("CRAFTING",0.55),("SMELTING",0.25),("SMITHING",0.10),("STONECUTTING",0.10)]],
        "station_distribution":[{"name":st,"display_name":st.replace("_"," ").title(),"total":int(amt*w),"percent":w*100} for st,w in [("CRAFTING_TABLE",0.45),("FURNACE",0.25),("SMITHING_TABLE",0.10),("STONECUTTER",0.10),("PLAYER_INVENTORY",0.10)]],
        "world_distribution":[{"world_name":w,"display_name":dn,"total":int(amt*wt),"percent":wt*100} for w,_,_,dn in WORLDS if (wt:=WORLD_WEIGHTS[w])],
        "game_mode_distribution":[{"display_name":"Survival","total":int(amt*0.96),"percent":96.0},{"display_name":"Creative","total":int(amt*0.04),"percent":4.0}],
        "fun_facts":[f"{fmt(amt)} items produced.", f"{fmt(act)} actions."],
        "assets":{"minecraft_assets_enabled":False,"icon_mode":"emoji"}
    }, open(f"{OUT}/getProductionPlayerData_{puuid}.json","w"))

# ═══════════════════════════════════════════════════════════
# INTERACTION DATA
# ═══════════════════════════════════════════════════════════
def gen_interaction_data(group="ALL", mode="ALL"):
    total_act = 0
    player_set = set()
    group_dist = {}
    type_dist = {}
    world_dist = {}
    top_targets = {}
    top_players = {}
    for pname, puuid, scale in PLAYERS:
        act = int(5000 * scale * (0.5+0.5*random.random()))
        total_act += act
        player_set.add(puuid)
        top_players[puuid] = {"uuid":puuid,"player_name":pname,"total":act}
        for _ in range(random.randint(5, 15)):
            g = random.choice(list(INTERACTION_GROUPS.keys()))
            if group != "ALL" and g != group: continue
            ig = INTERACTION_GROUPS[g]
            it = random.choice(ig["types"])
            target = random.choice(ig["targets"])
            w = pick_world()
            a = int(act * random.random() * 0.15)
            group_dist[g] = group_dist.get(g, 0) + a
            type_dist[it] = type_dist.get(it, 0) + a
            world_dist[w] = world_dist.get(w, 0) + a
            key = (it, target, g)
            top_targets[key] = top_targets.get(key, {"interaction_type":it,"target_type":target,"target_material":target,"entity_type":"","interaction_group":g,"total":0,"players":set()})
            top_targets[key]["total"] += a
            top_targets[key]["players"].add(puuid)

    g_dist = [{"name":g,"display_name":{"CONTAINER":"Containers","UTILITY_BLOCK":"Utility Blocks","DOORS_AND_SWITCHES":"Doors & Switches","SPECIAL_BLOCK":"Special Blocks","ANIMAL":"Animals","ENTITY":"Entities","BUCKET":"Buckets"}.get(g,g),"total":group_dist.get(g,0),"percent":pct(group_dist.get(g,0),total_act)} for g in INTERACTION_GROUPS]
    t_dist = [{"name":it,"display_name":it.replace("_"," ").title(),"total":type_dist.get(it,0),"percent":pct(type_dist.get(it,0),total_act)} for it in sorted(set(type_dist.keys()))]
    w_dist = [{"world_name":w,"display_name":dn,"total":world_dist.get(w,0),"percent":pct(world_dist.get(w,0),total_act)} for w,_,_,dn in WORLDS]
    m_dist = [{"display_name":"Survival","total":int(total_act*0.97),"percent":97.0},{"display_name":"Creative","total":int(total_act*0.03),"percent":3.0}]
    top_t = sorted(top_targets.values(), key=lambda x: x["total"], reverse=True)
    for i, tt in enumerate(top_t[:20]): tt["rank"] = i+1; tt["display_name"] = tt["target_type"].replace("_"," ").title(); tt["players"] = len(tt["players"])
    top_p = sorted(top_players.values(), key=lambda x: x["total"], reverse=True)
    for i, p in enumerate(top_p[:20]): p["rank"] = i+1; p["types"] = random.randint(2,8)

    return {
        "success":True,"server":{"name":"Demo Server","slug":"demo","mode":mode},
        "summary":{"interaction_group":group,"game_mode":mode,"actions":total_act,"unique_types":len(type_dist),"unique_targets":len(top_targets),"players":len(player_set),"worlds":3},
        "group_distribution":g_dist,"type_distribution":t_dist,"world_distribution":w_dist,"game_mode_distribution":m_dist,
        "top_interactions":top_t[:20],"top_players":top_p[:20],
        "fun_facts":[f"{fmt(total_act)} interactions tracked.", f"{fmt(total_act//len(PLAYERS))} avg per player.", "Chest is the most popular container.", "Door toggling detected — someone's building a base."],
        "assets":{"minecraft_assets_enabled":False,"icon_mode":"emoji"}
    }

json.dump(gen_interaction_data("ALL","ALL"), open(f"{OUT}/getInteractionData.json","w"))
for pname, puuid, scale in PLAYERS:
    act = int(5000 * scale)
    json.dump({
        "success":True,"server":{"name":"Demo Server","slug":"demo"},
        "player":{"uuid":puuid,"player_name":pname},
        "summary":{"interaction_group":"ALL","game_mode":"ALL","actions":act,"unique_types":random.randint(3,10),"unique_targets":random.randint(5,20),"worlds":random.randint(1,3)},
        "group_distribution":[{"name":g,"display_name":{"CONTAINER":"Containers","UTILITY_BLOCK":"Utility Blocks","DOORS_AND_SWITCHES":"Doors & Switches","SPECIAL_BLOCK":"Special Blocks","ANIMAL":"Animals","ENTITY":"Entities","BUCKET":"Buckets"}.get(g,g),"total":int(act*w),"percent":w*100} for g,w in random.sample(list(zip(INTERACTION_GROUPS.keys(),[0.30,0.20,0.15,0.10,0.10,0.08,0.07])),5)],
        "type_distribution":[{"name":it,"display_name":it.replace("_"," ").title(),"total":int(act*0.3),"percent":30} for it in ["OPEN_CONTAINER","TOGGLE_DOOR","BUCKET_FILL","SHEAR_ENTITY","INTERACT_ENTITY"]],
        "world_distribution":[{"world_name":w,"display_name":dn,"total":int(act*wt),"percent":wt*100} for w,_,_,dn in WORLDS if (wt:=WORLD_WEIGHTS[w])],
        "game_mode_distribution":[{"display_name":"Survival","total":int(act*0.97),"percent":97.0},{"display_name":"Creative","total":int(act*0.03),"percent":3.0}],
        "top_interactions":[{"interaction_type":"OPEN_CONTAINER","target_type":"CHEST","target_material":"CHEST","entity_type":"","interaction_group":"CONTAINER","display_name":"Chest","total":int(act*0.15),"rank":1},{"interaction_type":"TOGGLE_DOOR","target_type":"OAK_DOOR","target_material":"OAK_DOOR","entity_type":"","interaction_group":"DOORS_AND_SWITCHES","display_name":"Oak Door","total":int(act*0.08),"rank":2},{"interaction_type":"BUCKET_FILL","target_type":"WATER","target_material":"WATER","entity_type":"","interaction_group":"BUCKET","display_name":"Water","total":int(act*0.06),"rank":3}],
        "fun_facts":[f"{fmt(act)} interactions.", f"Most active: {random.choice(['Container','Doors','Utility'])}."],
        "assets":{"minecraft_assets_enabled":False,"icon_mode":"emoji"}
    }, open(f"{OUT}/getInteractionPlayerData_{puuid}.json","w"))

# ═══════════════════════════════════════════════════════════
# WORLD DATA
# ═══════════════════════════════════════════════════════════
world_list = []
for wname, env, wtype, dn in WORLDS:
    block_p = {"world_name":wname,"display_name":dn,"environment":env,"world_type":wtype,"seed":0,"first_seen":ts(85),"last_seen":ts(0),
        "stats":{"blocks":{"players":12+random.randint(0,3),"mined":int(80000*WORLD_WEIGHTS[wname]),"placed":int(40000*WORLD_WEIGHTS[wname]),"total":int(120000*WORLD_WEIGHTS[wname])},
                 "combat":{"players":10+random.randint(0,4),"kills":int(15000*WORLD_WEIGHTS[wname]),"deaths":int(2000*WORLD_WEIGHTS[wname]),"total":int(17000*WORLD_WEIGHTS[wname])},
                 "movement":{"players":random.randint(8,14),"distance_cm":int(300_000_000*WORLD_WEIGHTS[wname])},
                 "production":{"players":random.randint(8,13),"amount":int(20000*WORLD_WEIGHTS[wname]),"actions":int(14000*WORLD_WEIGHTS[wname])}}}
    world_list.append(block_p)

json.dump({"success":True,"worlds":world_list,"total_worlds":3,"dimensions":{"overworld":1,"nether":1,"the_end":1}},
    open(f"{OUT}/getWorldList.json","w"))

# World detail pages
for wname, env, wtype, dn in WORLDS:
    wt = WORLD_WEIGHTS[wname]
    mined = int(80000 * wt); placed = int(40000 * wt)
    kills = int(15000 * wt); deaths = int(2000 * wt)
    cm = int(300_000_000 * wt); amt = int(20000 * wt); actions = int(14000 * wt)

    # top blocks for world
    top_blocks_w = []
    for mat, cat, _ in random.sample(BLOCK_MATERIALS, min(15, len(BLOCK_MATERIALS))):
        m = int(mined * random.random() * 0.2)
        p = int(placed * random.random() * 0.15)
        top_blocks_w.append({"rank":len(top_blocks_w)+1,"material":mat,"display_name":mat.replace("_"," ").title(),"category":cat,"mined":m,"placed":p,"total":m+p,"players":random.randint(2,12)})
    top_blocks_w.sort(key=lambda x: x["total"], reverse=True)
    for i, b in enumerate(top_blocks_w): b["rank"] = i+1

    # top entities for world
    top_entities_w = []
    for et, eg in random.sample(ENTITY_TYPES, min(10, len(ENTITY_TYPES))):
        k = int(kills * random.random() * 0.3)
        d = int(deaths * random.random() * 0.2)
        top_entities_w.append({"rank":len(top_entities_w)+1,"entity_type":et,"entity_group":eg,"kills":k,"deaths":d,"total":k+d,"players":random.randint(1,8)})
    top_entities_w.sort(key=lambda x: x["total"], reverse=True)
    for i, e in enumerate(top_entities_w): e["rank"] = i+1

    # material categories
    cat_dist = []
    for cat in ["Nature","Building","Nether","Ores","Tech","Other"]:
        t = int(mined * random.random() * 0.25)
        cat_dist.append({"name":cat,"total":t,"percent":pct(t, mined)})

    # movement types
    move_dist = []
    for mt in MOVEMENT_TYPES[:10]:
        mc = int(cm * MOVE_WEIGHTS.get(mt, 0.02) * (0.5+0.5*random.random()))
        move_dist.append({"movement_type":mt,"distance_cm":mc,"percent":pct(mc, cm)})

    # top players
    top_p = []
    for pname, puuid, scale in random.sample(PLAYERS, 5):
        v = int(10000 * scale * wt)
        top_p.append({"rank":len(top_p)+1,"uuid":puuid,"player_name":pname,"value":v})

    json.dump({
        "success":True,
        "world_name":wname,"display_name":dn,"environment":env,"world_type":wtype,"seed":0,
        "first_seen":ts(85),"last_seen":ts(0),
        "summary":{"block_players":random.randint(10,15),"mined":mined,"placed":placed,"blocks_total":mined+placed,
            "entity_players":random.randint(8,13),"kills":kills,"deaths":deaths,"combat_total":kills+deaths,
            "move_players":random.randint(8,14),"distance_cm":cm,
            "prod_players":random.randint(8,13),"total_amount":amt,"total_actions":actions,
            "total_players":random.randint(12,15)},
        "top_blocks":top_blocks_w,"top_entities":top_entities_w,
        "material_categories":cat_dist,"movement_types":move_dist,
        "top_miners":top_p,"top_builders":top_p,"top_killers":top_p,"top_travelers":top_p,"top_producers":top_p
    }, open(f"{OUT}/getWorldData_{wname}.json","w"))

# ═══════════════════════════════════════════════════════════
# PROJECT DATA
# ═══════════════════════════════════════════════════════════
projects_list = []
for proj in PROJECTS:
    mined = int(random.randint(20000, 80000) * 0.5)
    placed = int(mined * (1.1 + random.random() * 0.4))
    members = []
    for muuid in proj["members"]:
        pname = next(p[0] for p in PLAYERS if p[1] == muuid)
        members.append({"uuid":muuid,"player_name":pname,"active":True,"mined":int(mined/len(proj["members"])*random.random()*1.5),"placed":int(placed/len(proj["members"])*random.random()*1.5)})
    projects_list.append({
        "slug":proj["slug"],"name":proj["name"],"created_by_uuid":proj["creator_uuid"],"created_by_name":proj["creator_name"],
        "created_at":ts(60),"updated_at":ts(1),"members_count":len(proj["members"]),
        "mined":mined,"placed":placed,"total":mined+placed,"net":placed-mined,
        "members":members,"top_contributor":{"uuid":proj["members"][0],"player_name":next(p[0] for p in PLAYERS if p[1]==proj["members"][0])}
    })

json.dump({"success":True,"server":{"name":"Demo Server","slug":"demo"},"projects":projects_list,"assets":{"minecraft_assets_enabled":False,"icon_mode":"emoji"}},
    open(f"{OUT}/getProjects.json","w"))

# Individual project details
for proj in PROJECTS:
    mined = int(random.randint(20000, 80000) * 0.5)
    placed = int(mined * 1.3)
    members = []
    for muuid in proj["members"]:
        pname = next(p[0] for p in PLAYERS if p[1] == muuid)
        members.append({"uuid":muuid,"player_name":pname,"mined":int(mined/len(proj["members"])),"placed":int(placed/len(proj["members"])),"total":int(mined/len(proj["members"]))+int(placed/len(proj["members"]))})
    json.dump({
        "success":True,"server":{"name":"Demo Server","slug":"demo"},
        "project":{"project_slug":proj["slug"],"project_name":proj["name"],"created_by_uuid":proj["creator_uuid"],"created_by_name":proj["creator_name"],"created_at":ts(60),"updated_at":ts(1)},
        "summary":{"mined":mined,"placed":placed,"total":mined+placed,"net_build_gain":placed-mined,"members":len(proj["members"]),"block_types":random.randint(8,20),"worlds":1},
        "top_contributor":{"uuid":proj["members"][0],"player_name":next(p[0] for p in PLAYERS if p[1]==proj["members"][0]),"total":int(mined*0.4+placed*0.4)},
        "top_block":{"material":"STONE_BRICKS","display_name":"Stone Bricks","mined":int(mined*0.1),"placed":int(placed*0.2),"total":int(mined*0.1+placed*0.2)},
        "material_categories":[{"name":cat,"mined":int(mined*0.2),"placed":int(placed*0.15),"total":int((mined+placed)*0.18),"percent":pct((mined+placed)*0.18,mined+placed)} for cat in ["Building","Nature","Tech","Nether","Ores","Other"]],
        "world_distribution":[{"world_name":"world","display_name":"Overworld","mined":mined,"placed":placed,"total":mined+placed,"percent":100.0}],
        "top_blocks":[{"rank":i+1,"material":mat,"display_name":mat.replace("_"," ").title(),"category":cat,"mined":int(mined*0.1*r),"placed":int(placed*0.08*r),"total":int((mined+placed)*0.09*r),"players":random.randint(1,4)} for i,(mat,cat,_) in enumerate(random.sample(BLOCK_MATERIALS,min(15,len(BLOCK_MATERIALS)))) if (r:=random.random()*0.4+0.1)],
        "contributors":members,
        "trend":[{"date":f"2026-06-{d:02d}","mined":int(mined/30*r),"placed":int(placed/30*r)} for d in range(1,31) if (r:=random.random()*0.7+0.3)],
        "achievements":[{"name":"First Block","description":"Place the first block.","unlocked":True,"progress":100},
            {"name":"100 Blocks","description":"Place 100 blocks.","unlocked":True,"progress":100},
            {"name":"1K Blocks","description":"Place 1,000 blocks.","unlocked":True,"progress":100},
            {"name":"10K Blocks","description":"Place 10,000 blocks.","unlocked":mined+placed>10000,"progress":min(100,int((mined+placed)/10000*100))},
            {"name":"Net Positive","description":"More placed than mined.","unlocked":placed>mined,"progress":100 if placed>mined else int(placed/max(mined,1)*100)}],
        "fun_facts":[f"{fmt(mined+placed)} blocks tracked.", f"{len(proj['members'])} contributors.", f"Net build gain: {fmt(placed-mined)}."],
        "assets":{"minecraft_assets_enabled":False,"icon_mode":"emoji"}
    }, open(f"{OUT}/getProjectData_{proj['slug']}.json","w"))

# ═══════════════════════════════════════════════════════════
# SEARCH DATA
# ═══════════════════════════════════════════════════════════
search_players = [{"uuid":p[1],"player_name":p[0],"mined":int(25000*p[2]),"placed":int(12000*p[2]),"total":int(37000*p[2])} for p in PLAYERS]
json.dump({"success":True,"players":search_players}, open(f"{OUT}/searchPlayers.json","w"))
entity_search = [{"uuid":p[1],"player_name":p[0],"kills":int(5000*p[2]),"deaths":int(1000*p[2]),"total":int(6000*p[2])} for p in PLAYERS]
json.dump({"success":True,"players":entity_search}, open(f"{OUT}/searchEntityPlayers.json","w"))
move_search = [{"uuid":p[1],"player_name":p[0],"distance_cm":int(800_000_000*p[2])} for p in PLAYERS]
json.dump({"success":True,"players":move_search}, open(f"{OUT}/searchMovementPlayers.json","w"))
prod_search = [{"uuid":p[1],"player_name":p[0],"total_amount":int(15000*p[2]),"total_actions":int(10000*p[2])} for p in PLAYERS]
json.dump({"success":True,"players":prod_search}, open(f"{OUT}/searchProductionPlayers.json","w"))
interact_search = [{"uuid":p[1],"player_name":p[0],"actions":int(5000*p[2])} for p in PLAYERS]
json.dump({"success":True,"players":interact_search}, open(f"{OUT}/searchInteractionPlayers.json","w"))

# ═══════════════════════════════════════════════════════════
# BLOCK INDEX
# ═══════════════════════════════════════════════════════════
block_index = []
for i, (mat, cat, _) in enumerate(BLOCK_MATERIALS):
    m = random.randint(500, 50000); p = random.randint(200, 30000)
    block_index.append({"rank":i+1,"material":mat,"display_name":mat.replace("_"," ").title(),"category":cat,"mined":m,"placed":p,"total":m+p,"players":random.randint(2,14),"percent":0})
total_bi = sum(b["total"] for b in block_index)
for b in block_index: b["percent"] = pct(b["total"], total_bi)
block_index.sort(key=lambda x: x["total"], reverse=True)
for i, b in enumerate(block_index): b["rank"] = i+1
json.dump({"success":True,"blocks":block_index[:25],"summary":{"total":total_bi,"unique_blocks":len(block_index),"players":15},"assets":{"minecraft_assets_enabled":False,"icon_mode":"emoji"}},
    open(f"{OUT}/getBlockIndex.json","w"))

# ═══════════════════════════════════════════════════════════
# AUTH (no password for demo)
# ═══════════════════════════════════════════════════════════
json.dump({"password_required":False,"authenticated":True}, open(f"{OUT}/getLocalAuthStatus.json","w"))
json.dump({"success":True,"service":"404Stats Local Webserver","storage":"local"}, open(f"{OUT}/ping.json","w"))

print(f"✅ Generated {len(os.listdir(OUT))} JSON files in {OUT}")
