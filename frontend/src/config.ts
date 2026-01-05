export const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

export const getSessionId = (): string => {
    let sessionId = sessionStorage.getItem('searchly_session');
    if (!sessionId) {
        sessionId = crypto.randomUUID();
        sessionStorage.setItem('searchly_session', sessionId);
    }
    return sessionId;
};

export const clearSessionId = () => {
    sessionStorage.removeItem('searchly_session');
};
