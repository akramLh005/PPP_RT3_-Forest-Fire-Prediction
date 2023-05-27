<?php
$backend_api_url = 'http://127.0.0.1:8000/prediction'; 

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $temp = $_POST['Temperature'];
    $Ws = $_POST['Windspeed'];
    $Rain = $_POST['Rain'];
    $FFMC = $_POST['Fuel Moisture Code'];
    $DMC = $_POST['Duff Moisture Code'];
    $ISI = $_POST['Initial spread index'];

    // Preparing data for POST request
    $data = array(
        'temp' => $temp,
        'Ws' => $Ws,
        'Rain' => $Rain,
        'FFMC' => $FFMC,
        'DMC' => $DMC,
        'ISI' => $ISI
    );

    $options = array(
        'http' => array(
            'header'  => "Content-Type: application/json\r\n",
            'method'  => 'POST',
            'content' => json_encode($data),
        ),
    );

    $context = stream_context_create($options);
    $response = file_get_contents($backend_api_url, false, $context);

    if ($response === false) {
        die('Error: Unable to connect to the backend API.');
    }

    $prediction = json_decode($response, true);
    $is_fire_danger = $prediction['prediction value'] == 0;

    if ($is_fire_danger) {
        echo "Stay alert !!! Our fire prediction system indicates potential danger in your area. Take necessary precautions to stay safe.";
    } else {
        echo "Good news! Our fire prediction system indicates that there is no immediate danger in your area.";
    }
}
?>
