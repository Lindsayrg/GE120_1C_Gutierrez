
console.log("Hello madlang people, mabuhay!")

// creating variable in Js
let x = 5
var y = 6
const z = 7

// if stateents 
if (x == y) {
        console.log(x).toString().concat(" is equal to ", y.toString())
} else if (x == z)


//array
var students = ["peter", "maja", "aj", "quinmar"]
console.log(students) 

//Comparing two values and data types
console.log(0 == "0")
console.log(0 === "0")

// for loop
for (var i = 0; i <= z; i++){
    console.log(i)
}

for(var student of students){
    for (var i = 0; i < student.length; i++)[
        console.log(student[1])
    ]
}

// While loop
function degreesToRadians(num) {
    var value = number * Math.PI / 180
    return value
}

console.log(degreesToRadians(180))

function getLatitude(distance, azimuth) {
    var laitude = -distance * Math.cos(degreesToRadians(azimuth))
    return latitude
}

console.log(getLatitude)