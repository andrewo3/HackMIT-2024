import React from 'react';
import "./navbar.css"

const WebsiteNavbar = () => {
  return (

<nav className="navbar">
  <div className="navbar-logo">
    <a href="/">HackMIT Project</a>
  </div>
  <div className="navbar-left">
    <a href="/">Test</a>
    <a href="/">Try</a>
  </div>
  <div className="navbar-right">
    <a href="/">About Us</a>
  </div>
</nav>
);
};

export default WebsiteNavbar;