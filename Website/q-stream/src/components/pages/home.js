import React, { useState } from 'react';
import { Jumbotron, Container, Modal, Button } from 'react-bootstrap';
import logo from '../../Images/logo.jpg';
import use from '../../Videos/use.mp4';
import './home.css';

function Home() {

    const [show, setShow] = useState(false);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    return (
        <div>
            <Jumbotron fluid>
                <Container fluid>
                    <h1><img className="logo"
                        src={logo}
                        width="50"
                        height="50"
                    /> Q-Stream Online Media Player</h1>
                    <h2>The Open Source Media Player which supports media from various media platforms such as Youtube, Twitch</h2>
                </Container>
            </Jumbotron>
            <Button className="use" onClick={handleShow}>How to Use</Button>
            <Button className="dnld">Download</Button>
            <Modal show={show} onHide={handleClose}>
                <Modal.Body>
                    <video width="100%" autoPlay controls>
                        <source src={use} type="video/mp4" />
                        Your browser does not support the video tag.
                    </video>
                </Modal.Body>
                {/* <Modal.Footer>
                    <Button variant="secondary" onClick={handleClose}>
                        Close
                    </Button>
                </Modal.Footer> */}
            </Modal>
        </div>
    )
}

export default Home;