## Usage
Use CDN to add stylesheet into your head section (using one with integrity hash could be a good practice):
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/krzysztofrewak/flat-flags-iconset/style.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/krzysztofrewak/flat-flags-iconset/style.css" integrity="SHA384_INTEGRITY_HASH" crossorigin="anonymous">
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
