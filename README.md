# 404Stats Demo Site

> Static demo of the 404Stats Minecraft statistics plugin — pre-generated data, no server needed.

**[demo.404gnf.de](https://demo.404gnf.de)**

---

## What This Is

This is a fully static, read-only demo of the [404Stats](https://github.com/404DiscNotFound/404Stats) web panel. It showcases all six tracking modules with pre-generated statistics for 15 fictional players across 3 worlds and 2 community projects.

No Minecraft server, no database, no backend — just HTML, CSS, JavaScript, and JSON files. Deploy anywhere that serves static files (Netlify, GitHub Pages, any web host).

---

## Modules Shown

| Module | Demo Data |
| :--- | :--- |
| ⛏ **Blocks** | 419K blocks mined/placed by 15 players, trend charts, hall of fame |
| ⚔ **NPC Combat** | 20K+ kills, entity index, weapon usage across mobs and NPCs |
| 👟 **Movement** | 800M+ cm traveled, biome grid with 60% unlocked, 17 movement types |
| 🏭 **Production** | 15K items crafted/smelted/smithed, station distribution |
| 🔗 **Interactions** | Container opens, doors, bells, animal feeding, bucket actions |
| 🌍 **Worlds** | Overworld, Nether, and End with per-world aggregated stats |

Also includes **2 projects** (Stone Castle, Wheat Farm) with contributors, timelines, and achievements.

---

## Tech Stack

| Layer | Tech |
| :--- | :--- |
| Frontend | Vanilla JavaScript (no framework, no build step) |
| Styling | Plain CSS with custom properties |
| Charts | CSS conic-gradient donuts + inline SVG trend charts |
| Data | 98 pre-generated JSON files mimicking the live API |
| Routing | Client-side SPA with `history.pushState` |
| Hosting | Any static file server — Netlify, GitHub Pages, nginx, etc. |

---

## Folder Structure

```
├── index.html            # Landing page shell
├── demo.js               # SPA with static JSON loader (modded from app.local.js)
├── styles.css            # Full 404Stats stylesheet
├── logo-404.svg          # Brand asset
├── server-icon.png       # Placeholder server icon
├── _redirects            # Netlify SPA routing rules
├── admin/                # Admin panel (static demo)
│   ├── index.html
│   ├── admin.css
│   └── admin.js
├── demo-data/            # 98 JSON files simulating API responses
│   ├── getModuleStatus.json
│   ├── getServerData_*.json
│   ├── getPlayerData_*.json
│   ├── getEntityData.json
│   ├── getMovementData.json
│   ├── getProductionData.json
│   ├── getInteractionData.json
│   ├── getWorldList.json
│   ├── getWorldData_*.json
│   ├── getProjects.json
│   ├── getProjectData_*.json
│   └── ... (search, block index, auth, ping)
└── generate_demo_data.py # Python script that generated all demo JSONs
```

---

## Related Projects

| Project | Link |
| :--- | :--- |
| 404Stats Plugin | Closed Source until beta state |
| Project Website | [mcstats.404gnf.de](https://mcstats.404gnf.de) |

---

## License

This demo site is part of the 404Stats project, a non-profit effort by **404DiscNotFound** for the **404GameNotFound Community**.

Please respect the project and community links when using, forking, or publicly showcasing this demo.
