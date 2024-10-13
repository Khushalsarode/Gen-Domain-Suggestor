import React from 'react';
import './About.css'; // Importing CSS for styles

const About = () => {
  return (
    <div className="about-container">
      <section className="about-header">
        <h1>About DomainSuggest</h1>
        <p>
          Welcome to <strong>DomainSuggest</strong>, where technology meets creativity. Our platform utilizes cutting-edge AI, including Gemini AI and Whosi's Domain API, to help you discover the perfect domain name for your website or project. Whether you're starting a blog, launching a business, or building a personal brand, we've got you covered.
        </p>
      </section>

      <section className="mission-section">
        <h2>Our Mission</h2>
        <p>
          At DomainSuggest, we aim to simplify the process of finding a unique, creative, and available domain name. We believe that the right domain name is key to your success online, and our tools are designed to make this crucial step quick, easy, and fun.
        </p>
      </section>

      <section className="how-it-works">
        <h2>How It Works</h2>
        <p>
          DomainSuggest combines the power of advanced AI with real-time domain availability checks to deliver tailored suggestions. Here's how:
        </p>
        <ul>
          <li><strong>AI-Powered Suggestions:</strong> Using the latest AI models, we generate creative and relevant domain name options based on your input.</li>
          <li><strong>Real-Time Availability:</strong> Integrated with Whosi’s Domain API, we ensure the domains suggested are available for immediate registration.</li>
          <li><strong>Customization:</strong> Filter domain suggestions based on keywords, industry, and top-level domain (TLD) preferences.</li>
        </ul>
      </section>

      <section className="team-section">
        <h2>Meet the Team</h2>
        <div className="team-grid">
          <div className="team-member">
            <img src="team-member-1.jpg" alt="Khushal Sarode" className="team-photo" />
            <h3>Khushal Sarode</h3>
            <p>Student</p>
          </div>
          <div className="team-member">
            <img src="team-member-2.jpg" alt="Vishakha Sarode" className="team-photo" />
            <h3>Vishakha Sarode</h3>
            <p>Student</p>
          </div>
        </div>
      </section>

      <section className="values-section">
        <h2>Our Values</h2>
        <ul>
          <li><strong>Innovation:</strong> We embrace technology to create forward-thinking solutions.</li>
          <li><strong>Simplicity:</strong> We make domain search as easy and efficient as possible.</li>
          <li><strong>Customer Focus:</strong> Your success is our priority, and we’re here to support you every step of the way.</li>
        </ul>
      </section>
    </div>
  );
};

export default About;
