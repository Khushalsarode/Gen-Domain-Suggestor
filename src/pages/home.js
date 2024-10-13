// src/pages/Home.js
import React from 'react';
import './Home.css'; // Include CSS for styling

const Home = () => {
  return (
    <div className="home-container">
      <header className="hero-section">
        <h1>Welcome to DomainSuggest</h1>
        <p>Your tool for finding the perfect domain name!</p>
        <a href="/domain-ai" className="cta-button">Get Started</a>
      </header>
      <section className="features-section">
        <h2>Features</h2>
        <div className="feature-cards">
          <div className="feature-card">
            <h3>Domain Search</h3>
            <p>Quickly search for available domain names with our intelligent suggestions.</p>
          </div>
          <div className="feature-card">
            <h3>AI Suggestions</h3>
            <p>Get AI-powered recommendations based on your keywords and preferences.</p>
          </div>
          <div className="feature-card">
            <h3>Domain Status</h3>
            <p>Check the status of your domains and receive real-time updates.</p>
          </div>
        </div>
      </section>
      <footer className="footer">
        <p>&copy; {new Date().getFullYear()} DomainSuggest. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default Home;
