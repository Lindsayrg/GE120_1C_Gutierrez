/*
GE 120 Machine Exercise 3
April 18, 2024
Lindsay Gutierrez 
2023-02961
*/

function getLatitude(distance, azimuth) {
    let lat = -(distance)*(Math.cos(azimuth * Math.PI / 180.0))
    return lat
}

function getDeparture(distance, azimuth) {
    let dep = -(distance)*(Math.sin(azimuth * Math.PI / 180.0))
    return dep
}

function azimuthToBearing(azimuth) {
    /*if (azimuth.includes("-"))
    [degrees, minutes, seconds] = azimuth.split("-")
    azimuth = ((parseInt(degrees)) + (parseInt(minutes)/60) + (parseFloat(seconds)/3600))%360
    } else {
        azimuth = parseFloat(azimuth)%360  
    }*/

 // In case the input value of azimuth is in the form of dms


   if (azimuth > 0 && azimuth < 90) {
        let azimuth_dms = azimuth
        let degree = Math.floor(azimuth)
        let minutes = (azimuth_dms - degree) * 60
        let minutes_fractional = Math.floor(minutes)
        let seconds = ((minutes - minutes_fractional) * 60)
        let br_dms = degree + "-" + (Math.floor(minutes))  + "-" + (Math.round(seconds,2))

        let bearing = "S" + br_dms.padStart(10) + " W"
        return bearing 
   } else if (azimuth > 90 && azimuth <180) {

        let azimuth_dms = 180 - azimuth

        let degree = Math.floor(azimuth_dms)
        let minutes = (azimuth_dms - degree) * 60
        let minutes_fractional = Math.floor(minutes)
        let seconds = ((minutes - minutes_fractional) * 60)
        let br_dms = degree + "-" + (Math.floor(minutes)) + "-" + (Math.round(seconds,2))

        let bearing = "N" + br_dms.padStart(10) + " W"
        return bearing 
   } else if (azimuth > 180 && azimuth <270) {

        let azimuth_dms = azimuth - 180

        let degree = Math.floor(azimuth_dms)
        let minutes = (azimuth_dms - degree) * 60
        let minutes_fractional = Math.floor(minutes)
        let seconds = ((minutes - minutes_fractional) * 60)
        let br_dms = degree + "-" + (Math.floor(minutes)) + "-" + (Math.round(seconds,2))

        let bearing = "N" + br_dms.padStart(10) + " E"
        return bearing
   } else if (azimuth > 270 && azimuth <360){
        let azimuth_dms = 360 - azimuth

        let degree = Math.floor(azimuth_dms)
        let minutes = (azimuth_dms - degree) * 60
        let minutes_fractional = Math.floor(minutes)
        let seconds = ((minutes - minutes_fractional) * 60)
        let br_dms = degree+ "-" + (Math.floor(minutes))+ "-" + (Math.round(seconds,2))

        let bearing = "S" + br_dms.padStart(10) + " E"
        return bearing
   } else if (azimuth == 0){
        return"   DUE SOUTH  "
   } else if (azimuth == 90) {
        return "   DUE WEST  "
   } else if (azimuth == 180) {
        return "   DUE NORTH  "
   } else if (azimuth == 270) {
        return "   DUE EAST  "
   } else {
        return "Please input an azimuth value."
   } 
}
var data = [
    [13.23, 124.795],
    [15.57, 14.143],
    [43.36, 270.000],
    [23.09, 188.169],
    [10.99, 180.000],
    [41.40, 50.562],
]
var lines = []
var lines2 = []
var lines3 = []
var sumLat = 0 
var sumDep = 0
var sumDist = 0 

/* Code if no set of values are assigned and values need to be an input
while (True){
    console.log ()
    console.log("Line No.", counter, '-', counter + 1 )

    let wrong_input = false
    while (!wrong_input) {
        let distance = input('Distance: ')
        if (wrong_input) {
            console.log("Invalid. Please input valid distance value")
            continue
        } if (!wrong_input) {
            break
        }
*/

for (var i = 0 ; i < data.length ; i++) { // increment

    let line = data[i]
    let distance = line[0]
    let azimuth = line[1]

    let bearingPrint = azimuthToBearing(azimuth)
    let latPrint = getLatitude(distance, azimuth)
    let depPrint = getDeparture(distance, azimuth) 
    
    sumLat += latPrint //+= INCEREMENT
    sumDep += depPrint
    sumDist = sumDist + parseFloat(distance)
    
    lines.push([((i+1)), distance,  bearingPrint, Math.round(latPrint,5), Math.round(depPrint,5)]) //append line in terms of javascript 
 }  

 // print the output
console.log("\n\nLines")
console.log("LINE NO.".padEnd(12), "DISTANCE".padEnd(18), "BEARING".padEnd(20), "LATITUDE".padEnd(16), "DEPARTURE".padEnd(30))
for (var line of lines){
    console.log(line[0].toString().padEnd(13), 
    line[1].toString().padEnd(14), 
    line[2].toString().padEnd(25), 
    line[3].toString().padEnd(18),
    line[4].toString().padEnd(25))
}

line2 = [
    Math.round(sumLat,5), 
    Math.round(sumDep,5), 
    Math.round(sumDist,5)
] // for the table of the summation of values
lines2.push(line2)

// print the output
// summation of latitude, departure, distance
console.log("\n\nSummation")
console.log("∑ Latitude ".padEnd(17), "∑ Departure ".padEnd(17), "∑ Distance ".padEnd(27))
for (var line2 of lines2){
    console.log(line2[0].toString().padEnd(22), 
    line2[1].toString().padEnd(16), 
    line2[2].toString().padEnd(12))
}


let LEC = Math.sqrt((Math.pow(sumLat,2) + (Math.pow(sumDep,2))))
let REC = sumDist/LEC

// print the output
// LEC AND REC
console.log("\n")
console.log("LEC: ", LEC.toPrecision(5))
console.log("1: ", Math.floor(REC/1000)*1000)


// code for corrections

/*function adjLat(distance, azimuth){
    let latitudeCorr = -(distance)*(Math.cos(azimuth * Math.PI / 180.0))
    let ccorr_lat = -(sumLat)/sumDist
    let corr_lat = (ccorr_lat) * distance

    // adjusted latitude
    let adjLat = latitudeCorr + corr_lat
    return adjLat
}

function adjDep(distance, azimuth){
    let departureCorr = -(distance)*(Math.sin(azimuth * Math.PI / 180.0))
    let ccorr_dep = -(sumDep)/ sumDist
    let corr_dep = (ccorr_dep) * distance

    // adjusted departure
    let  adjDep = departureCorr + corr_dep
    return adjDep
}

function corrdep (distance) {
    let ccorr_dep2 = -(sumDep)/ sumDist
    let corrdep = (ccorr_dep2) * distance 
    return corrdep  
}

function corrlat (distance) {
    let ccorr_lat2 = -(sumLat)/sumDist
    let corr_lat = (ccorr_lat2) * distance
    return corr_lat
}

var counter = 0
var count = 1

var line3 = [
    Math.round(corrlat,5),
    Math.round(corrdep,5),
    Math.round(adjLat,5),
    Math.round(adjDep,5)
]


lines3.push([((counter+1) + "-" + (count+1)), line3[0], line3[1], line3[2], line3[3]])

// print the output
//corrections
console.log("\n\nCorrections")
console.log("LINE NO.".padEnd(12), "     Latitude Correction".padEnd(19), "           Departure Correction".padEnd(38), "ADJUSTED LATITUDE".padEnd(23), "ADJUSTED DEPARTURE".padEnd(19))
for (var line3 of lines3){
    console.log(
    line3[0].toString().padEnd(20),
    line3[1].toString().padEnd(31),
    line3[2].toString().padEnd(27),
    line3[3].toString().padEnd(25),
    line3[4].toString().padEnd(20))
}

*/

console.log("\n\n")
console.log("-------------END--------------".padStart(70))

