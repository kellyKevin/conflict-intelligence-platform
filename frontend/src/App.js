import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer,
  BarChart, Bar
} from 'recharts';

const API_BASE = "http://localhost:8000";

const ConflictDashboard = () => {
  const [ewsData, setEwsData] = useState([]);
  const [treatyText, setTreatyText] = useState("");
  const [ptaResults, setPtaResults] = useState(null);
  const [ethicalParams, setEthicalParams] = useState({ autonomy: 0.5, confidence: 0.8, density: 0.3, proportionality: 0.5 });
  const [ethicalScore, setEthicalScore] = useState(null);

  useEffect(() => {
    // Load some initial EWS data
    const regions = ["Sudan", "Libya", "Ukraine", "Gaza"];
    Promise.all(regions.map(r => axios.get(`${API_BASE}/ews/risk-index?region=${r}`)))
      .then(responses => setEwsData(responses.map(res => res.data)));
  }, []);

  const analyzeTreaty = () => {
    axios.get(`${API_BASE}/pta/treaty-analysis`, { params: { text: treatyText } })
      .then(res => setPtaResults(res.data));
  };

  const calculateEthicalScore = () => {
    axios.get(`${API_BASE}/efaw/ethical-score`, { params: ethicalParams })
      .then(res => setEthicalScore(res.data.risk_score));
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h1>Conflict Intelligence & Ethics Platform</h1>

      <section style={{ marginBottom: '40px' }}>
        <h2>1. Conflict Early-Warning System</h2>
        <div style={{ display: 'flex', gap: '20px' }}>
          <div style={{ flex: 1, border: '1px solid #ccc', padding: '10px' }}>
            <h3>Regional Risk Index</h3>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={ewsData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="region" />
                <YAxis domain={[0, 100]} />
                <Tooltip />
                <Legend />
                <Bar dataKey="current_risk_score" fill="#8884d8" name="Risk Score" />
              </BarChart>
            </ResponsiveContainer>
          </div>
          <div style={{ width: '300px', border: '1px solid #ccc', padding: '10px' }}>
            <h3>Risk Alerts</h3>
            {ewsData.map(d => (
              <div key={d.region} style={{ color: d.current_risk_score > 60 ? 'red' : 'orange' }}>
                <strong>{d.region}</strong>: {d.current_risk_score} ({d.trend})
              </div>
            ))}
          </div>
        </div>
      </section>

      <section style={{ marginBottom: '40px' }}>
        <h2>2. Peace Treaty Analytics</h2>
        <textarea
          value={treatyText}
          onChange={(e) => setTreatyText(e.target.value)}
          placeholder="Paste treaty text here..."
          style={{ width: '100%', height: '100px' }}
        />
        <br />
        <button onClick={analyzeTreaty} style={{ marginTop: '10px' }}>Analyze Clauses</button>
        {ptaResults && (
          <div style={{ marginTop: '20px', padding: '10px', background: '#f0f0f0' }}>
            <h3>Analysis Results</h3>
            <ul>
              {ptaResults.map((r, i) => (
                <li key={i}>
                  "{r.clause.substring(0, 50)}..." -> <strong>{r.label}</strong> (Confidence: {r.score.toFixed(2)})
                </li>
              ))}
            </ul>
          </div>
        )}
      </section>

      <section style={{ marginBottom: '40px' }}>
        <h2>3. Ethics Frameworks for AI in War</h2>
        <div style={{ border: '1px solid #ccc', padding: '20px' }}>
          <h3>Ethical Risk Calculator</h3>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
            <label>Autonomy Level: {ethicalParams.autonomy}</label>
            <input type="range" min="0" max="1" step="0.1" value={ethicalParams.autonomy} onChange={e => setEthicalParams({...ethicalParams, autonomy: parseFloat(e.target.value)})} />

            <label>Target Confidence: {ethicalParams.confidence}</label>
            <input type="range" min="0" max="1" step="0.1" value={ethicalParams.confidence} onChange={e => setEthicalParams({...ethicalParams, confidence: parseFloat(e.target.value)})} />

            <label>Civilian Density: {ethicalParams.density}</label>
            <input type="range" min="0" max="1" step="0.1" value={ethicalParams.density} onChange={e => setEthicalParams({...ethicalParams, density: parseFloat(e.target.value)})} />

            <label>Proportionality: {ethicalParams.proportionality}</label>
            <input type="range" min="0" max="1" step="0.1" value={ethicalParams.proportionality} onChange={e => setEthicalParams({...ethicalParams, proportionality: parseFloat(e.target.value)})} />
          </div>
          <button onClick={calculateEthicalScore} style={{ marginTop: '20px' }}>Calculate Risk Score</button>
          {ethicalScore !== null && (
            <div style={{ marginTop: '20px', fontSize: '24px', fontWeight: 'bold', color: ethicalScore > 50 ? 'red' : 'green' }}>
              Risk Score: {ethicalScore}/100
            </div>
          )}
        </div>
      </section>
    </div>
  );
};

export default ConflictDashboard;
