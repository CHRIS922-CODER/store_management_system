// script.js

    // Get all tabs
    var tabs = document.getElementsByClassName('tab');

    // Add click event listener to each tab
    for (var i = 0; i < tabs.length; i++) {
      tabs[i].addEventListener('click', function(event) {
        var tab = event.target;
        var tabName = tab.getAttribute('data-tab');

        // Remove active class from all tabs
        for (var j = 0; j < tabs.length; j++) {
          tabs[j].classList.remove('active');
        }

        // Add active class to the clicked tab
        tab.classList.add('active');
      });
    }