import React from 'react';
import './Blogs.css'; // Import CSS for styles

const Blogs = () => {
  return (
    <div className="blogs-container">
      <header className="blogs-header">
        <h1>Our Blog</h1>
        <p>Explore the latest insights, trends, and tips on domain names and the digital landscape.</p>
      </header>
      
      <section className="featured-articles">
        <h2>Featured Articles</h2>
        <div className="articles-grid">
          <article className="article-card">
            <h3>Choosing the Perfect Domain Name</h3>
            <p>Learn the key considerations for selecting a domain name that enhances your brand's visibility.</p>
            <a href="#" className="read-more">Read more</a>
          </article>
          <article className="article-card">
            <h3>Top Domain Trends in 2024</h3>
            <p>Stay ahead of the curve with the latest domain name trends shaping the online world.</p>
            <a href="#" className="read-more">Read more</a>
          </article>
        </div>
      </section>

      <section className="recent-posts">
        <h2>Recent Posts</h2>
        <ul className="posts-list">
          <li><a href="#">How to Protect Your Domain from Expiring</a></li>
          <li><a href="#">5 Tips for Boosting Your Website's SEO</a></li>
          <li><a href="#">Why Your Business Needs a Custom Domain</a></li>
          <li><a href="#">Securing Domain Names for Future Projects</a></li>
        </ul>
      </section>

      <section className="blog-categories">
        <h2>Categories</h2>
        <ul className="categories-list">
          <li><a href="#">Domain Name Strategies</a></li>
          <li><a href="#">SEO & Web Performance</a></li>
          <li><a href="#">Branding & Marketing</a></li>
          <li><a href="#">Tech & Innovation</a></li>
        </ul>
      </section>
    </div>
  );
};

export default Blogs;
