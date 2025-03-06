import React, { useState, useEffect } from "react";
import Flashcard from "./Flashcard";

function App() {
  const [card, setCard] = useState(null);
  const [sessionTime, setSessionTime] = useState(60); // 1 min by default
  const [response, setResponse] = useState(null)
  let card_index = 0
  useEffect(() => {
    // Fetch cards
    fetch("http://localhost:8000/cards")
      .then((res) => {
        if (!res.ok) {
          throw new Error("Network response was not ok");
        }
        return res.json();
      })
      .then((data) => {
        setResponse(data);
        setCard(data[card_index]);
      })
      .catch((error) => console.error(error));
  }, []);

  const handleNext = (userAnswer) => {
    // Process the answer (scoring logic, etc.)
    console.log("User answer:", userAnswer);
    // Fetch next card...
    card_index = card_index + 1
    if (response != null) {
      setCard(response[card_index])
    }

  };

  return (
    <div>
      <h1>Flashcard Study App</h1>
      <p>Session time: {sessionTime} seconds</p>
      {card && <Flashcard card={card} onNext={handleNext} />}

      {/* Add timer and topic selection components as needed */}
    </div>
  );
}

export default App;

