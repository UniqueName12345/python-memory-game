function main() {
    console.log("\nWelcome to the game!");
    console.log("1. Play");
    console.log("2. Exit");
    const choice = prompt("\nPlease choose an option: ");
    switch (choice) {
      case "1":
        console.log(`\nYou have chosen to play the game.`);
        game_play();
        break;
      case "2":
        exit();
        break;
      default:
        console.log("\nInvalid option. Please try again.");
        main();
        break;
    }
  }
  

function generate_random_number() {
    return (Math.random() * 10 + 1) | 0;
}


function get_user_guess() {
    return prompt("\nGuess a number between 1 and 10: ");
}

function checkGuess(randomNumber, guess) {
    return randomNumber === guess;
}

function game() {
    let play_again = prompt("\nDo you want to play again? (y/n): ");
    if (play_again.toLowerCase() === 'y') {
        game_play();
    }
}

function game_play() {
    while(true) {
        let guess = get_user_guess();
        if (checkGuess(generate_random_number(), guess)) {
            return;
        }
    }
}

