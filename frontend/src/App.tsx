import { useEffect, useState } from 'react';
import './App.css';
import { Ingester } from './components/Ingester';
import { Chat } from './components/Chat';
import { clearSession, getSessionId } from './api';

function App() {
  const [sessionId] = useState(getSessionId());

  useEffect(() => {
    clearSession().catch(() => { });
  }, []);

  const handleManualClear = async () => {
    await clearSession();
    window.location.reload();
  }

  return (
    <div className="app-container">
      <header className="header glass">
        <div className="brand">
          🔍 SearchlyAI
        </div>
        <button onClick={handleManualClear} className="secondary-btn">
          Clear Session
        </button>
      </header>

      <main className="main-content container">
        <Ingester onIngestComplete={(count) => console.log(`Added ${count} chunks`)} />
        <Chat />
      </main>
    </div>
  );
}

export default App;
