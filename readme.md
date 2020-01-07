# About
This package is a simple semantic wrapper for Flatstudio's [Flat Flags](https://dribbble.com/shots/4028772-Freebies-Flat-Flags-227) icon set. 

## Usage
You can insert a flag via country's [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code combined with `flat flag` CSS class:
```html
<i class="is flat flag"></i>
<i class="md flat flag"></i>
<i class="tn flat flag"></i>
```

Simple country names are working too:
```html
<i class="iceland flat flag"></i>
<i class="moldova flat flag"></i>
<i class="tunisia flat flag"></i>
```

You can add resizing classes `large`, `huge` and `giant` to receive bigger images. It's working also with container tagged `flat flags`:
```html
<div class="huge flat flags">
    <i class="australia flat flag"></i>
    <i class="new zealand flat flag"></i>
</div>
```

## For developers
You can rebuild `style.css` from `resources.json` via Python script:
```sh
docker-compose run -w /application python python builder.py
```