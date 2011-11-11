
(function() {
  $dm.server('http://arya.stanford.edu:3777/');
  $dm.api_key('6b044f121358683678e5e21de2202a5e0a0394d5');
  console.log($dm);
  $dm.getTasks(function(r) {
    console.log(r);
  });
})();
