import json
import hashlib

styles = "i.flat.flag { width: 18px; height: 12px; display: inline-block; background-size: 100% 100%; background-repeat: no-repeat; }"

styles += "i.large.flat.flag, .large.flat.flags > i.flat.flag { width: 36px; height: 24px; }"
styles += "i.huge.flat.flag, .huge.flat.flags > i.flat.flag { width: 54px; height: 36px; }"
styles += "i.giant.flat.flag, .giant.flat.flags > i.flat.flag { width: 72px; height: 48px; }"

with open("resources.json") as file:
	data = json.load(file)

	for resource in data["flags"]:
		styles += ", ".join(map(lambda x: "i.flat.flag." + x.replace(" ", "."), resource["classes"])) + " { background-image:url('./flags/" + resource["flag"] + ".png'); } "

content = styles.replace(" ", "")

file = open("style.css", "w")
file.write(content)
file.close()

sri = hashlib.sha384()
sri.update(content.encode('utf-8'))
sri = base64.b64encode(sri.digest()).decode()

print("Integrity hash: sha384-" + sri)