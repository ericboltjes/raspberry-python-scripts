<?php
$json = file_get_contents("https://api.tbssi21a.de/jokes/random");
$ar = (explode(",",$json));
$w0 = strlen($ar[0]);
$w1 = strlen($ar[1]);
$w = $w0 + $w1 +10;
$id = substr($ar[1], 5);
$genre = substr($ar[0],11 ,-1);
$joke = substr($json, $w, -4);
?>

<html>


<html style="font-size: 16px;" lang="de"><head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8">
    <meta name="keywords" content="Jokes">
    <title>Jokes</title>
    <link rel="stylesheet" href="nicepage.css" media="screen">
    <link rel="stylesheet" href="Startseite.css" media="screen">





</script>
    <meta name="theme-color" content="#478ac9">
  </head>
  <body data-home-page="Startseite.html" data-home-page-title="Startseite" class="u-body u-xl-mode" data-lang="de">
    <section class="u-clearfix u-section-1" id="sec-5a70">
      <div class="u-clearfix u-sheet u-sheet-1">
        <h1 class="u-text u-text-default u-text-1">Jokes</h1>
        <div class="u-container-style u-group u-palette-4-base u-radius-30 u-shape-round u-group-1">
          <div class="u-container-layout u-container-layout-1">
            <h3 class="u-align-center u-text u-text-body-color u-text-2"><p><?php echo $joke; ?></p></h3>
            <h5 class="u-text u-text-body-color u-text-default u-text-3"><p><?php echo $genre; ?></p></h5>
          </div>
        </div>
        <button onClick="history.go(0);" class="u-btn u-btn-round u-button-style u-hover-palette-1-light-1 u-palette-5-light-1 u-radius-50 u-btn-1">Reload</button>
      </div>
    </section>



</body></html>
