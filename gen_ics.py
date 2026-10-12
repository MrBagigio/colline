# Genera i file .ics per il calendario. Da rilanciare se cambiano data o mete.
BACKSLASH_N = chr(92) + "n"          # la sequenza letterale che vuole il formato iCal

mete = [
    ("vr-alto", "Verona dall'alto", "Giardino Giusti, Verona",
     "Giardino Giusti, cicchetti in Sottoriva, tramonto a Castel San Pietro (18:35) e aperitivo in Veronetta."),
    ("vr-romana", "Verona romana", "Arena di Verona, Piazza Bra",
     "Dentro l'Arena, pranzo in osteria, Ponte Pietra al tramonto e spritz sotto Porta Borsari."),
    ("vr-fiume", "Verona sul fiume", "Basilica di San Zeno, Verona",
     "San Zeno, pranzo e lungadige, tramonto sul ponte di Castelvecchio e aperitivo sul Corso."),
    ("vr-piazze", "Piazze e torre", "Piazza delle Erbe, Verona",
     "Torre dei Lamberti, pranzo in Veronetta, spritz in Piazza delle Erbe."),
]

for slug, nome, luogo, desc in mete:
    righe = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//colline//invito//IT",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "BEGIN:VEVENT",
        "UID:" + slug + "-20261014@colline",
        "DTSTAMP:20261012T120000Z",
        "DTSTART:20261014T080000Z",      # 10:00 ora italiana (ora legale fino al 25/10)
        "DTEND:20261014T190000Z",        # 21:00 ora italiana
        "SUMMARY:Una giornata fuori - " + nome,
        "LOCATION:" + luogo,
        "DESCRIPTION:" + desc + BACKSLASH_N +
        "Art. 5 del contratto: partenza in mattinata, rientro per cena, con facolta' di prolungare.",
        "BEGIN:VALARM",
        "TRIGGER:-PT2H",
        "ACTION:DISPLAY",
        "DESCRIPTION:Fra due ore si parte",
        "END:VALARM",
        "END:VEVENT",
        "END:VCALENDAR",
        "",
    ]
    testo = "\r\n".join(righe)
    with open("ics/" + slug + ".ics", "w", encoding="utf-8", newline="") as f:
        f.write(testo)
    # nessuna riga deve contenere a capo veri
    assert BACKSLASH_N in testo
    print(slug + ".ics", len(testo.encode("utf-8")), "byte")
