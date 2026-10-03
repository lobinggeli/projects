#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translation script for baby development timeline
Translates remaining English content to French
"""

import re

# Translation dictionary for common terms and phrases
translations = {
    # Months
    "Month 5": "Mois 5",
    "Month 6": "Mois 6",
    "Month 7": "Mois 7",
    "Month 8": "Mois 8",
    "Month 9": "Mois 9",
    "Month 10": "Mois 10",
    "Month 11": "Mois 11",
    "Month 12": "Mois 12",

    # Month names
    " Apr ": " avr ",
    " May ": " mai ",
    " Jun ": " jun ",
    " Jul ": " jul ",
    " Aug ": " aoû ",
    " Sep ": " sep ",
    " Oct ": " oct ",
    " Nov ": " nov ",

    # Common sections
    "<strong>Type:</strong>": "<strong>Type :</strong>",
    "<strong>Frequency:</strong>": "<strong>Fréquence :</strong>",
    "<strong>Amount per feed:</strong>": "<strong>Quantité par tétée :</strong>",
    "<strong>Daily total:</strong>": "<strong>Total quotidien :</strong>",
    "<strong>Breastfeeding tip:</strong>": "<strong>Conseil allaitement :</strong>",
    "<strong>Formula tip:</strong>": "<strong>Conseil préparation :</strong>",
    "<strong>Timing:</strong>": "<strong>Moment :</strong>",
    "<strong>Signs to watch for:</strong>": "<strong>Signes à surveiller :</strong>",
    "<strong>How to handle:</strong>": "<strong>Comment gérer :</strong>",
    "<strong>What to expect after:</strong>": "<strong>À quoi s'attendre après :</strong>",
    "<strong>Status:</strong>": "<strong>Statut :</strong>",
    "<strong>Timeline:</strong>": "<strong>Calendrier :</strong>",
    "<strong>Teeth count:</strong>": "<strong>Nombre de dents :</strong>",
    "<strong>Signs of teething:</strong>": "<strong>Signes de dentition :</strong>",
    "<strong>Safe remedies:</strong>": "<strong>Remèdes sûrs :</strong>",

    # Common phrases
    "Breast milk or formula": "Lait maternel ou préparation",
    "No screens": "Pas d'écrans",
    "Tummy time": "Temps sur le ventre",
    "Sleep": "Sommeil",
    "hours": "heures",
    "per day": "par jour",
    "well-child visit": "visite de contrôle",
    "vaccines": "vaccins",
    "Growth spurt": "Poussée de croissance",
    "Focus:": "Objectif :",

    # Development terms
    "Rolls both ways": "Se retourne dans les deux sens",
    "Sits independently": "S'assoit de manière autonome",
    "Crawls": "Rampe",
    "Stands with support": "Se tient debout avec soutien",
    "Walks independently": "Marche de manière autonome",
    "First words": "Premiers mots",
    "Pincer grasp": "Pince",

    # Time references
    "days": "jours",
    "weeks": "semaines",
    "months": "mois",
}

def translate_file(input_file, output_file=None):
    """Translate the baby timeline file"""
    if output_file is None:
        output_file = input_file

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply translations
    for english, french in translations.items():
        content = content.replace(english, french)

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Translation complete. Output written to: {output_file}")

if __name__ == "__main__":
    translate_file("/Users/loicbinggeli/Github/MASTER/baby-development-timeline-fr.html")
