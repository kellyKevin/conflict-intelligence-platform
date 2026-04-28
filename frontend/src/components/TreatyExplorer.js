import React from 'react';

const TreatyExplorer = () => {
  return (
    <div className="component">
      <h3>Treaty Explorer</h3>
      <textarea placeholder="Paste treaty text here..." rows="4" cols="50"></textarea>
      <button>Analyze Clauses</button>
      <div className="results">
        <p>Versailles Treaty Case Study: Effectiveness Score 50/100</p>
      </div>
    </div>
  );
};

export default TreatyExplorer;
