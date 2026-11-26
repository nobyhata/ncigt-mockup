#!/bin/sh
# Rebuild the whole site: designed pages, carried-over pages, section pages, menus.
set -e
cd "$(dirname "$0")/.."
rm -rf /home/claude/ncigt /home/claude/build /home/claude/site
mkdir -p /home/claude/ncigt /home/claude/build /home/claude/site
cp -r design /home/claude/ncigt/project
(cd /home/claude/ncigt/project && python3 make_people.py >/dev/null && python3 render.py >/dev/null)
cp /home/claude/site/*.html .
python3 design/restyle.py
python3 design/build_landing.py
python3 design/build_sections.py
python3 design/megamenu.py *.html
