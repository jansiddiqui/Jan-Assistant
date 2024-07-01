// controller.js
$(document).ready(function () {
    // Display Speak Message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
        $(".siri-message li:first").text(message);
        $(".siri-message").textillate('start');
    }
    // Display Hood
    eel.expose(DisplayHood)
    function DisplayHood() {
        $("#Oval").removeClass("hidden");
        $("#SiriWave").addClass("hidden");
    }
});

