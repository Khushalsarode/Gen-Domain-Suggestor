// src/App.js
import React from 'react';
// index.js or App.js
import 'bootstrap/dist/css/bootstrap.min.css';
import PrivateRoute from './components/PrivateRoute';

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/navbar';
import Home from './pages/home';
import DomainAI from './pages/domainaI';
import DomainStatus from './pages/domainstatus';
import SurpriseMe from './pages/surpriseme';
import ChatAssistant from './pages/chatassistant';
import Blogs from './pages/blogs';
import About from './pages/about';
import './App.css';

const App = () => {
  return (
    <Router>
      <div className="app">
        <Navbar />
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/blogs" element={<Blogs />} />
            <Route path="/about" element={<About />} />

            {/* Protected Routes */}
            <Route path="/domain-ai" element={<PrivateRoute element={DomainAI} />} />
            <Route path="/domain-status" element={<PrivateRoute element={DomainStatus} />} />
            <Route path="/surprisem" element={<PrivateRoute element={SurpriseMe} />} />
            <Route path="/chatassistant" element={<PrivateRoute element={ChatAssistant} />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
};

export default App;
