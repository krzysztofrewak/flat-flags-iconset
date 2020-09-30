# About
This package is a simple semantic wrapper for Muharrem Senyil & Flatstudio's [Flat Flags](https://dribbble.com/shots/4028772-Freebies-Flat-Flags-227) icon set.
## Usage
Use CDN to add stylesheet into your head section (using one with integrity hash could be a good practice):
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/krzysztofrewak/flat-flags-iconset@latest/style.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/krzysztofrewak/flat-flags-iconset@latest/style.css" integrity="sha384-typL+psvFGLzSJiF9ka5WmyYwYhYltLSIOJoXOf+ey7UKwkijRwY6YQIGqwOW2Io" crossorigin="anonymous">
```

Now you can insert a flag via country's [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) code combined with `flat flag` CSS class:
```html
<i class="is flat flag"></i>
<i class="md flat flag"></i>
```

Simple country names (and some abbreviations) are working too:
```html
<i class="tunisia flat flag"></i>
<i class="uae flat flag"></i>
```

You can add resizing classes `large`, `huge` and `giant` to receive bigger images. It's working also with container tagged `flat flags`:
```html
<i class="giant cyprus flat flag"></i>

<div class="huge flat flags">
    <i class="australia flat flag"></i>
    <i class="new zealand flat flag"></i>
</div>
```
## For developers
You can rebuild `style.css` (and `readme.md`) from `resources.json` via Python script in Docker container:
```sh
docker-compose run -w /application python python builder.py
```
## Flag index
| flag | country | ISO | available selectors |
| --- | --- | --- | --- |
| ![ad icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ad.png) | Andorra | AD | `ad`, `andorra` |
| ![ae icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ae.png) | United Arab Emirates | AE | `ae`, `united arab emirates`, `uae` |
| ![af icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/af.png) | Afghanistan | AF | `af`, `afghanistan` |
| ![ag icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ag.png) | Antigua and Barbuda | AG | `ag`, `antigua`, `barbuda` |
| ![ai icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ai.png) | Anguilla | AI | `ai`, `anguilla` |
| ![al icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/al.png) | Albania | AL | `al`, `albania` |
| ![am icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/am.png) | Armenia | AM | `am`, `armenia` |
| ![ao icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ao.png) | Angola | AO | `ao`, `angola` |
| ![aq icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/aq.png) | Antarctica | AQ | `aq`, `antarctica` |
| ![ar icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ar.png) | Argentina | AR | `ar`, `argentina` |
| ![as icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/as.png) | American Samoa | AS | `as`, `american samoa` |
| ![at icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/at.png) | Austria | AT | `at`, `austria` |
| ![au icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/au.png) | Australia | AU | `au`, `australia` |
| ![aw icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/aw.png) | Aruba | AW | `aw`, `aruba` |
| ![az icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/az.png) | Azerbaijan | AZ | `az`, `azerbaijan` |
| ![ax icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ax.png) | Åland Islands | AX | `ax`, `aland islands`, `aland` |
| ![ba icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ba.png) | Bosnia and Herzegovina | BA | `ba`, `bosnia`, `herzegovina` |
| ![bb icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/bb.png) | Barbados | BB | `bb`, `barbados` |
| ![bd icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/bd.png) | Bangladesh | BD | `bd`, `bangladesh` |
| ![be icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/be.png) | Belgium | BE | `be`, `belgium` |
| ![bf icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/bf.png) | Burkina Faso | BF | `bf`, `burkina faso` |
| ![bg icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/bg.png) | Bulgaria | BG | `bg`, `bulgaria` |
| ![bh icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/bh.png) | Bahrain | BH | `bh`, `bahrain` |
| ![bi icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/bi.png) | Burundi | BI | `bi`, `burundi` |
| ![bj icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/bj.png) | Benin | BJ | `bj`, `benin` |
| ![bl icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/bl.png) | Saint Barthélemy | BL | `bl`, `saint barthelemy` |
| ![bm icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/bm.png) | Bermuda | BM | `bm`, `bermuda` |
| ![bn icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/bn.png) | Brunei | BN | `bn`, `brunei` |
| ![bo icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/bo.png) | Bolivia | BO | `bo`, `bolivia` |
| ![bq icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/bq.png) | Caribbean Netherlands | bq | `bq`, `caribbean netherlands`, `bonaire`, `sint eustatius`, `saba` |
| ![br icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/br.png) | Brazil | BR | `br`, `brazil` |
| ![bs icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/bs.png) | Bahamas | BS | `bs`, `bahamas` |
| ![bt icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/bt.png) | Bhutan | BT | `bt`, `bhutan` |
| ![bv icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/bv.png) | Bouvet Island | BV | `bv`, `bouvet island` |
| ![bw icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/bw.png) | Botswana | BW | `bw`, `botswana` |
| ![by icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/by.png) | Belarus | BY | `by`, `belarus` |
| ![bz icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/bz.png) | Belize | BZ | `bz`, `belize` |
| ![ca icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ca.png) | Canada | CA | `ca`, `canada` |
| ![cc icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/cc.png) | Cocos Islands | CC | `cc`, `cocos islands` |
| ![cd icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/cd.png) | Democratic Republic of the Congo | CD | `cd`, `democratic republic congo`, `dr congo` |
| ![cf icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/cf.png) | Central African Republic | CF | `cf`, `central african republic` |
| ![cg icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/cg.png) | Congo | CG | `cg`, `congo` |
| ![ch icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ch.png) | Switzerland | CH | `ch`, `switzerland` |
| ![ci icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ci.png) | Ivory Coast | CI | `ci`, `ivory coast` |
| ![ck icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ck.png) | Cook Islands | CK | `ck`, `cook islands` |
| ![cl icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/cl.png) | Chile | CL | `cl`, `chile` |
| ![cm icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/cm.png) | Cameroon | CM | `cm`, `cameroon` |
| ![cn icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/cn.png) | China | CN | `cn`, `china` |
| ![co icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/co.png) | Colombia | CO | `co`, `colombia` |
| ![cr icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/cr.png) | Costa Rica | CR | `cr`, `costa rica` |
| ![cu icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/cu.png) | Cuba | CU | `cu`, `cuba` |
| ![cv icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/cv.png) | Cape Verde | CV | `cv`, `cabo verde`, `cape varde` |
| ![cw icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/cw.png) | Curaçao | CW | `cw`, `curacao` |
| ![cx icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/cx.png) | Christmas Island | CX | `cx`, `christmas island` |
| ![cy icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/cy.png) | Cyprus | CY | `cy`, `cyprus` |
| ![cy-tr icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/cy-tr.png) | Northern Cyprus | - | `cy tr`, `northern cyprus` |
| ![cz icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/cz.png) | Czechia | CZ | `cz`, `czechia`, `czech republic` |
| ![de icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/de.png) | Germany | DE | `de`, `germany` |
| ![dj icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/dj.png) | Djibouti | DJ | `dj`, `djibouti` |
| ![dk icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/dk.png) | Denmark | DK | `dk`, `denmark` |
| ![dm icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/dm.png) | Dominica | DM | `dm`, `dominica` |
| ![do icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/do.png) | Dominican Republic | DO | `do`, `dominican republic` |
| ![dz icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/dz.png) | Algeria | DZ | `dz`, `algeria` |
| ![ec icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ec.png) | Ecuador | EC | `ec`, `ecuador` |
| ![ee icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ee.png) | Estonia | EE | `ee`, `estonia` |
| ![eg icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/eg.png) | Egypt | EG | `eg`, `egypt` |
| ![eh icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/eh.png) | Western Sahara | EH | `eh`, `western sahara` |
| ![er icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/er.png) | Eritrea | ER | `er`, `eritrea` |
| ![es icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/es.png) | Spain | ES | `es`, `spain` |
| ![et icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/et.png) | Ethiopia | ET | `et`, `ethiopia` |
| ![fi icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/fi.png) | Finland | FI | `fi`, `finland` |
| ![fj icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/fj.png) | Fiji | FJ | `fj`, `fiji` |
| ![fk icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/fk.png) | Falkland Islands | FK | `fk`, `falkland islands` |
| ![fm icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/fm.png) | Federated States of Micronesia | FM | `fm`, `micronesia` |
| ![fo icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/fo.png) | Faroe Islands | FO | `fo`, `faroe islands` |
| ![fr icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/fr.png) | France | FR | `fr`, `france` |
| ![ga icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ga.png) | Gabon | GA | `ga`, `gabon` |
| ![gb icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/gb.png) | Great Britain | GB | `gb`, `great britain`, `united kingdom` |
| ![gb-eng icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/gb-eng.png) | England | GB-ENG | `gb eng`, `england` |
| ![gb-nir icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/gb-nir.png) | Northern Ireland | GB-NIR | `gb nir`, `northern ireland` |
| ![gb-sct icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/gb-sct.png) | Scotland | GB-SCT | `gb sct`, `scotland` |
| ![gb-wls icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/gb-wls.png) | Wales | GB-WLS | `gb wls`, `wales` |
| ![gd icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/gd.png) | Grenada | GD | `gd`, `grenada` |
| ![ge icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ge.png) | Georgia | GE | `ge`, `georgia` |
| ![gf icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/gf.png) | French Guiana | GF | `gf`, `french guiana` |
| ![gg icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/gg.png) | Guernsey | GG | `gg`, `guernsey` |
| ![gh icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/gh.png) | Ghana | GH | `gh`, `ghana` |
| ![gi icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/gi.png) | Gibraltar | GI | `gi`, `gibraltar` |
| ![gl icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/gl.png) | Greenland | GL | `gl`, `greenland` |
| ![gm icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/gm.png) | Gambia | GM | `gm`, `gambia` |
| ![gn icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/gn.png) | Guinea | GN | `gn`, `guinea` |
| ![gp icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/gp.png) | Guadeloupe | GP | `gp`, `guadeloupe` |
| ![gq icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/gq.png) | Equatorial Guinea | GQ | `gq`, `equatorial guinea` |
| ![gr icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/gr.png) | Greece | GR | `gr`, `greece` |
| ![gs icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/gs.png) | South Georgia and the South Sandwich Islands | GS | `gs`, `south georgia`, `sound sandwich` |
| ![gt icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/gt.png) | Guatemala | GT | `gt`, `guatemala` |
| ![gu icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/gu.png) | Guam | GU | `gu`, `guam` |
| ![gw icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/gw.png) | Guinea-Bissau | GW | `gw`, `guinea bissau` |
| ![gy icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/gy.png) | Guyana | GY | `gy`, `guyana` |
| ![hk icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/hk.png) | Hong Kong | HK | `hk`, `hong kong` |
| ![hm icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/hm.png) | Heard Island and McDonald Islands | HM | `hm`, `heard`, `mcdonald` |
| ![hn icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/hn.png) | Honduras | HN | `hn`, `honduras` |
| ![hr icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/hr.png) | Croatia | HR | `hr`, `croatia` |
| ![ht icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ht.png) | Haiti | HT | `ht`, `haiti` |
| ![hu icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/hu.png) | Hungary | HU | `hu`, `hungary` |
| ![id icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/id.png) | Indonesia | ID | `id`, `indonesia` |
| ![ie icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ie.png) | Ireland | IE | `ie`, `ireland` |
| ![il icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/il.png) | Israel | IL | `il`, `israel` |
| ![im icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/im.png) | Isle of Man | IM | `im`, `isle of man`, `man` |
| ![in icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/in.png) | India | IN | `in`, `india` |
| ![io icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/io.png) | British Indian Ocean Territory | IO | `io`, `british indian ocean territory` |
| ![iq icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/iq.png) | Iraq | IQ | `iq`, `iraq` |
| ![ir icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ir.png) | Iran | IR | `ir`, `iran` |
| ![is icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/is.png) | Iceland | IS | `is`, `iceland` |
| ![it icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/it.png) | Italy | IT | `it`, `italy` |
| ![je icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/je.png) | Jersey | JE | `je`, `jersey` |
| ![jm icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/jm.png) | Jamaica | JM | `jm`, `jamaica` |
| ![jo icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/jo.png) | Jordan | JO | `jo`, `jordan` |
| ![jp icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/jp.png) | Japan | JP | `jp`, `japan` |
| ![ke icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ke.png) | Kenya | KE | `ke`, `kenya` |
| ![kg icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/kg.png) | Kyrgyzstan | KG | `kg`, `kyrgyzstan` |
| ![kh icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/kh.png) | Cambodia | KH | `kh`, `cambodia` |
| ![ki icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ki.png) | Kiribati | KI | `ki`, `kiribati` |
| ![km icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/km.png) | Comoros | KM | `km`, `comoros` |
| ![kn icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/kn.png) | Saint Kitts and Nevis | KN | `kn`, `saint kitts`, `nevis` |
| ![kp icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/kp.png) | North Korea | KP | `kp`, `north korea` |
| ![kr icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/kr.png) | South Korea | KR | `kr`, `south korea` |
| ![kw icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/kw.png) | Kuwait | KW | `kw`, `kuwait` |
| ![ky icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ky.png) | Cayman Islands | KY | `ky`, `cayman islands` |
| ![kz icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/kz.png) | Kazakhstan | KZ | `kz`, `kazakhstan` |
| ![la icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/la.png) | Laos | LA | `la`, `laos` |
| ![lb icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/lb.png) | Lebanon | LB | `lb`, `lebanon` |
| ![lc icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/lc.png) | Saint Lucia | LC | `lc`, `saint lucia` |
| ![li icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/li.png) | Liechtenstein | LI | `li`, `liechtenstein` |
| ![lk icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/lk.png) | Sri Lanka | LK | `lk`, `sri lanka` |
| ![lr icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/lr.png) | Liberia | LR | `lr`, `liberia` |
| ![ls icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ls.png) | Lesotho | LS | `ls`, `lesotho` |
| ![lt icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/lt.png) | Lithuania | LT | `lt`, `lithuania` |
| ![lu icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/lu.png) | Luxembourg | LU | `lu`, `luxembourg` |
| ![lv icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/lv.png) | Latvia | LV | `lv`, `latvia` |
| ![ly icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ly.png) | Libya | LY | `ly`, `libya` |
| ![ma icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ma.png) | Morocco | MA | `ma`, `morocco` |
| ![mc icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/mc.png) | Monaco | MC | `mc`, `monaco` |
| ![md icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/md.png) | Moldova | MD | `md`, `moldova` |
| ![me icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/me.png) | Montenegro | ME | `me`, `montenegro` |
| ![mf icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/mf.png) | Saint Martin | mf | `mf`, `saint-martin` |
| ![mg icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/mg.png) | Madagascar | MG | `mg`, `madagascar` |
| ![mh icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/mh.png) | Marshall Islands | MH | `mh`, `marshall islands` |
| ![mk icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/mk.png) | North Macedonia | MK | `mk`, `north macedonia` |
| ![ml icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ml.png) | Mali | ML | `ml`, `mali` |
| ![mm icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/mm.png) | Myanmar | MM | `mm`, `myanmar` |
| ![mn icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/mn.png) | Mongolia | MN | `mn`, `mongolia` |
| ![mo icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/mo.png) | Macao | MO | `mo`, `macao` |
| ![mp icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/mp.png) | Northern Mariana Islands | MP | `mp`, `northern mariana` |
| ![mq icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/mq.png) | Martinique | MQ | `mq`, `martinique` |
| ![mr icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/mr.png) | Mauritania | MR | `mr`, `mauritania` |
| ![ms icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ms.png) | Montserrat | MS | `ms`, `montserrat` |
| ![mt icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/mt.png) | Malta | MT | `mt`, `malta` |
| ![mu icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/mu.png) | Mauritius | MU | `mu`, `mauritius` |
| ![mv icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/mv.png) | Maldives | MV | `mv`, `maldives` |
| ![mw icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/mw.png) | Malawi | MW | `mw`, `malawi` |
| ![mx icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/mx.png) | Mexico | MX | `mx`, `mexico` |
| ![my icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/my.png) | Malaysia | MY | `my`, `malaysia` |
| ![mz icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/mz.png) | Mozambique | MZ | `mz`, `mozambique` |
| ![na icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/na.png) | Namibia | NA | `na`, `namibia` |
| ![nc icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/nc.png) | New Caledonia | NC | `nc`, `new caledonia` |
| ![ne icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ne.png) | Niger | NE | `ne`, `niger` |
| ![nf icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/nf.png) | NOrfolk Island | NF | `nf`, `norfolk` |
| ![ng icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ng.png) | Nigeria | NG | `ng`, `nigeria` |
| ![ni icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ni.png) | Nicaragua | NI | `ni`, `nicaragua` |
| ![nl icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/nl.png) | Netherlands | NL | `nl`, `netherlands` |
| ![no icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/no.png) | Norway | NO | `no`, `norway` |
| ![np icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/np.png) | Nepal | NP | `np`, `nepal` |
| ![nr icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/nr.png) | Nauru | NR | `nr`, `nauru` |
| ![nu icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/nu.png) | Niue | NU | `nu`, `niue` |
| ![nz icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/nz.png) | New Zealand | NZ | `nz`, `new zealand` |
| ![om icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/om.png) | Oman | OM | `om`, `oman` |
| ![pa icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/pa.png) | Panama | PA | `pa`, `panama` |
| ![pe icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/pe.png) | Peru | PE | `pe`, `peru` |
| ![pf icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/pf.png) | French Polynesia | PF | `pf`, `french polynesia` |
| ![pg icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/pg.png) | Papua New Guinea | PG | `pg`, `papua new guinea` |
| ![ph icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ph.png) | Philippines | PH | `ph`, `philippines` |
| ![pk icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/pk.png) | Pakistan | PK | `pk`, `pakistan` |
| ![pl icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/pl.png) | Poland | PL | `pl`, `poland` |
| ![pm icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/pm.png) | Saint Pierre and Miquelon | PM | `pm`, `saint pierre`, `miquelon` |
| ![pn icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/pn.png) | Pitcairn | PN | `pn`, `pitcairn` |
| ![pr icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/pr.png) | Puerto Rico | PR | `pr`, `puerto rico` |
| ![ps icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ps.png) | Palestine | PS | `ps`, `palestine` |
| ![pt icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/pt.png) | Portugal | PT | `pt`, `portugal` |
| ![pw icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/pw.png) | Palau | PW | `pw`, `palau` |
| ![py icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/py.png) | Paraguay | PY | `py`, `paraguay` |
| ![qa icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/qa.png) | Qatar | QA | `qa`, `qatar` |
| ![re icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/re.png) | Réunion | RE | `re`, `reunion` |
| ![ro icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ro.png) | Romania | RO | `ro`, `romania` |
| ![rs icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/rs.png) | Serbia | RS | `rs`, `serbia` |
| ![ru icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ru.png) | Russia | RU | `ru`, `russia` |
| ![rw icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/rw.png) | Rwanda | RW | `rw`, `rwanda` |
| ![sa icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/sa.png) | Saudi Arabia | SA | `sa`, `saudi arabia` |
| ![sb icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/sb.png) | Solomon Islands | SB | `sb`, `solomon islands` |
| ![sc icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/sc.png) | Seychelles | SC | `sc`, `seychelles` |
| ![sd icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/sd.png) | Sudan | SD | `sd`, `sudan` |
| ![se icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/se.png) | Sweden | SE | `se`, `sweden` |
| ![sg icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/sg.png) | Singapore | SG | `sg`, `singapore` |
| ![sh icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/sh.png) | Saint Helena | SH | `sh`, `saint helena` |
| ![si icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/si.png) | Slovenia | SI | `si`, `slovenia` |
| ![sj icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/sj.png) | Svalbard and Jan Mayen | SJ | `sj`, `svalbard`, `jan mayen` |
| ![sk icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/sk.png) | Slovakia | SK | `sk`, `slovakia` |
| ![sl icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/sl.png) | Sierra Leone | SL | `sl`, `sierra leone` |
| ![sm icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/sm.png) | San Marino | SM | `sm`, `san marino` |
| ![sn icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/sn.png) | Senegal | SN | `sn`, `senegal` |
| ![so icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/so.png) | Somalia | SO | `so`, `somalia` |
| ![sr icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/sr.png) | Suriname | SR | `sr`, `suriname` |
| ![ss icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ss.png) | South Sudan | SS | `ss`, `south sudan` |
| ![st icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/st.png) | São Tomé and Príncipe | ST | `st`, `sao tome`, `principe` |
| ![sv icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/sv.png) | El Salvador | SV | `sv`, `el salvador` |
| ![sx icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/sx.png) | Sint Maarten | SX | `sx`, `sint maarten` |
| ![sy icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/sy.png) | Syria | SY | `sy`, `syria` |
| ![sz icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/sz.png) | Eswatini | SZ | `sz`, `eswatini` |
| ![tc icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/tc.png) | Turks and Caicos Islands | TC | `tc`, `turks`, `caicos` |
| ![td icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/td.png) | Chad | TD | `td`, `chad` |
| ![tf icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/tf.png) | French Southern Territories | tf | `tf`, `french southern territories` |
| ![tg icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/tg.png) | Togo | TG | `tg`, `togo` |
| ![th icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/th.png) | Thailand | TH | `th`, `thailand` |
| ![tj icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/tj.png) | Tajikistan | TJ | `tj`, `tajikistan` |
| ![tk icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/tk.png) | Tokelau | TK | `tk`, `tokelau` |
| ![tl icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/tl.png) | East Timor | TL | `tl`, `east timor` |
| ![tm icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/tm.png) | Turkmenistan | TM | `tm`, `turkmenistan` |
| ![tn icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/tn.png) | Tunisia | TN | `tn`, `tunisia` |
| ![to icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/to.png) | Tonga | TO | `to`, `tonga` |
| ![tr icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/tr.png) | Turkey | TR | `tr`, `turkey` |
| ![tt icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/tt.png) | Trinidad and Tobago | TT | `tt`, `trinidad`, `tobago` |
| ![tv icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/tv.png) | Tuvalu | TV | `tv`, `tuvalu` |
| ![tw icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/tw.png) | Taiwan | TW | `tw`, `taiwan` |
| ![tz icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/tz.png) | Tanzania | TZ | `tz`, `tanzania` |
| ![ua icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ua.png) | Ukraine | UA | `ua`, `ukraine` |
| ![ug icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ug.png) | Uganda | UG | `ug`, `uganda` |
| ![um icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/um.png) | United States Minor Outlying Islands | UM | `um`, `united states minor outlying islands` |
| ![us icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/us.png) | United States | YS | `us`, `united states`, `us` |
| ![uy icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/uy.png) | Uruguay | UY | `uy`, `uruguay` |
| ![uz icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/uz.png) | Uzbekistan | UZ | `uz`, `uzbekistan` |
| ![va icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/va.png) | Holy See | VA | `va`, `vatican`, `holy see` |
| ![vc icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/vc.png) | Saint Vincent and Genadines | VC | `vc`, `saint vincent`, `grenadines` |
| ![ve icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ve.png) | Venezuela | VE | `ve`, `venezuela` |
| ![vg icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/vg.png) | British Virgin Islands | VG | `vg`, `british virgin islands` |
| ![vi icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/vi.png) | United States Virgin Islands | VI | `vi`, `us virgin islands` |
| ![vn icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/vn.png) | Vietnam | VN | `vn`, `vietnam` |
| ![vu icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/vu.png) | Vanuatu | VU | `vu`, `vanuatu` |
| ![wf icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/wf.png) | Wallis and Futuna | WF | `wf`, `wallis`, `futuna` |
| ![ws icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ws.png) | Samoa | WS | `ws`, `samoa` |
| ![xk icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/xk.png) | Kosovo | XK | `xk`, `kosovo` |
| ![ye icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/ye.png) | Yemen | YE | `ye`, `yemen` |
| ![yt icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/yt.png) | Mayotte | YT | `yt`, `mayotte` |
| ![za icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/za.png) | South Africa | ZA | `za`, `south africa` |
| ![zm icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/zm.png) | Zambia | ZM | `zm`, `zambia` |
| ![zw icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/zw.png) | Zimbabwe | ZW | `zw`, `zimbabwe` |
| ![_africa icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/_africa.png) | Africa | - | `africa` |
| ![_asia icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/_asia.png) | Asia | - | `asia` |
| ![_australia icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/_australia.png) | Australia | - | `australia continent` |
| ![_europe icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/_europe.png) | Europe | - | `europe` |
| ![_north_america icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/_north_america.png) | North America | - | `north america` |
| ![_south_america icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/_south_america.png) | South America | - | `south america` |
| ![_world icon](https://raw.githubusercontent.com/krzysztofrewak/flat-flags-iconset/master/flags/_world.png) | World | - | `world` |
