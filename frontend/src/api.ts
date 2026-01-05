import axios from 'axios';
import { API_URL, getSessionId } from './config';
export { getSessionId };

const api = axios.create({
    baseURL: API_URL,
});

api.interceptors.request.use((config) => {
    config.headers['X-Session-ID'] = getSessionId();
    return config;
});

export const ingestDocument = async (file: File) => {
    const formData = new FormData();
    formData.append('file', file);
    return api.post('/ingest/document', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
    });
};

export const ingestWeb = async (url: string) => {
    return api.post('/ingest/web', { url });
};

export const querySearch = async (question: string) => {
    return api.post('/query', { question });
};

export const clearSession = async () => {
    const sessionId = getSessionId();
    return api.delete(`/session/${sessionId}`);
};
