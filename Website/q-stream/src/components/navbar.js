import React from 'react';
import { Link } from 'react-router-dom';
import { Navbar, Nav } from 'react-bootstrap';
import logo from '../Images/logo.jpg' ;
import './navbar.css';

function NavBar() {
    return (
        <>
            <Navbar expand="lg">
                <Navbar.Brand href="/">
                    <img
                        src={ logo }
                        width="40"
                        height="40"
                        className="d-inline-block align-top"
                        alt="Q-Stream logo"
                    />
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="mr-auto mx-auto navitems">
                        <Link to="/">Home</Link>
                        <Link to="/about">About Us</Link>
                        <Link to="/downloads">Downloads</Link>
                        <Link to="/contributors">Contributors</Link>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
        </>
    )
}

export default NavBar;