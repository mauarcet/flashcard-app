import React, { useState, useEffect } from "react";

const Flashcard = ({ card, onNext }) => {
  const [showConcept, setShowConcept] = useState(true);
  const [answer, setAnswer] = useState("");

  // Show concept for 6 seconds
//  useEffect(() => {
//    const timer = setTimeout(() => setShowConcept(false), 6000);
//    return () => clearTimeout(timer);
//  }, [card]);

  return (
    <div>
      {console.log(card)}
      {showConcept ? (
        <h2>Concept: {card.concept}</h2>
      ) : (
        <>
          <input
            type="text"
            placeholder="Type definition..."
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
          />
          <button onClick={() => onNext(answer)}>Next</button>
        </>
      )}
    </div>
  );
};

export default Flashcard;

