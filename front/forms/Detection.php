<?php
 $receiving_email_address = 'onsouhibi9@gmail.com';
 
if ($_SERVER['REQUEST_METHOD'] === 'POST') {

  $temp = $_POST['Temperature'];
  $Ws = $_POST['Windspeed'];
  $Rain = $_POST['Rain'];
  $FFMC = $_POST['Fuel Moisture Code'];
  $DMC = $_POST['Duff Moisture Code'];
  $ISI = $_POST['Initial spread index'];
  
 /// exemple aal affichage kifeh ykoun lenna aamalt 
  if ($temp > 30) {
    echo "Stay alert !!! Our fire prediction system indicates potential danger in your area. Take necessary precautions to stay safe.";
  } else {
    echo "Good news! Our fire prediction system indicates that there is no immediate danger in your area.";
  }
  
}
?>
