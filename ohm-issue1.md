This is a little rough, but I wanted to get something out there before I went too far down the rabbit hole :smile:.

After a lot of digging (and some circular searching), I found this paper(http://www.ahahah.eu/data/doc/gisscience2012_gaffuri_draft.pdf) from 2012 which describes four interoperable parts to making client-side vector rendering work for web mapping:
1. Ensuring only the "relevant 'data slice'" or Level of Detail (LoD) is served up to the client. Why bog the browser down with a load of vectors which aren't even viewable at the current zoom/view?
2. Deciding between vector tiling or spatial indexing (vector tiling is best for our needs, but the detail/type of images needed for the OSM Buildings project might benefit from using spatial indexing.)
3. The use of generalization is important to prevent serving up so many vectors that the map is distorted (the author of the paper shows an example of literally discriminating the forest from the trees that makes the point nicely.) [www.ahahah.eu/data/doc/gissience2012_gaffuri_draft.pdf, top of page 9)
4. Finally, progressive transmission of the vector data requires that an inital push of vectors goes down to the client (so the browser has something to display) and then the rest of the data can be served.

The paper supports the use of OpenCarto(http://www.opencarto.ahahah.eu/), a Java vector mapping library, but the methods described within can be used as filters for searching for Javascript libraries that would be appropriate for our use.

###Kothic.js###
https://github.com/kothic/kothic-js
Kothic has the whole package in one place. There are lots of rave reviews about other libraries and tools, though:

###Cartagen###
http://cartagen.org/
Cargagen uses Geographic Style Sheets to describe how to render the vectors. It's wiki specifically says it can be useful for rendering time-based data https://github.com/jywarren/cartagen/wiki

###Notable Libraries###
###OpenLayers###
Many users on gis.stackexchange like the performance of OpenLayers. It uses WebGL, which has some compatability issues, though - http://caniuse.com/webgl

###Polymaps###
http://polymaps.org/
Javascript library, uses SVG

###Leaflet.js###
http://leafletjs.com/index.html
Another Javascript library, apparently especially good for mobile, already in use for the Android and iOS Wikimedia apps. 

###CartoDB###
https://github.com/CartoDB/torque/tree/new_torque
CartoDB uses Leaflet. I'm still looking through it - it's demo page on
http://cartodb.github.io/torque/ is rather striking and uses historical data.
