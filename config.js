// Configuration for nGAGE AI Feedback Frontend
const config = {
    // Backend API URL - Update this with your Railway backend URL
    API_BASE_URL: window.location.hostname === 'localhost' 
        ? "http://localhost:5000" 
        : "https://web-production-c6d3.up.railway.app", // ✅ Updated with actual Railway URL
    
    // App settings
    APP_NAME: "nGAGE AI Feedback",
    VERSION: "1.0.0",
    
    // API endpoints
    ENDPOINTS: {
        GENERATE_FEEDBACK: "/api/generate-feedback",
        ANALYZE_CONTEXT: "/api/analyze-context",
        HEALTH: "/api/health",
        ANALYTICS: "/api/analytics",
        RECENT_FEEDBACK: "/api/recent-feedback",
        RECOMMEND_ATTRIBUTES: "/api/recommend-attributes",
        GET_ATTRIBUTES: "/api/attributes"
    }
};

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = config;
}
