# 30gunde uygulamasının içeriğini bu repoya aktarır: müfredat, gün gün anlatımlar (MD + JSON).
#   MVP=/yol/mvp python3 araclar/disa-aktar.py
# Kaynak: <MVP>/content/lessons.json (Python, TR) ve <MVP>/content/js/lessons.json (JavaScript)
import json, os, re, shutil
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MVP = Path(os.environ.get("MVP", "/home/claude/mvp"))

COURSES = {
    "python": {
        "src": MVP / "content/lessons.json", "name": "30 Günde Python", "mascot": "Piko", "lang": "python",
        "default_track": ("oyun", "Piko'nun Macerası"),
        "region_img": "gorseller/python/harita/{id}.webp",
    },
    "javascript": {
        "src": MVP / "content/js/lessons.json", "name": "30 Günde JavaScript", "mascot": "Kodi", "lang": "js",
        "default_track": ("js-oyun", "Yıldız Avcısı"),
        "region_img": "gorseller/javascript/bolgeler/{id}.webp",
    },
}


def fence(code, lang):
    code = (code or "").rstrip("\n")
    ticks = "```"
    while ticks in code:
        ticks += "`"
    return f"{ticks}{lang}\n{code}\n{ticks}"


def item_md(it, lang, level="###", label=""):
    out = [f"{level} {label}{it['title']}", "", it["prompt"].strip(), ""]
    if it.get("mode") == "page":
        out += ["**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):", "", fence(it.get("html", ""), "html"), ""]
        if it.get("css"):
            out += ["**CSS:**", "", fence(it["css"], "css"), ""]
    out += ["**Başlangıç kodu:**", "", fence(it["starter"], lang), ""]
    if it.get("hints"):
        out += ["**İpuçları:**", ""] + [f"{i + 1}. {h}" for i, h in enumerate(it["hints"])] + [""]
    out += ["<details><summary>Çözüm</summary>", "", fence(it["solution"], lang), "", "</details>", ""]
    return out


def lesson_md(c, l, regions, tracks):
    lang = c["lang"]
    reg = next((r for r in regions if r["id"] == l["region"]), {"name": l["region"]})
    out = [f"# Gün {l['day']}: {l['title']}", "",
           f"**Kurs:** {c['name']}  ·  **Bölge:** {reg['name']}  ·  **Maskot:** {c['mascot']}", "",
           f"**Bugünün hedefi:** {l['objective']}", "",
           f"> {l['story']}", "",
           f"![{reg['name']}](../../{c['region_img'].format(id=l['region'])})", "", "## Konu anlatımı", ""]
    for s in l["sections"]:
        out += [f"### {s['title']}", "", s["body"].strip(), ""]
    if l.get("examples"):
        out += ["## Örnekler", ""]
        for e in l["examples"]:
            out += [f"### {e['title']}", ""]
            if e.get("mode") == "page":
                out += ["Sayfa:", "", fence(e.get("html", ""), "html"), ""]
            out += [fence(e["code"], lang), ""]
            if e.get("note"):
                out += [f"*{e['note']}*", ""]
    out += ["## Görevler", ""]
    for i, t in enumerate(l["tasks"]):
        out += item_md(t, lang, "###", f"Görev {i + 1}: ")
    if l.get("visual_task"):
        out += item_md(l["visual_task"], lang, "###", "Sahne görevi: ")
    if l.get("challenge"):
        out += item_md(l["challenge"], lang, "##", "Challenge: ")
    dflt_id, dflt_name = c["default_track"]
    out += ["## Proje adımları", "", f"Bugünün katkısı ({dflt_name}): **{l.get('project_contribution', '')}**", ""]
    out += item_md(l["project_task"], lang, "###", f"{dflt_name}: ")
    for tid, t in (l.get("tracks") or {}).items():
        name = tracks.get(tid, {}).get("name", tid)
        out += item_md(t["project_task"], lang, "###", f"{name}: ")
    return "\n".join(out).rstrip() + "\n"


def curriculum_md(c, data):
    regions, tracks = data["regions"], data["tracks"]
    out = [f"# {c['name']}: müfredat", "",
           f"30 gün, {len(regions)} bölge. Maskot: **{c['mascot']}**. Her gün: kısa anlatım, çalıştırılabilir örnekler, "
           "3 görev, isteğe bağlı challenge ve seçilen projeye bir adım.", "", "## Proje yolları", ""]
    dflt_id, dflt_name = c["default_track"]
    out += [f"- **{dflt_name}** (varsayılan)"]
    for tid, t in tracks.items():
        if tid == dflt_id:
            continue
        out += [f"- **{t.get('name', tid)}** ({t.get('kind', '')}): {t.get('desc', '')}"]
    out += ["", "## Günler", ""]
    for r in regions:
        out += [f"### {r['name']} (Gün {r['days'][0]}–{r['days'][-1]})", "",
                f"![{r['name']}](../{c['region_img'].format(id=r['id'])})", "",
                "| Gün | Konu | Hedef | Proje katkısı |", "|---|---|---|---|"]
        for l in data["lessons"]:
            if l["day"] in r["days"]:
                out += [f"| [{l['day']}](gunler/gun-{l['day']:02d}.md) | {l['title']} | {l.get('objective', '').replace('|', '/')} | {l.get('project_contribution', '')} |"]
        out += [""]
    return "\n".join(out)


for key, c in COURSES.items():
    data = json.loads(c["src"].read_text("utf8"))
    base = REPO / key
    for sub in ("gunler", "veri"):
        d = base / sub
        if d.exists():
            shutil.rmtree(d)
        d.mkdir(parents=True)
    (base / "mufredat.md").write_text(curriculum_md(c, data), "utf8")
    meta = {k: v for k, v in data.items() if k != "lessons"}
    meta.update(course=key, name=c["name"], mascot=c["mascot"])
    (base / "veri" / "kurs.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), "utf8")
    for l in data["lessons"]:
        n = f"gun-{l['day']:02d}"
        (base / "gunler" / f"{n}.md").write_text(lesson_md(c, l, data["regions"], data["tracks"]), "utf8")
        (base / "veri" / f"{n}.json").write_text(json.dumps(l, ensure_ascii=False, indent=1), "utf8")
    print(key, len(data["lessons"]), "gün aktarıldı")
