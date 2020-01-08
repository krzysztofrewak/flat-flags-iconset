import base64
import json
import hashlib

styles = "i.flat.flag { width: 18px; height: 12px; display: inline-block; background-size: 100% 100%; background-repeat: no-repeat; }"

styles += "i.large.flat.flag, .large.flat.flags > i.flat.flag { width: 36px; height: 24px; }"
styles += "i.huge.flat.flag, .huge.flat.flags > i.flat.flag { width: 54px; height: 36px; }"
styles += "i.giant.flat.flag, .giant.flat.flags > i.flat.flag { width: 72px; height: 48px; }"

with open("resources.json") as file:
	data = json.load(file)

	for country in data["countries"]:
		styles += ", ".join(map(lambda x: "i.flat.flag." + x.replace(" ", "."), country["classes"])) + " { background-image:url('./flags/" + country["flag"] + ".png'); } "

content = styles.replace(" ", "")

file = open("style.css", "w")
file.write(content)
file.close()
print("File style.css has been updated.")

sri = hashlib.sha384()
sri.update(content.encode("utf-8"))
sri = "sha384-" + base64.b64encode(sri.digest()).decode()
print("Integrity hash: " + sri)

readme = open("readme.md", "w")

with open("readme/about.md") as section:
	readme.write(section.read())

with open("readme/usage.md") as section:
	readme.write(section.read().replace("SHA384_INTEGRITY_HASH", sri))

with open("readme/development.md") as section:
	readme.write(section.read())

with open("readme/index.md") as section:
	readme.write(section.read())
	index = ""
	for c in data["countries"]:
		template = "| ![{} icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/{}.png) | {} | {} | {} |\n"
		index += template.format(c["flag"], c["flag"], c["name"], c["iso"], ", ".join(map(lambda x: "`" + x + "`", c["classes"])))
	readme.write(index)

readme.close()
print("File readme2.md has been updated.")