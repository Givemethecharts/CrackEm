function showGreeting() {
      var showGreetingButton = document.getElementById('showGreetingButton');
      var greetingText = document.getElementById('greetingText');
      var borderofText =document.getElementById('text-container')

      // Hide the button
      showGreetingButton.style.display = 'none';

      // Show the greeting text
      greetingText.style.display = 'block';
      borderofText.style.display = 'block'
    }