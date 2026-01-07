import { useState } from 'react';
import { toast } from 'react-hot-toast';
import { ingestDocument, ingestWeb } from '../api';

interface IngesterProps {
    onIngestComplete: (count: number) => void;
}

export const Ingester = ({ onIngestComplete }: IngesterProps) => {
    const [url, setUrl] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
        if (!e.target.files?.[0]) return;
        setLoading(true);
        setError('');
        const toastId = toast.loading('Uploading document...');
        try {
            const res = await ingestDocument(e.target.files[0]);
            onIngestComplete(res.data.chunks_added);
            toast.success('Document uploaded successfully!', { id: toastId });
        } catch (err) {
            console.error(err);
            setError('Failed to upload file.');
            toast.error('Failed to upload file.', { id: toastId });
        } finally {
            setLoading(false);
        }
    };

    const handleUrlSubmit = async () => {
        if (!url) return;
        setLoading(true);
        setError('');
        const toastId = toast.loading('Ingesting URL...');
        try {
            const res = await ingestWeb(url);
            onIngestComplete(res.data.chunks_added);
            setUrl('');
            toast.success('URL ingested successfully!', { id: toastId });
        } catch (err) {
            console.error(err);
            setError('Failed to ingest URL.');
            toast.error('Failed to ingest URL.', { id: toastId });
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="ingest-panel glass">
            <h2>📚 Knowledge Base</h2>
            <p className="description">Add documents or web pages to start searching.</p>

            <div className="upload-zone">
                <input
                    type="file"
                    id="file-upload"
                    hidden
                    onChange={handleFileUpload}
                    accept=".pdf,.txt"
                />
                <label htmlFor="file-upload" style={{ cursor: 'pointer' }}>
                    <div className="icon">📄</div>
                    <span>Click to upload PDF or TXT</span>
                </label>
            </div>

            <div className="divider">OR</div>

            <div className="url-input-group">
                <input
                    type="url"
                    className="input-field"
                    placeholder="https://example.com/article"
                    value={url}
                    onChange={(e) => setUrl(e.target.value)}
                />
                <button
                    className="primary-btn"
                    onClick={handleUrlSubmit}
                    disabled={loading || !url}
                >
                    {loading ? 'Adding...' : 'Add'}
                </button>
            </div>

            {error && <div className="error-msg">{error}</div>}
        </div>
    );
};
