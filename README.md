# Project-CR

Un simulatore di **Clash Royale** scritto in Python, con interfaccia grafica in `tkinter`.
Piazzi le truppe sull'arena, gestisci l'elisir, cicli le carte del mazzo e cerchi di abbattere le torri avversarie prima che scada il tempo.

> Progetto amatoriale e non ufficiale. Clash Royale è un marchio di [Supercell](https://supercell.com/en/); gli asset e i nomi appartengono ai rispettivi proprietari.

**Stato attuale:** versione 1.3 giocabile, in lavorazione la 1.4.

---

## Funzionalità (v1.3)

- **Menu iniziale** con pulsanti *Click to battle*, *Edit Deck* e crediti
- **Editor del mazzo**: scegli 8 carte (il gioco non parte con un mazzo incompleto)
- **Arena** con sfondo, torri principesse e torre del re per entrambe le squadre, con barre di vita
- **Elisir** da 0 a 10 che si rigenera nel tempo, con barra viola e contatore numerico
- **Ciclo delle carte**: 4 carte in mano; quando ne giochi una, entra la quinta del mazzo e quella usata va in fondo
- **Timer di partita** da 3 minuti
- **Truppe e magie** con statistiche definite in JSON (velocità, vita, danno, raggio, visione, velocità d'attacco, costo)
- **Sprite** blu e rosse caricate automaticamente dalla cartella `Renderers`

### Carte disponibili

| Carta | Tipo | Elisir |
|---|---|---|
| Zap | magia | 2 |
| Wall Breaker | truppa | 2 |
| Knight | truppa | 3 |
| Valkyrie | truppa | 4 |
| Mini P.E.K.K.A | truppa | 4 |
| Hog Rider | truppa | 4 |
| Fireball | magia | 4 |
| P.E.K.K.A | truppa | 7 |

Le statistiche sono in `project_CR 1.3/troopDictionary.json`. Le voci che finiscono con `F` sono truppe alleate, quelle con `E` sono nemiche.

---

## Requisiti

- **Python 3.10+** (testato con 3.11 e 3.12)
- **tkinter** (incluso nell'installer ufficiale di Python; su Linux: `sudo apt install python3-tk`)
- **Pillow**

```bash
pip install pillow
```

## Come avviare il gioco

```bash
cd "project_CR 1.3"
python _main.py
```

## Come si gioca

| Azione | Comando |
|---|---|
| Selezionare una carta | tasti **1**, **2**, **3**, **4** (la carta scelta diventa rossa) |
| Schierare la carta | **click sinistro** sull'arena |
| Modificare il mazzo | pulsante *Edit Deck* dal menu |

Regole di base:

- Le **truppe** si possono piazzare solo nella tua metà campo (la metà inferiore dell'arena).
- Le **magie** si possono lanciare ovunque.
- Se non hai abbastanza elisir la carta non viene giocata.
- L'elisir parte da 6, ne ottieni 1 ogni 2,8 secondi e il massimo è 10.
- La partita termina quando cade la torre del re avversaria o scade il timer.

---

## Struttura del progetto

```
Project-CR/
├── project_CR 1.0/   Prima versione: script unico, con emote, video d'intro e schermata di vittoria
├── project_CR 1.1/   Seconda versione, con pezzi di codice separati (mazzo, elisir, torri, pathfinding...)
├── project_CR 1.2/   Terza versione: sprite, campo di battaglia, pagina iniziale, esperimenti e prove
└── project_CR 1.3/   Versione attuale, divisa in moduli
```

### Moduli della 1.3

| File | Ruolo |
|---|---|
| `_main.py` | Punto di ingresso: crea i manager e avvia il gioco |
| `CanvasManager.py` | Finestra, menu, editor del mazzo, arena, UI, elisir, timer, input e danni alle torri |
| `Troop.py` | Comportamento di una truppa alleata (movimento, bersagli, attacco) |
| `TroopEnemy.py` | Comportamento delle truppe nemiche |
| `TroopManager.py` | Carica le statistiche da `troopDictionary.json` |
| `RenderingManager.py` | Carica le sprite dalla cartella `Renderers` |
| `PathFinder.py` | Cerca file e cartelle del progetto sul disco |
| `EnemyAI.py` | Segnaposto per l'IA avversaria (`TrainerFikova`) |
| `TaskManager.py` | Segnaposto |
| `troopDictionary.json` | Statistiche di truppe e magie |
| `Renderers/` | Sprite: `blueTroops`, `redTroops`, `mainRenderers` (arena e torri) |
| `OldClash1,1.py`, `OldClash1,2.py`, `TheOrigins.py` | Versioni precedenti tenute come riferimento |

---

## Problemi noti e idee future

- `CanvasManager` concentra troppe responsabilità e va spezzato in moduli più piccoli.
- Ogni truppa crea molte chiamate `canvas.after`, che a lungo andare fanno rallentare il gioco.
- L'IA avversaria (`EnemyAI.py`) è solo un'impostazione di base: non c'è ancora un avversario che gioca da solo.
- L'editor del mazzo elenca anche carte non ancora implementate (arciere, gigante, strega, ecc.), che non hanno statistiche né sprite.
- `PathFinder` prova prima la cartella corrente, lo script, Desktop e Documenti; solo dopo scansiona i dischi Windows (`C:` – `F:`). Conviene lanciare il gioco dalla cartella `project_CR 1.3` per evitare scansioni lente.
- La 1.4 dovrebbe risolvere i punti sopra.

---

## Crediti

**Programmatori**

- ZhenTing Lei
- Giovanni De Sabbata

**Aiuti e supporto:** Copi_lot

**Diritti del gioco originale:** Supercell, <https://supercell.com/en/>

Grazie per aver giocato! ❤️
