<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:06b6d4&height=180&section=header&text=CSV+Joiner&fontSize=46&fontColor=ffffff&animation=fadeIn&fontAlignY=35" width="100%" alt="CSV Joiner banner"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=900&color=06b6d4&center=true&vCenter=true&width=760&lines=Join+CSV+datasets+by+key+and+inspect+unmatched+rows" alt="Typing title"/>
</p>
<p align="center">
<img src="https://img.shields.io/github/license/CyberLoop-dev/csv-joiner?style=for-the-badge" alt="License"/>
<img src="https://img.shields.io/github/languages/top/CyberLoop-dev/csv-joiner?style=for-the-badge" alt="Language"/>
<img src="https://img.shields.io/github/stars/CyberLoop-dev/csv-joiner?style=for-the-badge" alt="Stars"/>
<img src="https://img.shields.io/github/last-commit/CyberLoop-dev/csv-joiner?style=for-the-badge" alt="Last commit"/>
</p>
<p align="center"><img src="assets/overview.svg" width="640" alt="CSV Joiner illustration"/></p>

## 🧭 Overview
CSV Joiner is a small Python CLI for combining two tabular exports without opening a spreadsheet. It preserves duplicate-key matches, prefixes non-key columns to avoid collisions, and supports left, inner, and full joins.

## ✨ Features
- 🔗 Join two CSV files using a chosen key column
- 🧮 Preserve one-to-many and many-to-many key matches
- 🧾 Choose left, inner, or full join behavior
- 🧭 Keep unmatched rows visible instead of silently dropping them
- 📤 Write a clean output CSV with collision-safe column names

## 🎬 Demo
~~~bash
python main.py customers.csv orders.csv --key customer_id --how left --output joined.csv
~~~
The output keeps unmatched customer rows and leaves their order columns empty.

## 🚀 Quick Start
Requires Python 3.10+. No third-party packages are required.
~~~bash
python main.py left.csv right.csv --key id --how full --output merged.csv
python -m unittest discover -s tests
~~~

## 🧰 Tech Stack
- 🐍 Python standard library
- 📄 csv and argparse
- 🧪 unittest

## 🗂️ Folder Structure
~~~text
csv-joiner/
├── assets/overview.svg
├── tests/test_main.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
~~~

## 🗺️ Roadmap
- [ ] 📊 Add summary counts for matched and unmatched rows
- [ ] 🧩 Support joining more than two files
- [ ] 🧪 Add optional type-aware key normalization

## 🤝 Contributing
Bug reports and focused pull requests are welcome. Include a reproducible example or a test when changing behavior.

## 📄 License
MIT — see [LICENSE](LICENSE).

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:06b6d4&height=110&section=footer" width="100%" alt="Animated wave footer"/></p>