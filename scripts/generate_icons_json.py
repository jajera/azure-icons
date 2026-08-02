#!/usr/bin/env python3
"""Generate icons.json from the organized Azure Architecture Icons SVG library."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ICONS_DIR = ROOT / "icons"
OUTPUT = ROOT / "icons.json"

AZURE_BLUE = "#0078D4"

CATEGORY_NAMES = {
    "ai-machine-learning": "AI + Machine Learning",
    "analytics": "Analytics",
    "app-services": "App Services",
    "azure-ecosystem": "Azure Ecosystem",
    "blockchain": "Blockchain",
    "compute": "Compute",
    "containers": "Containers",
    "databases": "Databases",
    "developer-tools": "Developer Tools",
    "devops": "DevOps",
    "general": "General",
    "hybrid-multicloud": "Hybrid + Multicloud",
    "identity": "Identity",
    "integration": "Integration",
    "intune": "Intune",
    "iot": "IoT",
    "management-governance": "Management + Governance",
    "menu": "Menu",
    "migrate": "Migrate",
    "mixed-reality": "Mixed Reality",
    "monitor": "Monitor",
    "networking": "Networking",
    "new-icons": "New Icons",
    "other": "Other",
    "security": "Security",
    "storage": "Storage",
    "web": "Web",
}

TOKEN_NAMES = {
    "ai": "AI",
    "aks": "AKS",
    "api": "API",
    "apis": "APIs",
    "cdn": "CDN",
    "ci": "CI",
    "db": "DB",
    "dns": "DNS",
    "gpu": "GPU",
    "hsm": "HSM",
    "http": "HTTP",
    "https": "HTTPS",
    "iot": "IoT",
    "ip": "IP",
    "sql": "SQL",
    "ssh": "SSH",
    "ssl": "SSL",
    "tls": "TLS",
    "vm": "VM",
    "vms": "VMs",
    "vnet": "VNet",
    "vpn": "VPN",
}

EXTRA_TAGS = {
    "kubernetes-services": ["aks", "k8s", "kubernetes"],
    "aks-automatic": ["aks", "kubernetes"],
    "container-registries": ["acr", "registry"],
    "function-apps": ["functions", "serverless"],
    "app-services": ["webapp", "app-service"],
    "virtual-networks": ["vnet", "network"],
    "load-balancers": ["lb"],
    "application-gateways": ["appgw", "waf"],
    "front-door-and-cdn-profiles": ["afd", "cdn", "front-door"],
    "key-vaults": ["secrets", "certificates"],
    "storage-accounts": ["blob", "storage"],
    "sql-database": ["mssql", "database"],
    "azure-cosmos-db": ["cosmos", "nosql"],
    "event-hubs": ["streaming", "messaging"],
    "azure-service-bus": ["messaging", "queue"],
    "api-management-services": ["apim", "gateway"],
}


def humanize(slug: str) -> str:
    words = []
    for word in slug.split("-"):
        words.append(TOKEN_NAMES.get(word, word.capitalize()))
    return " ".join(words)


def tags_for(category: str, slug: str, fullname: str) -> list[str]:
    # Category + curated abbreviations only. Search still matches name/fullname.
    tags = {category}
    tags.update(EXTRA_TAGS.get(slug, []))
    return sorted(tags)


def description_for(category_label: str, fullname: str) -> str:
    return f"{fullname} Azure architecture icon ({category_label})."


def build_entries() -> list[dict[str, object]]:
    entries: list[dict[str, object]] = []
    for svg_path in sorted(ICONS_DIR.glob("*/*.svg")):
        relative = svg_path.relative_to(ROOT)
        category = relative.parts[1]
        slug = svg_path.stem
        category_label = CATEGORY_NAMES.get(category, humanize(category))
        fullname = humanize(slug)
        entries.append(
            {
                "path": relative.as_posix(),
                "tags": tags_for(category, slug, fullname),
                "category": category,
                "color": AZURE_BLUE,
                "description": description_for(category_label, fullname),
                "fullname": fullname,
                "name": slug,
            }
        )

    entries.sort(
        key=lambda icon: (
            str(icon["category"]).casefold(),
            str(icon["fullname"]).casefold(),
            str(icon["path"]),
        )
    )
    return entries


def main() -> None:
    entries = build_entries()
    if not entries:
        raise SystemExit(f"No SVG icons found under {ICONS_DIR}")

    OUTPUT.write_text(
        json.dumps(entries, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(entries)} icons to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
