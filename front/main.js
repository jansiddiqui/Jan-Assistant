// main.js
$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "bounceIn",
        },
        out:{
            effect: "bounceOut",
        },
    });
    // Siri configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
    });
    // Siri message animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "fadeInUp",
            sync: true,
        },
        out:{
            effect: "fadeOutUp",
            sync: true,
        },
    });
    // Mic button click event
    $("#MicBtn").click(function () { 
        eel.playassistantsound()
        $("#Oval").addClass("hidden");
        $("#SiriWave").removeClass("hidden");
        eel.allCommands()()
    });

    function doc_keyUp(e){
        //this would test for whichever key is 40 (down arrow) and the ctrl key at the same time
        if (e.key == 'j' && e.metaKey) {
            eel.playassistantsound()
            $("#Oval").removeClass("hidden");
            $("#SiriWave").addClass("hidden");
            eel.allCommands()()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    // Function to Process Assistant Message
    function PlayAssistant(message) {
        if (message !== "") {
            $("#Oval").addClass("hidden");
            $("#SiriWave").removeClass("hidden");
            eel.allCommands(message); // Execute the assistant command
            $("#chatbox").val(""); // Clear the input field
            $("#MicBtn").removeClass("hidden"); // Show the mic button
            $("#SendBtn").addClass("hidden"); // Hide the send button
        }
    }

    // Function to Show/Hide Buttons Based on Input
    function ShowHideButton(message) {
        if (message.length === 0) {
            $("#MicBtn").removeClass("hidden");
            $("#SendBtn").addClass("hidden");
        } else {
            $("#MicBtn").addClass("hidden");
            $("#SendBtn").removeClass("hidden"); 
        }
    }

    // Input Field Keyup Event
    $("#chatbox").keyup(function () {
        let message = $("#chatbox").val();
        ShowHideButton(message);
    });

    // Send Button Click Event
    $("#SendBtn").click(function () {
        let message = $("#chatbox").val();
        PlayAssistant(message);
    });
    
    $("#chatbox").keypress(function (e){
        key = e.which;
        if(key == 13) {
            let message = $("#chatbox").val();
            PlayAssistant(message);
        }
    });
});