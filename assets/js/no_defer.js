// add bootstrap classes to tables
$(document).ready(function () {
  $("table").each(function () {
    if (determineComputedTheme() == "dark") {
      $(this).addClass("table-dark");
    } else {
      $(this).removeClass("table-dark");
    }

    // Avoid applying table styling inside cards.
    if (
      $(this).parents('[class*="card"]').length == 0 &&
      $(this).parents("code").length == 0
    ) {
      // make table use bootstrap-table
      $(this).attr("data-toggle", "table");
      // add some classes to make the table look better
      // $(this).addClass('table-sm');
      $(this).addClass("table-hover");
    }
  });
});
