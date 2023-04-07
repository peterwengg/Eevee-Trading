function rotateScenes() {
  var scroll = window.pageYOffset,
    relPos = scroll / height,
    angle = 90 * relPos;

  if (scroll >= height) {
    section1.style.transform = "rotateX(90deg)";
    section2.style.transform = "rotateX(0deg)";
  }

  section1.style.transform = "rotateX(" + (angle) + "deg)";
  section2.style.transform = "rotateX(-" + (90 - angle) + "deg)";
}

var section1 = document.querySelector("#top"),
  section2 = document.querySelector("#content"),
  height = window.innerHeight;
window.addEventListener("scroll", rotateScenes);