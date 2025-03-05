import React, { useState, useEffect } from "react";

const Flashcard = ({ card, onNext }) => {
  const [showDef, setShowDef] = useState(true);
  const [answer, setAnswer] = useState("");

  // Show definition for 6 seconds
  useEffect(() => {
    const timer = setTimeout(() => setShowDef(false), 6000);
    return () => clearTimeout(timer);
  }, [card]);

  return (
    <div>
      <h2>Concept: {card.concept}</h2>

      {showDef ? (
        <>
          <h3>{card.definition}</h3>
        </>
      ) : (
        <h3>Clock ticking...</h3>
      )}

      <>
        <input
          type="text"
          placeholder="Type definition..."
          value={answer}
          onChange={(e) => setAnswer(e.target.value)}
        />
        <button onClick={() => onNext(answer)}>Next</button>
      </>
    </div>
  );
};

export default Flashcard;
