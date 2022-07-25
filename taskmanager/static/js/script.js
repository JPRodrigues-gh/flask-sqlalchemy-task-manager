document.addEventListener('DOMContentLoaded', function() {
    // sidenav Initialization
    var sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // Date Picker Initialization
    var datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
      format: "dd mmmm yyyy",
      i18n: {done: "Select"}
    });

    // select initialization
    var selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);

    // collapsible initialization
    var collapsibles = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsibles);
  });