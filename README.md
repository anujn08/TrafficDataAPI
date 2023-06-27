# TrafficDataAPI
This repo helps us to extract the  realtime traffic data for a given bounding box or location with the help of Here Map Api keys.
For finding the lat longs of bounding box , use open street map (https://www.openstreetmap.org/search?query=30.8961%2C75.92043#map=14/30.8961/75.9204).



# Refer to https://developer.here.com/documentation/traffic/dev_guide/topics_v6.1/example-flow.html 
# Common Acronyms: Refer to https://developer.here.com/documentation/traffic/dev_guide/topics/common-acronyms.html 
# Also see: https://stackoverflow.com/a/34150385/1359166
# fi --> flow item [[ tmc, shp, cf ]]
# tmc --> Traffic Message Channel : [[de --> name (de probably language); le --> length of the stretch; pc -->point TMC location code qd --> queuing direction (+/-)]]
# shp: [[fc--> functional classes ]] # https://developer.here.com/documentation/traffic/dev_guide/topics/resource-type-functional-class.html
# cf --> Current flow: [[cn -->confidence number (0-1); ff-->free flow speed; jf --> jam factor (0-10); sp -->avg speed ; su --> avg speed uncut (ignore speed limits, thus should be used); ty -->location reference, free string]]
