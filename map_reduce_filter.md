#Map, Reduce, Filter
Scott McCallister

Very slick built in ad for Smartsheet

filter()
map()
reduce()

```	
for (let i = 0; i < people.length; i++) {
	if (people[i]).age >= 18) {
	adults.push(people[i]);
	}
}
```

_can be:_

var adults = people.filter((person) => person.age >= 18);

##Go through an array, filtering in the things that meet the condition and return it
`array.filter(function(element, index, array), thisArg)`

##Go through an array, doing someting to each element of the array
array.map(function(currentValue, index, array), thisValue)
_map is a transform_

`var aged = people.map((person) => person.age + 1);`

#Applies a function against an accumulator and exh element in the array (from left to right) to reduce it to a single value.
array.reduce(functionPaccumulator, currentValue, currentIndex, array), initialValue)

###Chaining the functions is where it gets really fun

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9];
// goes from left to right, firlter first then map
let tripleOdds = numbers.
	// find odd
	filter(n) => n%2 != 0).
	// triple
	map(odd) => odd*3;

_Keep browser compatability in mind_