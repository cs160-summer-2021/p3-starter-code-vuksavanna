var path;
x=0;
function onMouseDown(event) { 
    path = new Path();
    path.add(event.point);
}
function onMouseDrag(event) {
  var circle = Path.Circle(event.point, 50);
  circle.fillColor = 'red';
  circle.fillColor.hue += x;
  x+=10;
}