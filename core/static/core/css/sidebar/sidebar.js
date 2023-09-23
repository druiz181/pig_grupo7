// // A function is used for dragging and moving
// function dragElement(element, direction)
// {
//     var   md; // remember mouse down info
//     const first  = document.getElementById("first");
    // const second = document.getElementsByClassName("js-sidebar")[0];

//     element.onmousedown = onMouseDown;
    
//     function onMouseDown(e)
//     {
//       //console.log("mouse down: " + e.clientX);
//       md = {e,
//         offsetLeft:  element.offsetLeft,
//         offsetTop:   element.offsetTop,
//         firstWidth:  first.offsetWidth,
//         secondWidth: second.offsetWidth
//       };
//       console.log(md)

//         document.onmousemove = onMouseMove;
//         document.onmouseup = () => {
//             //console.log("mouse up");
//             document.onmousemove = document.onmouseup = null;
//         }
//     }

//     function onMouseMove(e)
//     {
//         //console.log("mouse move: " + e.clientX);
//         var delta = {x: e.clientX - md.e.clientX,
//                      y: e.clientY - md.e.clientY};

//         if (direction === "H" ) // Horizontal
//         {
//             // Prevent negative-sized elements
//             delta.x = Math.min(Math.max(delta.x, -md.firstWidth),
//                        md.secondWidth);

//             element.style.left = md.offsetLeft + delta.x + "px";
//             first.style.width = (md.firstWidth + delta.x) + "px";
//             second.style.width = (md.secondWidth - delta.x) + "px";
//         }
//     }
// }


// dragElement( document.getElementById("separator"), "H" );


let btnToggler = document.getElementsByClassName("js-sidebar__toggler")[0];
let sidebar = document.getElementsByClassName("js-sidebar")[0];


btnToggler.addEventListener("click", (e) => {
  console.log(e.target == btnToggler, "--------");
  if (sidebar.classList.contains("js-sidebar__active")) {
    sidebar.classList.remove("js-sidebar__active");
  }
  else sidebar.classList.toggle("js-sidebar__active");
});

// Close the sidebar when the focus is lost on the button
btnToggler.addEventListener('blur', () => {
});