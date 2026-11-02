// Galatry 3 · table des matières à gauche, commune à toutes les pages de l'artifact.
// Injectée par build.py ; les liens sont relatifs, préfixés comme le src de ce script.
(function () {
  var PAGES = [
    { href: "plans.html", label: "Actuel – Plans et 3D" },   // today's house: plans and 3D model of the existing villa, always first (user)
    { href: "index.html", label: "Projet – Plans et 3D" },   // the artifact's own page (build.py publishes projet.html as index.html)
    { href: "archi.html", label: "Plans d’architecte" },   // A3 sheets of the base project to SIA 400 conventions (archi_plans.py)
    { href: "interieur.html", label: "Intérieur 3D" },   // full-screen 3D page from galatry-interior/: keeps its own Sommaire, no toc.js
    { href: "travaux.html", label: "Travaux par étapes" },   // from etapes/: keeps its own sommaire, no toc.js
    { href: "cfc.html", label: "Devis CFC" },   // the base's costs by CFC position (cfc.py)
    { href: "illustrations.html", label: "Illustrations" },
    { href: "photos.html", label: "Photos de l’annonce" }
  ];
  // the other Galatry 3 artifacts, opened in a new tab
  var OTHER = [
    { url: "https://lobinggeli.github.io/projects/galatry/", label: "Site public à partager" },   // the GitHub copy of this artifact (public_sync.py)
    { url: "https://claude.ai/artifact/72yV95DrnY97G4iceXXBTu", label: "À deux · achat et financement" }
  ];

  var me = document.currentScript;
  var prefix = me ? (me.getAttribute("src") || "").replace(/toc\.js.*$/, "") : "";
  var here = location.pathname.replace(/\/$/, "/index.html");

  function isCurrent(p) {
    return here.slice(-p.href.length) === p.href &&
      (here.length === p.href.length || here.charAt(here.length - p.href.length - 1) === "/");
  }
  function cur(p) {
    return isCurrent(p);
  }

  var css = "" +
    ".gtoc{position:fixed;top:0;left:0;bottom:0;width:236px;z-index:900;overflow-y:auto;" +
    "background:var(--sheet,#FBFCFB);border-right:1px solid var(--rule,#C9D1D4);padding:24px 14px 32px;" +
    "font:14px/1.4 var(--f-body,system-ui,sans-serif);color:var(--ink,#1B2530)}" +
    ".gtoc .gtoc-k{font-family:var(--f-draw,'Arial Narrow',sans-serif);text-transform:uppercase;letter-spacing:.14em;" +
    "font-size:12px;color:var(--accent,#2F6690);margin:0 8px 4px}" +
    ".gtoc .gtoc-t{font-family:var(--f-draw,'Arial Narrow',sans-serif);font-weight:600;font-size:20px;margin:0 8px 18px;line-height:1.1}" +
    ".gtoc ol{list-style:none;margin:0;padding:0;display:block}.gtoc li{margin:0;padding:0}" +
    ".gtoc a{display:block;border:0;background:none;text-transform:none;letter-spacing:0;font-size:inherit;font-family:inherit;color:inherit;text-decoration:none;padding:6px 8px;border-radius:3px;border-left:2px solid transparent}" +
    ".gtoc a:hover,.gtoc a:focus-visible{background:var(--room,#E6ECEE);outline:none}" +
    ".gtoc .gtoc-p>a{font-family:var(--f-draw,'Arial Narrow',sans-serif);text-transform:uppercase;letter-spacing:.07em;font-size:14px;font-weight:600}" +
    ".gtoc .gtoc-p{margin-bottom:2px}" +
    ".gtoc .gtoc-p.is-cur>a{color:var(--accent,#2F6690)}" +
    ".gtoc .gtoc-sub{margin:2px 0 8px 8px;border-left:1px solid var(--rule,#C9D1D4)}" +
    ".gtoc .gtoc-sub a{font-size:13.5px;color:var(--ink-2,#56626E);padding:4px 10px;border-radius:0 3px 3px 0;margin-left:-1px}" +
    ".gtoc .gtoc-sub a.is-on{color:var(--ink,#1B2530);border-left-color:var(--accent,#2F6690);font-weight:500}" +
    ".gtoc .gtoc-k2{margin:0 8px 4px;font-size:11px;color:var(--ink-2,#56626E)}" +
    ".gtoc .gtoc-ext{margin:0 0 16px;padding-bottom:12px;border-bottom:1px solid var(--rule,#C9D1D4)}" +
    ".gtoc .gtoc-ext a{color:var(--accent,#2F6690);font-size:13.5px;padding:4px 8px}" +
    ".gtoc-btn{display:none}" +
    "@media (min-width:1100px){body.has-gtoc{padding-left:268px!important}}" +
    "@media (max-width:1099px){" +
    ".gtoc{transform:translateX(-100%);transition:transform .2s ease;box-shadow:none;width:min(280px,84vw)}" +
    ".gtoc.open{transform:none;box-shadow:0 0 0 100vmax rgba(0,0,0,.35)}" +
    ".gtoc-btn{display:flex;align-items:center;gap:8px;position:fixed;left:12px;bottom:12px;z-index:901;" +
    "font:600 13px/1 var(--f-draw,'Arial Narrow',sans-serif);text-transform:uppercase;letter-spacing:.08em;" +
    "background:var(--ink,#1B2530);color:var(--paper,#F3F5F4);border:0;border-radius:3px;padding:11px 14px;cursor:pointer}" +
    ".gtoc.open+.gtoc-btn{left:auto;right:12px}}" +
    "@media print{.gtoc,.gtoc-btn{display:none}body.has-gtoc{padding-left:0!important}}";

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text) e.textContent = text;
    return e;
  }

  function sections() {
    var out = [];
    document.querySelectorAll("section[id]").forEach(function (s) {
      var h = s.querySelector(":scope > .sec-head h2, :scope > h2");
      if (h && h.textContent.trim()) out.push({ id: s.id, label: h.textContent.trim(), node: s });
    });
    return out;
  }

  function build() {
    var style = el("style");
    style.textContent = css;
    document.head.appendChild(style);

    var nav = el("aside", "gtoc");
    nav.setAttribute("role", "navigation");
    nav.setAttribute("aria-label", "Table des matières");
    nav.appendChild(el("div", "gtoc-k", "Corseaux VD"));
    nav.appendChild(el("div", "gtoc-t", "Galatry 3"));
    nav.appendChild(el("div", "gtoc-k gtoc-k2", "Autres pages"));
    var ext = el("ol", "gtoc-ext");
    OTHER.forEach(function (o) {
      var li = el("li"), a = el("a", null, o.label + " ↗");
      a.href = o.url; a.target = "_blank"; a.rel = "noopener";
      li.appendChild(a); ext.appendChild(li);
    });
    nav.appendChild(ext);

    var secs = sections();
    var links = {};
    var list = el("ol");

    function addPage(p, parent) {
      var li = el("li", "gtoc-p");
      var a = el("a", null, p.label);
      a.setAttribute("href", prefix + p.href);
      li.appendChild(a);
      if (cur(p)) {
        li.classList.add("is-cur");
        a.setAttribute("aria-current", "page");
        if (secs.length) {
          var sub = el("ol", "gtoc-sub");
          secs.forEach(function (s) {
            var sl = el("a", null, s.label);
            sl.href = "#" + s.id;
            links[s.id] = sl;
            var sli = el("li");
            sli.appendChild(sl);
            sub.appendChild(sli);
          });
          li.appendChild(sub);
        }
      }
      parent.appendChild(li);
      if (p.children) {
        var kids = el("ol", "gtoc-sub");
        p.children.forEach(function (c) { addPage(c, kids); });
        li.appendChild(kids);
      }
    }
    PAGES.forEach(function (p) { addPage(p, list); });
    nav.appendChild(list);

    var btn = el("button", "gtoc-btn", "☰ Sommaire");
    btn.type = "button";
    btn.setAttribute("aria-expanded", "false");
    function toggle(open) {
      nav.classList.toggle("open", open);
      btn.setAttribute("aria-expanded", String(open));
      btn.textContent = open ? "✕ Fermer" : "☰ Sommaire";
    }
    btn.addEventListener("click", function () { toggle(!nav.classList.contains("open")); });
    nav.addEventListener("click", function (e) { if (e.target.tagName === "A") toggle(false); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") toggle(false); });
    document.addEventListener("click", function (e) {
      if (nav.classList.contains("open") && !nav.contains(e.target) && e.target !== btn) toggle(false);
    });

    document.body.prepend(btn);
    document.body.prepend(nav);
    document.body.classList.add("has-gtoc");

    if (secs.length && "IntersectionObserver" in window) {
      var visible = {};
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) { visible[en.target.id] = en.isIntersecting; });
        var on = null;
        for (var i = 0; i < secs.length; i++) if (visible[secs[i].id]) { on = secs[i].id; break; }
        if (!on) return;
        Object.keys(links).forEach(function (id) { links[id].classList.toggle("is-on", id === on); });
      }, { rootMargin: "-10% 0px -55% 0px" });
      secs.forEach(function (s) { io.observe(s.node); });
    }
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", build);
  else build();
})();
