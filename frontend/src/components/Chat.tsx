import { useState, useRef, useEffect } from 'react';
import { querySearch } from '../api';

interface Message {
    role: 'user' | 'ai';
    content: string;
    sources?: { content: string; score: number; source: string }[];
}

export const Chat = () => {
    const [query, setQuery] = useState('');
    const [history, setHistory] = useState<Message[]>([]);
    const [loading, setLoading] = useState(false);
    const bottomRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [history]);

    const handleSearch = async (e?: React.FormEvent) => {
        e?.preventDefault();
        if (!query.trim()) return;

        const userMsg: Message = { role: 'user', content: query };
        setHistory((prev) => [...prev, userMsg]);
        setQuery('');
        setLoading(true);

        try {
            const res = await querySearch(userMsg.content);
            const aiMsg: Message = {
                role: 'ai',
                content: res.data.answer,
                sources: res.data.sources
            };
            setHistory((prev) => [...prev, aiMsg]);
        } catch (err) {
            console.error(err);
            setHistory((prev) => [...prev, { role: 'ai', content: 'Sorry, something went wrong.' }]);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="chat-panel glass">
            <div className="chat-history">
                {history.length === 0 && (
                    <div className="placeholder-text">
                        <h3>Ready to help!</h3>
                        <p>Ask me anything about your documents.</p>
                    </div>
                )}
                {history.map((msg, idx) => (
                    <div key={idx} className={`message ${msg.role}`}>
                        <p>{msg.content}</p>
                        {msg.sources && msg.sources.length > 0 && (
                            <div className="source-badges">
                                {msg.sources.map((s, i) => (
                                    <div key={i} className="source-badge">
                                        Score: {s.score.toFixed(2)}
                                    </div>
                                ))}
                            </div>
                        )}
                    </div>
                ))}
                {loading && <div className="message ai">Thinking...</div>}
                <div ref={bottomRef} />
            </div>

            <form className="query-box" onSubmit={handleSearch}>
                <div className="input-group">
                    <input
                        type="text"
                        className="input-field"
                        placeholder="Ask a question..."
                        value={query}
                        onChange={(e) => setQuery(e.target.value)}
                        disabled={loading}
                    />
                    <button type="submit" className="primary-btn" disabled={loading}>
                        Send
                    </button>
                </div>
            </form>
        </div>
    );
};
