import React from 'react';
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
                    <Nav className="mr-auto mx-auto">
                        <Nav.Link href="/">Home</Nav.Link>
                        <Nav.Link href="/about">About Us</Nav.Link>
                        <Nav.Link href="/downloads">Downloads</Nav.Link>
                        <Nav.Link href="/contributors">Contributors</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
        </>
    )
}

export default NavBar;