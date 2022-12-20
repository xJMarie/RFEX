
// Show dropdown
$("#dropdownMenuIconButton").click(function () {
   if ($("#dropdownMenu_Guest").hasClass('hidden') == true)
      $("#dropdownMenu_Guest").removeClass('hidden');
   else
      $("#dropdownMenu_Guest").addClass('hidden');
});

$("#dropdownSearch").click(function () {
   if ($("#dropdownMenu_Search").hasClass('hidden') == true)
      $("#dropdownMenu_Search").removeClass('hidden');
   else
      $("#dropdownMenu_Search").addClass('hidden');
});