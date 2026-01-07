import { useEffect } from 'react';
import './App.css';
import { Ingester } from './components/Ingester';
import { Chat } from './components/Chat';
import { clearSession } from './api';
import { Toaster, toast } from 'react-hot-toast';

function App() {

  useEffect(() => {
    clearSession().catch(() => { });
  }, []);

  const handleManualClear = async () => {
    try {
      await clearSession();
      toast.success('Session cleared successfully');
      setTimeout(() => window.location.reload(), 1000);
    } catch (error) {
      console.error(error);
      toast.error('Failed to clear session');
    }
  }

  return (
    <div className="app-container">
      <Toaster position="top-right" />
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
