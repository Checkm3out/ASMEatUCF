var myCollection2 = document.getElementsByTagName("hr");
// console.log('collection length: ');
// console.log(myCollection2.length);
// console.log("item 0");
// console.log(myCollection2.item(0));
console.log(myCollection2[0].nodeName)
for( let i = 0; i<myCollection2.length; i++){

    var elem = myCollection2[i]
    elem.classList.add('hidden');

    var getSiblings = function (elem) {

        // Setup siblings array and get the first sibling
        var siblings = [];
        var sibling = elem.nextElementSibling;

        //create a new div for the child elements
        var newDiv = document.createElement('div');
        newDiv.classList.add('jumbotron');
        newDiv.id = ('newDiv');

        var container = document.getElementById('container');
        container.insertBefore(newDiv, container.firstChild.nextSibling);



        // Loop through each sibling and push to the array
        while (sibling) {
            if (sibling.nodeType === 1 && sibling !== elem) {
                console.log(sibling.nodeName)
                if(sibling.nodeName === "HR"){

                    break;
                }
                else{
                    siblings.push(sibling);

                }

            }

            sibling = sibling.nextSibling

	}

	//iterate through sibling array and the info into the appropriate div
	for(let i = 0; i<siblings.length; i++){
	    document.getElementById("newDiv").insertAdjacentHTML( 'beforeend', '<div>'+ siblings[i].outerHTML + '</div>');
	    //make the copied elements disapear
	    siblings[i].classList.add('hidden');
        console.log(siblings[i].outerHTML)
    }

	return siblings;

};

var siblings = getSiblings(elem);

console.log(siblings)


}
//     console.log("entered for loop: " + i)
//     var htmlhrElement = myCollection2.item(i);
//     console.log('loaded hr element');
//     console.log(htmlhrElement);
//
//     var container = document.getElementById('container');
//     var myCollection = container.getElementsByTagName("p");
//
//     var newDiv= document.createElement('div');
//     newDiv.classList.add('jumbotron');
//
//     var info = htmlhrElement.nextElementSibling;
//     console.log("info sibling:" + info.nodeName)
//     if(info == "null"){
//         console.log("we hit a null");
//     }
//
//
//     if(info.nodeName == 'null'){
//         console.log("we hit a null");
//
//     }
//     else{
//         console.log("info2 sibling:" + info2.nodeName)
//         var info2 = info.nextElementSibling;
//     }
//
//
//
//     var info3 = info2.nextElementSibling;
//
//     // alert(info);
//
//
//
//
//
//     if(document.body.contains(htmlhrElement)){
//             htmlhrElement.classList.add('hidden')
//             info = htmlhrElement.nextElementSibling;
//             if(info.contains(null)){
//                 // alert('null');
//             }
//             else{
//                 htmlhrElement.nextElementSibling.classList.add('hidden');
//             }
//
//
//
//             // alert(item.childNodes.length);
//             // alert(htmlhrElement.nodeType);
//             // htmlhrElement.insertAdjacentHTML('beforebegin', '</div><div class="jumbotron">')
//             container.insertBefore(newDiv, container.firstChild.nextSibling);
//             newDiv.id = ('newDiv');
//
//             // alert(myCollection.length)
//             for(let i = 0; i < myCollection.length; i++){
//                 document.getElementById("newDiv").insertAdjacentHTML( 'beforeend', '<div>'+ myCollection[i].innerText+ '</div>');
//             }
//
//
//
//
//
//         }
//         else{
//
//         }
//
//
// }

