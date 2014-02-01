function storeData(var location)
{
    var el = document.getElementByClass('form-control');
    var location = el.options[el.selectedIndex].innerHTML;
    var nameRef = new Firebase('https://dxc.firebaseIO-demo.com/'+location);
    nameRef.set(location);
}
